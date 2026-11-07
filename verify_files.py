"""Check the byte-level integrity of the distributed files (not their mathematical claims)."""
from pathlib import Path
import argparse, hashlib, sys

ROOT = Path(__file__).resolve().parent

def check(root, source_only=False):
    manifest = 'SOURCE_FILES.sha256' if source_only else 'SHA256SUMS.txt'
    expected = {}
    for line in (root / manifest).read_text(encoding="utf-8-sig").splitlines():
        if not line:
            continue
        digest, name = line.split("  ", 1)
        path = root / name
        if name in expected or len(digest) != 64 or any(c not in "0123456789abcdef" for c in digest):
            raise ValueError("Invalid or duplicate manifest entry: " + name)
        if not path.resolve().is_relative_to(root.resolve()):
            raise ValueError("Manifest path outside the catalogue: " + name)
        expected[name] = digest
    if not expected:
        raise ValueError('The file manifest must not be empty.')
    for name, digest in expected.items():
        if not (root / name).is_file():
            raise ValueError('Missing distributed file: ' + name +
                             '. Add the complete release data for a full integrity check; '
                             'use --source-only to check only the lightweight Git edition.')
        with (root / name).open("rb") as stream:
            actual = hashlib.file_digest(stream, "sha256").hexdigest()
        if actual != digest:
            raise ValueError("File digest mismatch: " + name)
    scope = 'source-edition' if source_only else 'complete-edition'
    print("PASS", len(expected), scope, "file hashes. Mathematical replay is separate.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-only', action='store_true',
                        help='Check the lightweight source edition; does not certify payload availability.')
    args = parser.parse_args()
    check(ROOT, args.source_only)
