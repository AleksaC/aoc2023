from __future__ import annotations

import argparse
import operator
import os.path
import re
from dataclasses import dataclass
from functools import reduce

INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")

CUBE_COUNT = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

GAME_ID_RE = re.compile(r"^Game (\d+):")


@dataclass
class Game:
    id: int
    results: list[dict[str, int]]


def parse_game(game: str) -> Game:
    game_id = int(re.match(GAME_ID_RE, game).group(1))
    _, sets = game.split(":")

    results = []
    for s in sets.split(";"):
        r = {}
        for i in s.split(","):
            num, color = i.strip().split(" ")
            r[color] = int(num)
        results.append(r)

    return Game(game_id, results)


def is_game_possible(game: Game) -> bool:
    for res in game.results:
        for color, num in res.items():
            if num > CUBE_COUNT[color]:
                return False
    return True


def get_min_cubes(game: Game):
    counts = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }

    for res in game.results:
        for color, num in res.items():
            if num > counts[color]:
                counts[color] = num

    return counts


def part_one(inp: str) -> int:
    res = 0

    for line in inp.splitlines():
        game = parse_game(line)
        if is_game_possible(game):
            res += game.id

    return res


def part_two(inp: str) -> int:
    res = 0

    for line in inp.splitlines():
        game = parse_game(line)
        res += reduce(operator.mul, get_min_cubes(game).values())

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
