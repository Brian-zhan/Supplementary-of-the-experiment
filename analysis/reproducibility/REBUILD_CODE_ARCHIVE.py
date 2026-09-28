#!/usr/bin/env python3
from pathlib import Path
import base64, hashlib

root = Path(__file__).resolve().parent
parts = sorted((root / "code_parts").glob("code_part*.b64"))
if len(parts) != 16:
    raise SystemExit(f"Expected 16 parts, found {len(parts)}")

b64 = "".join(p.read_text(encoding="utf-8").strip() for p in parts)
payload = base64.b64decode(b64, validate=True)
out = root / "Prebunking_Scapegoating_R453_Inferential_Code_COMPLETE.zip"
out.write_bytes(payload)

sha = hashlib.sha256(payload).hexdigest()
expected = "81d505d2acf6efb5ca2483d433f12291314d0ad218c3ab00744bf1ef54675312"
if sha != expected:
    raise SystemExit(f"SHA-256 mismatch: {sha}")
if len(payload) != 112625:
    raise SystemExit(f"Unexpected byte size: {len(payload)}")

print(f"Wrote {out.name}")
print(f"Bytes: {len(payload)}")
print(f"SHA-256: {sha}")
