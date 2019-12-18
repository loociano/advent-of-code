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


def get_grid(lines: list) -> list:
    return [list(line) for line in lines]


def get_doors(grid: list) -> dict:
    doors = {}
    for y in range(0, len(grid)):
        for x in range(0, len(grid[y])):
            if is_door(grid, x, y):
                doors[grid[y][x]] = (x, y)
    return doors


def get_start(grid: list) -> tuple:
    for y in range(0, len(grid)):
        for x in range(0, len(grid[y])):
            if is_entrance(grid, x, y):
                return x, y


def in_bounds(grid: list, x: int, y: int) -> bool:
    if x < 0 or x > len(grid[0]) - 1 or y < 0 or y > len(grid) - 1:
        return False
    return grid[y][x] != '#'


def is_door(grid: list, x: int, y: int) -> bool:
    return grid[y][x].isupper()


def is_key(grid: list, x: int, y: int) -> bool:
    return grid[y][x].islower()


def is_entrance(grid: list, x: int, y: int) -> bool:
    return grid[y][x] == '@'


def build_graph(grid, doors, start_x, start_y):
    graph = {}
    last_e = '@'
    dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    q = [(start_x, start_y, 0)]
    visited = set()
    while len(q) > 0:
        q_size = len(q)
        while q_size > 0:
            x, y, steps = q.pop(0)
            if is_door(grid, x, y):
                continue
            if is_key(grid, x, y):
                doorkey = grid[y][x]
                if graph.get(last_e) is None:
                    graph[last_e] = []
                graph[last_e].append((doorkey, steps))
                if doors.get(doorkey.upper()) is None:
                    return graph  # last key
                door_x, door_y = doors[doorkey.upper()]
                grid[door_y][door_x] = '.'  # open door
                grid[y][x] = '@'  # move
                last_e = doorkey
                visited = set()

            visited.add((x, y))
            grid[y][x] = '.'
            for dir in dirs:
                new_pos = (x + dir[0], y + dir[1])
                if in_bounds(grid, x + dir[0], y + dir[1]) and not is_door(grid, x, y) and new_pos not in visited:
                    q.append((x + dir[0], y + dir[1], steps + 1))
            q_size -= 1
    return graph


def bsf_min_steps(graph: dict) -> int:
    min_steps = sys.maxsize
    q = [('@', 0)]
    while len(q) > 0:
        node, steps = q.pop(0)
        if graph.get(node) is None:  # leaf
            min_steps = min(min_steps, steps)
        else:
            for neighbour in graph[node]:
                q.append(neighbour)
    return min_steps


def part_one(filename: str) -> int:
    grid = get_grid(read_file(filename))
    doors = get_doors(grid)
    x, y = get_start(grid)
    graph = build_graph(grid, doors, x, y)
    return bsf_min_steps(graph)
