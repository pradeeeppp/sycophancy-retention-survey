"""Replay on ACL Anthology revision 37f8244b23f7647a84173868f26bb0f52fb2cb77."""
import argparse
import csv
import re
import sys
from pathlib import Path
from xml.etree import ElementTree

TITLE = re.compile(r"\b(sycophan\w*|apolog(?:y|ies|iz\w*|is\w*)|acknowledg\w*|conformity|peer pressure|groupthink|social pressure|user disagreement|second.guesser|vacillations?|grounding gaps|taking feedback gracefully|misleading scenarios|debate.aware learning|consistency illusion|rational updating|(?:resisting|accepting) persuasion)\b", re.IGNORECASE)
COLLECTIONS = """2022.acl 2022.emnlp 2022.naacl 2023.acl 2023.eacl 2023.emnlp 2024.acl 2024.eacl 2024.emnlp 2024.naacl 2025.acl 2025.emnlp 2025.naacl 2026.acl 2026.eacl 2026.emnlp""".split()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("checkout", type=Path)
    args = parser.parse_args()
    writer = csv.writer(sys.stdout, lineterminator="\n")
    writer.writerow(["id", "title"])
    for collection in COLLECTIONS:
        source = args.checkout / "data" / "xml" / (collection + ".xml")
        for volume in ElementTree.parse(source).getroot().findall("volume"):
            track = volume.attrib["id"]
            if track not in {"main", "long", "short"}:
                continue
            for paper in volume.findall("paper"):
                number = paper.attrib["id"]
                title = paper.find("title")
                if number == "0" or title is None:
                    continue
                text = " ".join("".join(title.itertext()).split())
                if TITLE.search(text):
                    writer.writerow([f"{collection}-{track}.{number}", text])


if __name__ == "__main__":
    main()
