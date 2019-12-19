# Copyright 2019 Google LLC
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
import sys
from aoc2019.src.common.utils import read_file


class TreeNode:

    def __init__(self, val, steps, keys):
        self.val = val
        self.keys = keys
        self.steps = steps
        self.visited = set()


def get_grid(lines: list) -> list:
    return [list(line) for line in lines]


def get_num_keys(grid: list) -> int:
    count = 0
    for y in range(0, len(grid)):
        for x in range(0, len(grid[y])):
            if is_key(grid, x, y):
                count += 1
    return count


def find_start(grid: list) -> tuple:
    for y in range(0, len(grid)):
        for x in range(0, len(grid[y])):
            if grid[y][x] == '@':
                return x, y


def is_in_bounds(grid: list, x: int, y: int) -> bool:
    if x < 0 or x > len(grid[0]) - 1 or y < 0 or y > len(grid) - 1:
        return False
    return grid[y][x] != '#'


def is_door(grid: list, x: int, y: int) -> bool:
    return grid[y][x].isupper()


def is_key(grid: list, x: int, y: int) -> bool:
    return grid[y][x].islower()


def min_steps_all_keys(grid: list, num_keys: int, start_x: int, start_y: int) -> int:
    dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    root = TreeNode('@', 0, set())
    q = [(start_x, start_y, 0, root)]
    while len(q) > 0:
        x, y, steps, root = q.pop(0)
        value = grid[y][x]
        root.visited.add((x, y))
        if is_door(grid, x, y) and value.lower() not in root.keys:
            continue
        if is_key(grid, x, y) and value not in root.keys:
            key = value
            node = TreeNode(key, steps, root.keys.copy())
            node.keys.add(key)
            root = node
            if len(node.keys) == num_keys:  # found last key
                return root.steps
        for dir in dirs:
            new_pos = (x + dir[0], y + dir[1])
            if is_in_bounds(grid, x + dir[0], y + dir[1]) and new_pos not in root.visited:
                q.append((x + dir[0], y + dir[1], steps + 1, root))
    return -1


def part_one(filename: str) -> int:
    grid = get_grid(read_file(filename))
    x, y = find_start(grid)
    return min_steps_all_keys(grid, get_num_keys(grid), x, y)
