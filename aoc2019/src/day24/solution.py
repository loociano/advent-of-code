# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from aoc2019.src.common.file_utils import read_lines


def count_adj_bugs(grid: list, line: int, col: int) -> int:
    count = 0
    size = len(grid)
    for dxy in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
        x = col + dxy[0]
        y = line + dxy[1]
        if 0 <= x < size and 0 <= y < size:
            count += 1 if grid[y][x] == '#' else 0
    return count


def serialize_state(grid: list) -> str:
    res = []
    for line in grid:
        res.append(''.join(line))
    return ''.join(res)


def simulate(grid: list) -> list:
    size = len(grid)
    new_grid = []
    for y in range(size):
        new_grid.append(['.'] * size)
        for x in range(size):
            if grid[y][x] == '#':  # bug
                if count_adj_bugs(grid, y, x) == 1:
                    new_grid[y][x] = '#'  # lives
            else:  # empty space
                adj_bugs = count_adj_bugs(grid, y, x)
                if adj_bugs == 1 or adj_bugs == 2:
                    new_grid[y][x] = '#'  # infested
    return new_grid


def calc_biodiversity_rating(serial_state: str) -> int:
    biodiversity_rating = 0
    for i, val in enumerate(list(serial_state)):
        if val == '#':
            biodiversity_rating += 2 ** i
    return biodiversity_rating


def part_one(filename: str) -> int:
    grid = []
    for line in read_lines(filename):
        grid.append(list(line))

    states = set()
    states.add(serialize_state(grid))
    while True:
        grid = simulate(grid)
        state = serialize_state(grid)
        if state in states:
            return calc_biodiversity_rating(state)
        states.add(state)
