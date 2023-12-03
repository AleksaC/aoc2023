from __future__ import annotations

import argparse
import os.path
from types import MappingProxyType

INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")

DIGITS = MappingProxyType(
    {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
)


def get_first_digit(s: str, digits=DIGITS) -> int:
    for i in range(len(s)):
        if s[i].isdigit():
            return int(s[i])

        si = s[i:]
        for d in digits:
            if si.startswith(d):
                return digits[d]


def part_one(inp: str) -> int:
    res = 0
    for line in inp.splitlines():
        n = 0
        for d in line:
            if d.isdigit():
                n = 10 * int(d)
                break
        for d in reversed(line):
            if d.isdigit():
                n += int(d)
                break
        res += n

    return res


def part_two(inp: str) -> int:
    res = 0
    for line in inp.splitlines():
        res += 10 * get_first_digit(line) + get_first_digit(
            line[::-1], {k[::-1]: v for k, v in DIGITS.items()}
        )

    return res


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", nargs="?", default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.input_file) as f:
        input_data = f.read()
        print(f"Part one: {part_one(input_data)}")
        print(f"Part two: {part_two(input_data)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
