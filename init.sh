#! /bin/bash

if [ -z "$1" ]; then
    echo "Error: Date must be specified."
    echo "Usage: $0 <day>"
    exit 1
fi

if [[ -z "${AOC_SESSION}" ]] || ! aocd "$1" 2022 >/dev/null 2>&1; then
    echo "Error: AOC_SESSION not set or invalid"
    exit 1
fi

day=$(printf "%02d" "$1")

if ! command -v cookiecutter &>/dev/null; then
    pip install cookiecutter
fi

cookiecutter tools/cookiecutter/template --output-dir src --no-input day_number="${day}"

if ! command -v aocd &>/dev/null; then
    pip install advent-of-code-data
fi

aocd "${day}" 2025 >"src/day_${day}/inputs/input"
