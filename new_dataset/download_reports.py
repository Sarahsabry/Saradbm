#!/usr/bin/env python3
"""Download annual reports listed in manifest.csv and save them as Country_Bankname_year.pdf.

Fill the `url` column of manifest.csv with the direct PDF link for each bank/year,
then run on your own computer:

    python3 download_reports.py manifest.csv "/Users/home/Documents/My Research/SaraHanan/New dataset"

Rows with an empty url are skipped; files that already exist are not re-downloaded.
"""
import csv
import re
import sys
import urllib.request
from pathlib import Path


def clean(text):
    text = re.sub(r"\(.*?\)", "", text)          # drop "(formerly ...)" / abbreviations
    text = re.sub(r"[^A-Za-z0-9]+", "", text.title())
    return text


def main(manifest, out_dir):
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    ok, failed = 0, []
    with open(manifest, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            url = row["url"].strip()
            if not url:
                continue
            name = f"{clean(row['country'])}_{clean(row['bank_name'])}_{row['year']}.pdf"
            dest = out / name
            if dest.exists():
                continue
            try:
                req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
                with urllib.request.urlopen(req, timeout=120) as r:
                    data = r.read()
                if not data.startswith(b"%PDF"):
                    raise ValueError("response is not a PDF")
                dest.write_bytes(data)
                ok += 1
                print("saved", name)
            except Exception as e:
                failed.append((name, url, str(e)))
                print("FAILED", name, e)
    print(f"\n{ok} downloaded, {len(failed)} failed")
    if failed:
        with open(out / "failed_downloads.csv", "w", newline="") as f:
            csv.writer(f).writerows([("file", "url", "error"), *failed])


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2])
