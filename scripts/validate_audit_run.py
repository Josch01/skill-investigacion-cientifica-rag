#!/usr/bin/env python3
"""Lightweight deterministic checks for manuscript-audit run artifacts."""

from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

GENERIC_PHRASES = [
    "standard assumptions",
    "previous lemmas and theorems",
    "pending rigorous closure",
    "attempted refutation",
    "needs more scrutiny",
]


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: validate_audit_run.py AUDIT_DIRECTORY")
        return 2

    root = Path(sys.argv[1])
    errors: list[str] = []
    warnings: list[str] = []

    if not root.is_dir():
        print("AUDIT RUN VALIDATION: FAIL")
        print("- audit directory does not exist")
        return 1

    md_files = list(root.glob("*.md"))
    if not md_files:
        errors.append("no markdown audit artifacts found")

    for path in md_files:
        text = path.read_text(encoding="utf-8", errors="replace")
        if not text.strip():
            errors.append(f"empty artifact: {path.name}")
        low = text.lower()
        for phrase in GENERIC_PHRASES:
            if low.count(phrase) >= 3:
                warnings.append(f"{path.name}: repeated boilerplate phrase '{phrase}' x{low.count(phrase)}")

    # Detect suspicious repeated substantive blocks across claim sections.
    for path in md_files:
        text = path.read_text(encoding="utf-8", errors="replace")
        blocks = [
            re.sub(r"\s+", " ", b.strip().lower())
            for b in re.split(r"(?m)^#{2,4}\s+", text)
            if len(b.strip()) >= 180
        ]
        counts = Counter(blocks)
        for block, count in counts.items():
            if count >= 3:
                warnings.append(f"{path.name}: identical long section body repeated {count} times")
                break

    # Coverage report should exist for a full manuscript audit.
    coverage = root / "15_AUDIT_COVERAGE_REPORT.md"
    if coverage.exists():
        text = coverage.read_text(encoding="utf-8", errors="replace")
        for token in [
            "N_FORMAL_OBJECTS",
            "N_CENTRAL_CLAIMS",
            "AUDITED_FORMAL_OBJECTS",
            "N_SECOND_REVIEW_REQUIRED",
            "N_SECOND_REVIEW_COMPLETE",
            "AUDIT_COVERAGE_STATUS",
        ]:
            if token not in text:
                errors.append(f"{coverage.name}: missing {token}")

    if errors:
        print("AUDIT RUN VALIDATION: FAIL")
        for item in errors:
            print(f"- {item}")
        for item in warnings:
            print(f"! {item}")
        return 1

    print("AUDIT RUN VALIDATION: PASS")
    for item in warnings:
        print(f"! {item}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
