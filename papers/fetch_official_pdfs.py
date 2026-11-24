#!/usr/bin/env python3
"""Download official publisher PDF URLs from the curated CSV to a LOCAL ignored folder.

Does not commit to GitHub. Check paper-specific redistribution licenses before sharing.
"""
import argparse
import csv
import pathlib
import re
import urllib.request

HERE = pathlib.Path(__file__).resolve().parent

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=pathlib.Path, default=HERE / "downloaded-official-pdfs")
    parser.add_argument("--priority", choices=["E", "S", "all"], default="E")
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    with (HERE / "core-conference-manifest.csv").open(encoding="utf-8", newline="") as stream:
        rows = list(csv.DictReader(stream))
    for row in rows:
        if args.priority != "all" and row["priority_E_essential_S_supporting"] != args.priority:
            continue
        url = row["official_pdf_url_if_located"]
        if not url:
            print("NO DIRECT PUBLISHER PDF:", row["paper_id"], row["official_publication_url"])
            continue
        name = re.sub(r"[^A-Za-z0-9_.-]", "_", row["paper_id"]) + ".pdf"
        destination = args.output / name
        if destination.exists():
            print("EXISTS:", destination.name)
            continue
        request = urllib.request.Request(url, headers={"User-Agent":"AcademicSurveyResearch/1.0"})
        try:
            with urllib.request.urlopen(request, timeout=40) as response:
                data = response.read()
            if not data.startswith(b"%PDF-"):
                raise ValueError("No PDF magic header")
            destination.write_bytes(data)
            print("SAVED:", destination.name)
        except Exception as exc:
            print("FAILED:", row["paper_id"], str(exc))
    print("Local research copies only; do not upload without checking redistribution rights.")

if __name__ == "__main__":
    main()
