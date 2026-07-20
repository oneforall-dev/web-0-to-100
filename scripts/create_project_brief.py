#!/usr/bin/env python3
"""Create project-brief.yaml from the bundled template without overwriting."""

from pathlib import Path
import argparse
import shutil
import sys


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("project_root", nargs="?", default=".")
    parser.add_argument("--name", default="project-brief.yaml")
    args = parser.parse_args()

    skill_root = Path(__file__).resolve().parent.parent
    source = skill_root / "assets" / "project-brief.template.yaml"
    destination = Path(args.project_root).resolve() / args.name

    if destination.exists():
        print(f"SKIP: {destination} ya existe", file=sys.stderr)
        return 2

    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, destination)
    print(destination)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

