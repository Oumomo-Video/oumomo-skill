#!/usr/bin/env python3
"""Validate the structure of every skill in this repository.

Checks per skill under skills/<name>/:
  - SKILL.md exists and starts with a valid YAML frontmatter block
  - frontmatter contains required keys: name, description, when_to_use, license
  - frontmatter name matches the directory name
  - every relative link in SKILL.md resolves to an existing file
  - every YAML file under agents/ parses
"""

import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"
REQUIRED_KEYS = ("name", "description", "when_to_use", "license")


def check_skill(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    name = skill_dir.name
    md = skill_dir / "SKILL.md"

    if not md.is_file():
        return [f"{name}: missing SKILL.md"]

    text = md.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
    if not match:
        return [f"{name}: SKILL.md has no YAML frontmatter"]

    try:
        meta = yaml.safe_load(match.group(1))
    except yaml.YAMLError as exc:
        return [f"{name}: invalid frontmatter YAML: {exc}"]

    if not isinstance(meta, dict):
        return [f"{name}: frontmatter is not a mapping"]

    for key in REQUIRED_KEYS:
        if not meta.get(key):
            errors.append(f"{name}: missing frontmatter key '{key}'")

    if meta.get("name") and meta["name"] != name:
        errors.append(
            f"{name}: frontmatter name '{meta['name']}' != directory name '{name}'"
        )

    for link in re.findall(r"\]\((?!https?://|#)([^)]+)\)", text):
        target = (skill_dir / link.split("#")[0]).resolve()
        if not target.exists():
            errors.append(f"{name}: broken relative link '{link}'")

    agents_dir = skill_dir / "agents"
    if agents_dir.is_dir():
        for yml in sorted(agents_dir.glob("*.y*ml")):
            try:
                yaml.safe_load(yml.read_text(encoding="utf-8"))
            except yaml.YAMLError as exc:
                errors.append(f"{name}: invalid YAML in agents/{yml.name}: {exc}")

    return errors


def main() -> int:
    if not SKILLS_DIR.is_dir():
        print("ERROR: skills/ directory not found")
        return 1

    skills = sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir())
    if not skills:
        print("ERROR: no skills found under skills/")
        return 1

    all_errors: list[str] = []
    for skill in skills:
        all_errors.extend(check_skill(skill))
        print(f"checked: {skill.name}")

    if all_errors:
        print()
        for err in all_errors:
            print(f"ERROR: {err}")
        return 1

    print("\nAll skills valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
