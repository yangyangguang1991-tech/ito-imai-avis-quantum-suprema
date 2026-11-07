"""Replay an entry's complete mathematical certificate using bundled inputs."""
from pathlib import Path, PurePosixPath
from itertools import product
import argparse, hashlib, json, os, re, struct, subprocess, sys, tempfile, zipfile

ROOT = Path(__file__).resolve().parent
UNKNOWN = frozenset((14, 21, 47, 62, 64, 68, 82, 84, 89))

def require(condition, message):
    if not condition:
        raise ValueError(message)

def inside(root, name):
    p = PurePosixPath(name)
    require(name and not p.is_absolute() and '..' not in p.parts and '\\' not in name,
            f'Unsafe relative path: {name}')
    result = (root / name).resolve()
    require(result.is_relative_to(root.resolve()), f'Path escapes its directory: {name}')
    return result

def extract(z, target):
    names = z.namelist()
    require(len(names) == len({n.casefold() for n in names}), 'Duplicate archive members.')
    for name in names:
        inside(target, name)
    target = target.resolve()
    if os.name == 'nt' and not str(target).startswith('\\\\?\\'):
        text = str(target)
        target = Path('\\\\?\\UNC\\' + text[2:] if text.startswith('\\\\') else '\\\\?\\' + text)
    z.extractall(target)

def unpack_parts(directory, config, target):
    with tempfile.TemporaryFile() as archive:
        h = hashlib.sha256()
        for name in config['parts']:
            with inside(directory, name).open('rb') as source:
                while block := source.read(4 << 20):
                    archive.write(block)
                    h.update(block)
        require(h.hexdigest() == config['sha256'], 'Archive SHA256 mismatch.')
        with zipfile.ZipFile(archive) as z:
            extract(z, target)

def reflect(C):
    T = [r.copy() for r in C]
    T[0][0] = (4*C[0][0] + 2*sum(r[0] for r in C[1:])
               + 2*sum(C[0][1:]) + sum(sum(r[1:]) for r in C[1:]))
    for i in range(1, len(C)):
        T[i][0] = 2*C[i][0] + sum(C[i][1:])
    for j in range(1, len(C[0])):
        T[0][j] = 2*C[0][j] + sum(r[j] for r in C[1:])
    return T

def definition(number):
    e = ROOT / 'entries' / f'A{number:02d}'
    row = json.loads((e / 'definition.json').read_text(encoding='utf-8-sig'))
    C, m, n = row['probability_matrix'], row['m'], row['n']
    require(row['id'] == number, 'Entry number mismatch.')
    require(len(C) == m+1 and all(len(r) == n+1 for r in C), 'Coefficient shape mismatch.')
    require(all(type(v) is int for r in C for v in r), 'Coefficients must be integers.')
    if number != 1:
        source = row['literal_polynomial']
        terms = re.findall(r'[+-]?\d+(?:\*[XY]\d+)*', source)
        require(''.join(terms) == source, 'Literal polynomial parse mismatch.')
        recovered = [[0]*(n+1) for _ in range(m+1)]
        for term in terms:
            value, *letters = term.split('*')
            x = [int(w[1:]) for w in letters if w.startswith('X')]
            y = [int(w[1:]) for w in letters if w.startswith('Y')]
            require(len(x) <= 1 and len(y) <= 1, 'Unexpected polynomial monomial.')
            recovered[x[0] if x else 0][y[0] if y else 0] += row['multiplier_for_maximization']*int(value)
        require(recovered == C, 'Literal source / probability table mismatch.')
    require(reflect(C) == row['four_times_reflection_matrix'], 'Reflection conversion mismatch.')
    maximum = max(sum(C[i][j]*a*b for i,a in enumerate((1,*x)) for j,b in enumerate((1,*y)))
                  for x in product((0,1), repeat=m) for y in product((0,1), repeat=n))
    require(maximum == row['local_max'] == 0, 'Deterministic local maximum mismatch.')
    return e, row

def check_tables(core, config, row):
    require(config.get('table_bindings'), 'Missing functional binding.')
    for binding in config['table_bindings']:
        require(binding['kind'] == 'json', 'Unsupported functional binding.')
        require(binding['equals'] in ('probability_matrix','four_times_reflection_matrix'),
                'A functional binding must compare a complete Bell coefficient table.')
        value = json.loads(inside(core, binding['file']).read_text(encoding='utf-8-sig'))
        for key in binding['path']:
            value = value[key]
        expected = row[binding['equals']]
        if binding.get('padded'):
            m, n = row['m'], row['n']
            require(not any(value[i][j] for i in range(len(value)) for j in range(len(value[i]))
                            if i > m or j > n), 'Nonzero inactive setting.')
            value = [r[:n+1] for r in value[:m+1]]
        if binding.get('flatten'):
            expected = [v for r in expected for v in r]
        require(value == expected, 'Bell functional binding failed: ' + binding['file'])

def unpack(entry, core, row):
    config = json.loads((entry / 'proof.json').read_text(encoding='utf-8'))
    commands = config.get('commands')
    require(isinstance(commands, list) and bool(commands), 'The complete proof command list must not be empty.')
    for command in commands:
        args = [command] if isinstance(command, str) else command
        require(isinstance(args, list) and bool(args) and all(isinstance(v,str) and v for v in args),
                'Invalid proof command or empty argument.')
    unpack_parts(entry, config, core)
    check_tables(core, config, row)
    return config

def runtime(folder):
    require(os.name == 'nt' and sys.version_info[:2] == (3,12) and struct.calcsize('P') == 8,
            'The bundled numerical runtime requires 64-bit Windows and CPython 3.12. See MANUAL.md.')
    directory = ROOT / 'runtime'
    config = json.loads((directory / 'manifest.json').read_text(encoding='utf-8'))
    vendor = folder / 'libraries'
    vendor.mkdir()
    unpack_parts(directory, config, vendor)
    return vendor

def run(number, vendor):
    entry, row = definition(number)
    if number in UNKNOWN:
        require(not (entry / 'proof.json').exists(), 'Unexpected proof for an unresolved entry.')
        print(f'A{number}: Exact unrestricted quantum supremum: unknown.', flush=True)
        return
    env = dict(os.environ)
    env.update(PYTHONOPTIMIZE='', PYTHONUTF8='1', PYTHONDONTWRITEBYTECODE='1',
               PYTHONNOUSERSITE='1', PYTHONPATH=str(vendor) if vendor else '',
               BELL_BLAS_THREADS='1', OMP_NUM_THREADS='1', OPENBLAS_NUM_THREADS='1', MKL_NUM_THREADS='1')
    with tempfile.TemporaryDirectory(prefix=f'bell_a{number:02d}_') as temporary:
        core = Path(temporary)
        config = unpack(entry, core, row)
        require(config.get('command_directory') == 'script_parent', 'Unknown command directory convention.')
        for command in config['commands']:
            args = [command] if isinstance(command, str) else command
            require(args and not any(a in ('-O','-OO') for a in args), 'Optimized verification is not permitted.')
            script = inside(core, args[0])
            print(f'Running A{number}: ' + ' '.join(args), flush=True)
            try:
                subprocess.run([sys.executable, '-B', '-X', 'utf8', str(script), *args[1:]],
                               cwd=script.parent, env=env, check=True)
            except subprocess.CalledProcessError:
                logs = sorted(core.rglob('*.log'), key=lambda f:f.stat().st_mtime, reverse=True)
                for log in logs[:4]:
                    with log.open('rb') as f:
                        f.seek(max(0, log.stat().st_size - 4000))
                        print(str(log.relative_to(core)), f.read().decode('utf8','replace'), file=sys.stderr)
                raise
    print(f'PASS A{number:02d}', flush=True)

def main():
    if not __debug__:
        raise SystemExit('Assertions must be enabled; do not use python -O or -OO.')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('number', nargs='?', type=int)
    parser.add_argument('--all', action='store_true')
    parser.add_argument('--extract', type=Path)
    parser.add_argument('--definitions-only', action='store_true')
    args = parser.parse_args()
    if args.all == (args.number is not None):
        parser.error('Choose one entry number or --all.')
    if args.number is not None and not 1 <= args.number <= 89:
        parser.error('Choose a number from 1 to 89.')
    numbers = list(range(1,90)) if args.all else [args.number]
    if args.extract:
        if args.all or args.definitions_only or args.number in UNKNOWN:
            parser.error('--extract requires one closed entry.')
        entry, row = definition(args.number)
        args.extract.mkdir(parents=True, exist_ok=False)
        unpack(entry, args.extract, row)
        print('Extracted certificate and checked the original Bell functional.', flush=True)
    elif args.definitions_only:
        for n in numbers:
            definition(n)
        print('PASS: all selected literal definitions and local bounds.', flush=True)
    else:
        with tempfile.TemporaryDirectory(prefix='bell_libraries_') as folder:
            vendor = runtime(Path(folder)) if any(n not in UNKNOWN and n not in (1,2,3) for n in numbers) else None
            for n in numbers:
                run(n, vendor)

if __name__ == '__main__':
    main()
