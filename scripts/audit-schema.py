#!/usr/bin/env python3
"""Check every schema file against the house rules in schema/README.md.

Usage:
    python3 scripts/audit-schema.py            # audit and report
    python3 scripts/audit-schema.py --fix      # fix what can be fixed safely

Exit code is 0 when everything passes, 1 when something fails, so this can run
in CI.
"""

import glob
import json
import os
import re
import sys

CANONICAL_ORG_ID = "https://www.piratesoftokyobay.com/#organization"
BAD_GITHUB = "github.com/PiratesOfTokyoBay"
GOOD_GITHUB = "github.com/Pirates-of-Tokyo-Bay"
OUR_NAMES = {"Pirates of Tokyo Bay", "パイレーツ・オブ・東京湾"}
ORG_TYPES = ("PerformingGroup", "Organization")

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def walk(node, fn):
    """Call fn on every dict in the tree."""
    if isinstance(node, dict):
        fn(node)
        for value in node.values():
            walk(value, fn)
    elif isinstance(node, list):
        for value in node:
            walk(value, fn)


def audit(path, fix=False):
    raw = open(path, encoding="utf-8").read()
    problems = []
    fixes = []

    if BAD_GITHUB in raw:
        count = raw.count(BAD_GITHUB)
        problems.append(f"broken GitHub URL x{count} (that account 404s)")
        if fix:
            raw = raw.replace(BAD_GITHUB, GOOD_GITHUB)
            fixes.append(f"replaced GitHub URL x{count}")

    if "http://www.piratesoftokyobay" in raw:
        problems.append("http:// link to our own site, should be https://")

    if re.search(r"bilingual|バイリンガル", raw, re.IGNORECASE):
        problems.append('BANNED WORD: "bilingual" (see brand.json)')

    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        return [f"INVALID JSON: {exc}"], []

    def check(node):
        if node.get("@type") in ORG_TYPES and node.get("name") in OUR_NAMES:
            if node.get("@id") != CANONICAL_ORG_ID:
                problems.append(
                    f"org node @id is {node.get('@id', 'MISSING')}, should be canonical"
                )
                if fix:
                    node["@id"] = CANONICAL_ORG_ID
                    fixes.append("set org @id to canonical")
        lang = node.get("inLanguage")
        if isinstance(lang, list) and lang[:2] == ["en", "ja"]:
            problems.append("inLanguage is English first, should be Japanese first")
            if fix:
                node["inLanguage"] = ["ja", "en"]
                fixes.append("reordered inLanguage to Japanese first")

    walk(data, check)

    if fix and fixes:
        with open(path, "w", encoding="utf-8") as handle:
            json.dump(data, handle, ensure_ascii=False, indent=2)
            handle.write("\n")

    return problems, fixes


def main():
    fix = "--fix" in sys.argv
    paths = sorted(glob.glob(os.path.join(REPO, "schema", "*.json")))
    paths += sorted(glob.glob(os.path.join(REPO, "schema", "_parked", "*.json")))
    paths = [p for p in paths if not p.endswith("index.json")]

    failed = 0
    for path in paths:
        name = os.path.relpath(path, REPO)
        problems, fixes = audit(path, fix=fix)
        if fixes:
            print(f"FIXED  {name}")
            for item in fixes:
                print(f"       {item}")
        remaining = problems if not fix else [p for p in problems if not fixes]
        if remaining and not fixes:
            failed += 1
            print(f"FAIL   {name}")
            for item in remaining:
                print(f"       {item}")
        elif not problems:
            print(f"ok     {name}")

    print(f"\n{len(paths)} files checked, {failed} with problems")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
