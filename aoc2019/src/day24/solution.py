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
from aoc2019.src.common.file_utils import read_map


def count_row_bugs(grid: list, row: int) -> int:
    return ''.join(grid[row]).count('#')


def count_col_bugs(grid: list, col: int) -> int:
    return sum([1 if row[col] == '#' else 0 for row in grid])


def count_adj_bugs(grids: dict, level: int, line: int, col: int, recursive=False) -> int:
    count = 0
    grid = grids[level]
    size = len(grid)
    if recursive and (grids.get(level + 1) is None or grids.get(level - 1) is None):
        return 0

    for dxy in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
        x = col + dxy[0]
        y = line + dxy[1]
        if 0 <= x < size and 0 <= y < size:
            if recursive and x == 2 and y == 2:
                if line == 1 and col == 2:  # top
                    count += count_row_bugs(grids[level + 1], 0)
                elif line == 2 and col == 3:  # right
                    count += count_col_bugs(grids[level + 1], size - 1)
                elif line == 3 and col == 2:  # bottom
                    count += count_row_bugs(grids[level + 1], size - 1)
                elif line == 2 and col == 1:
                    count += count_col_bugs(grids[level + 1], 0)
            else:
                count += 1 if grid[y][x] == '#' else 0
        elif recursive:
            if (x < 0 and grids[level - 1][2][1] == '#') or (x >= size and grids[level - 1][2][3] == '#') \
                    or (y < 0 and grids[level - 1][1][2] == '#') or (y >= size and grids[level - 1][3][2] == '#'):
                count += 1
    return count


def serialize_state(grid: list) -> str:
    res = []
    for line in grid:
        res.append(''.join(line))
    return ''.join(res)


def get_empty_grid(size: int) -> list:
    grid = []
    for i in range(size):
        grid.append(['.'] * size)
    return grid


def has_life(grids: dict, level: int, x: int, y: int, recursive=False) -> bool:
    adj_bugs = count_adj_bugs(grids, level, y, x, recursive)
    return (grids[level][y][x] == '#' and adj_bugs == 1) \
           or (grids[level][y][x] == '.' and (adj_bugs == 1 or adj_bugs == 2))


def simulate(grids: dict, recursive=False) -> dict:
    new_grids = {}
    for level, grid in grids.items():
        size = len(grid)
        new_grid = get_empty_grid(size)
        for y in range(size):
            for x in range(size):
                if recursive and x == 2 and y == 2:
                    continue
                if has_life(grids, level, x, y, recursive):
                    new_grid[y][x] = '#'
        new_grids[level] = new_grid
    return new_grids


def calc_biodiversity_rating(serial_state: str) -> int:
    biodiversity_rating = 0
    for i, val in enumerate(list(serial_state)):
        if val == '#':
            biodiversity_rating += 2 ** i
    return biodiversity_rating


def part_one(filename: str) -> int:
    grid = read_map(filename)
    grids = {0: grid}
    states = {serialize_state(grid)}
    while True:
        grids = simulate(grids)
        state = serialize_state(grids[0])
        if state in states:
            return calc_biodiversity_rating(state)
        states.add(state)


def count_bugs(grids: dict) -> int:
    return sum([serialize_state(grid).count('#') for grid in grids.values()])


def part_two(filename: str, minutes: int) -> int:
    grid = read_map(filename)
    size = len(grid)
    grids = {0: grid}
    for m in range(1, minutes):
        grids[m] = get_empty_grid(size)
        grids[-m] = get_empty_grid(size)
    for m in range(minutes):
        grids = simulate(grids, True)
    return count_bugs(grids)
