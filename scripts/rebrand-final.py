#!/usr/bin/env python3
"""Final rebrand pass - catch remaining hermes references."""
import os
from pathlib import Path

SRC = Path("/root/kopi-ai-agent")
SKIP = {".git", "__pycache__", "node_modules", ".venv", "venv"}

replacements = [
    ('"kopi"', '"kopi"'),
    ("'kopi'", "'kopi'"),
    ("kopi-cli", "kopi-cli"),
    ("kopi-weixin", "kopi-weixin"),
    ("kopi-default", "kopi-default"),
    ("kopi-assistant", "kopi-assistant"),
    ("kopi-mux:", "kopi-mux:"),
    ("kopi/", "kopi/"),
    ("`kopi`", "`kopi`"),
    ("the kopi", "the kopi"),
    ("kopi.exe", "kopi.exe"),
]

count = 0
for f in SRC.rglob("*.py"):
    rel = f.relative_to(SRC)
    if any(p in SKIP for p in rel.parts):
        continue
    try:
        content = f.read_text(encoding="utf-8", errors="replace")
    except Exception:
        continue
    original = content
    for old, new in replacements:
        content = content.replace(old, new)
    if content != original:
        f.write_text(content, encoding="utf-8")
        count += 1

print(f"Changed {count} files")
