#!/usr/bin/env python3
"""Reproduce observed counts in the *repository-bounded* PRISMA screening audit.

This deliberately does NOT report a completed multi-database systematic-review
inclusion total. Input is frozen JSONL, not an external unrepeatable web search.
No CSV or third-party Python dependencies are required.

Usage:
  python research/reproduce-screening-counts.py
  python research/reproduce-screening-counts.py --check
"""
import argparse
from collections import Counter
import json
from pathlib import Path

BASE = Path(__file__).resolve().parent
SOURCE = BASE / "repository-screening-snapshot-2026-11-21.jsonl"
EXPECTED = {
    "initial_52": 52,
    "acl_screen_30": 30,
    "historical_31_core": 31,
    "readme_69": 69,
    "2026_11_21_review_34": 34,
    "new_targeted_publisher_3": 3,
}
ALLOWED = {"advance_fulltext", "exclude_metadata_screen"}

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--check", action="store_true", help="Fail if counts or fields are inconsistent")
    args = p.parse_args()
    rows = [json.loads(line) for line in SOURCE.read_text(encoding="utf-8").splitlines() if line.strip()]
    errors = []
    sources = Counter()
    decisions = Counter()
    exclusions = Counter()
    strata = Counter()
    ids = set()
    urls = set()

    for idx, r in enumerate(rows, start=1):
        for key in ("id", "title", "url", "sightings", "decision", "primary_reason", "stratum", "fulltext_status"):
            if key not in r:
                errors.append(f"row {idx}: missing {key}")
        rid = r["id"]
        if rid in ids:
            errors.append(f"duplicate record id: {rid}")
        ids.add(rid)
        if r["url"] in urls:
            errors.append(f"duplicate primary publication URL: {r['url']}")
        urls.add(r["url"])
        if r["decision"] not in ALLOWED:
            errors.append(f"row {idx}: invalid decision {r['decision']}")
        decisions[r["decision"]] += 1
        strata[r["stratum"]] += 1
        if r["decision"] == "exclude_metadata_screen":
            exclusions[r["primary_reason"]] += 1
        for item in r["sightings"]:
            if not item.get("url") or not item.get("source"):
                errors.append(f"row {idx}: incomplete provenance")
            sources[item["source"]] += 1

    raw = sum(sources.values())
    unique = len(rows)
    result = {
        "scope": "KNOWN REPOSITORY INVENTORIES plus 3 publisher discoveries, not exhaustive conference-database search",
        "source_occurrences": dict(sorted(sources.items())),
        "total_catalog_sightings": raw,
        "distinct_reports": unique,
        "repeated_catalog_sightings_removed": raw - unique,
        "metadata_screen_excluded": decisions["exclude_metadata_screen"],
        "advance_to_fulltext_queue": decisions["advance_fulltext"],
        "advance_strata": dict(sorted((k,v) for k,v in strata.items() if k.endswith("_candidate"))),
        "all_strata": dict(sorted(strata.items())),
        "exclusion_reasons": dict(sorted(exclusions.items())),
        "targeted_method_checked": sum(r["fulltext_status"] == "targeted_fulltext_method_inspection" for r in rows),
        "final_prisma_included_studies": None,
    }
    if set(sources) != set(EXPECTED):
        errors.append("unexpected/missing provenance source names")
    if sources != Counter(EXPECTED):
        errors.append(f"source counts changed: expected {EXPECTED}, got {dict(sources)}")
    if sum(decisions.values()) != len(rows):
        errors.append("record-to-decision mismatch")
    if sum(exclusions.values()) != decisions["exclude_metadata_screen"]:
        errors.append("exclusion-count mismatch")
    if not (raw == 219 and unique == 89 and decisions["advance_fulltext"] == 55 and decisions["exclude_metadata_screen"] == 34):
        errors.append("observed bounded-flow counts changed; update reporting and verify sources")
    if result["targeted_method_checked"] != 6:
        errors.append("source-PDF method inspection count changed; update evidence notes")
    result["checks_pass"] = not errors
    result["errors"] = errors
    print(json.dumps(result, indent=2, ensure_ascii=False))
    if args.check and errors:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
