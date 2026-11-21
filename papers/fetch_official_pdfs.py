#!/usr/bin/env python3
"""Fetch official published PDFs locally from the curated manifest.

This is a user-invoked local utility: it does NOT claim to upload PDFs to GitHub.
Do not redistribute downloaded files unless the specific publisher/license allows it.
"""
import argparse
import csv
import pathlib
import re
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default=str(ROOT / "downloaded-official-pdfs"))
    parser.add_argument("--tier", choices=["A", "B", "all"], default="A")
    parser.add_argument("--only-licensed", action="store_true",
                        help="Only fetch rows provisionally tagged CC-BY-4.0; still verify license")
    args = parser.parse_args()
    dest = pathlib.Path(args.output)
    dest.mkdir(parents=True, exist_ok=True)
    rows = csv.DictReader((ROOT / "core-conference-manifest.csv").open(encoding="utf-8"))
    for row in rows:
        if args.tier != "all" and row["priority"] != args.tier:
            continue
        if args.only_licensed and row["archive_policy"] != "CC-BY-4.0":
            continue
        name = re.sub(r"[^A-Za-z0-9_.-]", "_", row["id"]) + ".pdf"
        output = dest / name
        if output.exists():
            print("skip", output.name)
            continue
        req = urllib.request.Request(row["official_pdf_url"],
                                     headers={"User-Agent": "academic-literature-fetch/1.0"})
        try:
            with urllib.request.urlopen(req, timeout=45) as response:
                data = response.read()
                if not data.startswith(b"%PDF-"):
                    raise ValueError("Publisher did not return a PDF")
                output.write_bytes(data)
                print("saved", output)
        except Exception as exc:
            print("FAILED", row["id"], row["official_pdf_url"], str(exc))
    print("Downloaded PDFs are local only. Check license before public GitHub mirroring.")

if __name__ == "__main__":
    main()
