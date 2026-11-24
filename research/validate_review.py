#!/usr/bin/env python3
"""Deterministic consistency checks for the review's *candidate* Markdown collection.

This validates documentation integrity, NOT PRISMA completeness or study validity.
Uses only Python's standard library; no network or CSV files needed.
"""
from __future__ import annotations

import collections
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "literature" / "prisma-core-papers.md"
AUDIT = ROOT / "research" / "PRISMA-2020-audit.md"
VENUES = {"ICLR", "ICML", "NeurIPS", "CHI", "ACL", "EMNLP", "NAACL"}
HOSTS = {
    "aclanthology.org", "proceedings.neurips.cc",
    "proceedings.iclr.cc", "proceedings.mlr.press", "doi.org",
}

def main() -> int:
    issues = []
    text = DOC.read_text(encoding="utf-8")
    audit = AUDIT.read_text(encoding="utf-8")
    if "## Study catalog by survey question" not in text or "## Five new" not in text:
        raise ValueError("Missing candidate section delimiters")
    selection = text.split("## Study catalog by survey question", 1)[1].split("## Five new", 1)[0]
    table_pat = re.compile(
        r"^\| \[([^]]+)\]\((https?://[^)]+)\) \(([^)]+)\) \| (E|S) \|",
        re.M,
    )
    bullets_pat = re.compile(r"^- \[([^]]+)\]\((https?://[^)]+)\) \(([^)]+)\) — ", re.M)
    items = [
        {"title": title, "url": url, "label": label, "tier": tier}
        for title, url, label, tier in table_pat.findall(selection)
    ] + [
        {"title": title, "url": url, "label": label, "tier": "E/S stated in bullet"}
        for title, url, label in bullets_pat.findall(selection)
    ]
    match = re.search(r"\*\*(\d+) unique candidate records\*\*", text)
    if not match:
        issues.append("Missing explicit candidate count")
    elif int(match.group(1)) != len(items):
        issues.append(f"Declared count {match.group(1)} != parsed {len(items)}")
    if len({x["url"] for x in items}) != len(items):
        issues.append("Duplicate official publication link")
    if len({re.sub(r"\W+", "", x["title"].lower()) for x in items}) != len(items):
        issues.append("Duplicate normalized titles")

    venue_counts = collections.Counter()
    for item in items:
        parsed = urlparse(item["url"])
        if parsed.hostname not in HOSTS:
            issues.append(f"Unapproved publication host for {item['title']}: {parsed.hostname}")
        venue = re.match(r"(ICLR|ICML|NeurIPS|CHI|ACL|EMNLP|NAACL) (20\d{2})", item["label"])
        if not venue or venue.group(1) not in VENUES:
            issues.append(f"Unparseable venue for {item['title']}: {item['label']}")
            continue
        venue_counts[venue.group(1)] += 1

    if "Not established" not in audit and "**Not established**" not in audit:
        issues.append("PRISMA audit no longer explicitly identifies unobserved counts")
    if not any(phrase in text for phrase in (
        "NOT an exhaustive database-derived inclusion sample",
        "**NOT** an exhaustive database-derived inclusion sample",
    )):
        issues.append("Candidate metadata must not imply completed PRISMA sample")

    # Enforce *internal* section counts, not a fixed preferred publication quota.
    section_pat = re.compile(r"^### (.+?) \((\d+) candidates\)\n(.*?)(?=^### |\Z)", re.M | re.S)
    for heading, expected, block in section_pat.findall(selection):
        actual = len(table_pat.findall(block))
        if actual != int(expected):
            issues.append(f"Section {heading}: {expected} declared but {actual} table entries")

    result = {
        "candidate_records": len(items),
        "venue_counts": dict(sorted(venue_counts.items())),
        "unique_official_links": len({x["url"] for x in items}),
        "review_type": "candidate evidence map; not completed PRISMA selection",
        "passed": not issues,
        "errors": issues,
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 1 if issues else 0

if __name__ == "__main__":
    sys.exit(main())
