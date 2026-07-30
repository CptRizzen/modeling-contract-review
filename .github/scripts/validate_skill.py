#!/usr/bin/env python3
"""Validate skill.md against the Agent Skills frontmatter rules.

Run:  python3 .github/scripts/validate_skill.py
Self-test:  python3 .github/scripts/validate_skill.py --self-test
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
MAX_DESCRIPTION = 1024


def parse_frontmatter(text):
    """Return the top-level key/value pairs of a leading --- fenced block."""
    if not text.startswith("---\n"):
        raise ValueError("skill.md must start with a '---' frontmatter block")
    end = text.find("\n---", 3)
    if end == -1:
        raise ValueError("frontmatter block is never closed with '---'")
    fields = {}
    for line in text[4:end].splitlines():
        if not line.strip() or line.startswith("#") or line.startswith(" "):
            continue
        key, sep, value = line.partition(":")
        if sep:
            fields[key.strip()] = value.strip().strip("\"'")
    return fields


def check(text, changelog):
    """Return a list of problems. Empty list means valid."""
    problems = []
    fm = parse_frontmatter(text)

    for key in ("name", "description", "version"):
        if not fm.get(key):
            problems.append(f"frontmatter is missing required key: {key}")

    name = fm.get("name", "")
    if name and not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name):
        problems.append(f"name must be lowercase-kebab-case, got: {name!r}")

    description = fm.get("description", "")
    if len(description) > MAX_DESCRIPTION:
        problems.append(
            f"description is {len(description)} chars, max is {MAX_DESCRIPTION}"
        )

    version = fm.get("version", "")
    if version and not re.fullmatch(r"\d+\.\d+\.\d+", version):
        problems.append(f"version must be semver (x.y.z), got: {version!r}")
    elif version and f"[{version}]" not in changelog:
        problems.append(f"CHANGELOG.md has no entry for version {version}")

    return problems


def self_test():
    good = (
        "---\nname: modeling-contract-review\ndescription: Does a thing.\n"
        "version: 3.2.0\n---\n\n# Body\n"
    )
    log = "## [3.2.0] - 2026-06-06"
    assert check(good, log) == []
    assert check(good.replace("3.2.0", "3.9.9", 1), log), "stale version not caught"
    assert check(good.replace("version: 3.2.0", "version: v3"), log)
    assert check(good.replace("modeling-contract-review", "Modeling_Review"), log)
    assert check(good.replace("description: Does a thing.\n", ""), log)
    assert check(good.replace("description: Does a thing.", "description: " + "x" * 2000), log)
    try:
        check("# no frontmatter", log)
    except ValueError:
        pass
    else:
        raise AssertionError("missing frontmatter not caught")
    print("self-test OK")


def main():
    if "--self-test" in sys.argv:
        return self_test()
    problems = check(
        (ROOT / "skill.md").read_text(encoding="utf-8"),
        (ROOT / "CHANGELOG.md").read_text(encoding="utf-8"),
    )
    for problem in problems:
        print(f"::error file=skill.md::{problem}")
    if problems:
        sys.exit(1)
    print("skill.md frontmatter OK")


if __name__ == "__main__":
    main()
