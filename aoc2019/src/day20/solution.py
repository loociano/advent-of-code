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
from aoc2019.src.common.file_utils import read_map


def find_start(grid: list) -> (int, int):
    for y in range(0, len(grid)):
        for x in range(0, len(grid[y])):
            if grid[y][x] == grid[y + 1][x] == 'A':
                if y + 2 < len(grid) and grid[y + 2][x] == '.':
                    return x, y + 2
                else:
                    return x, y - 1


def find_portals(grid: list) -> (dict, dict):
    portals_key_pos = {}
    portals_key_name = {}
    width, height = len(grid[0]), len(grid)
    for y in range(0, height):
        for x in range(0, width):
            if portals_key_pos.get((x, y)) is not None:
                continue
            if grid[y][x].isupper():
                if y + 1 < height and grid[y + 1][x].isupper():
                    if y + 2 < height and grid[y + 2][x] == '.':  # down
                        portal = (grid[y][x], grid[y + 1][x])
                        pos = (x, y + 1)
                        portals_key_pos[pos] = portal
                        if portals_key_name.get(portal) is None:
                            portals_key_name[portal] = []
                        if y - 1 > 0 and grid[y - 1][x] == ' ':
                            portals_key_name[portal].insert(0, pos)  # inner portal first
                        else:
                            portals_key_name[portal].append(pos)
                    elif y - 1 > 0 and grid[y - 1][x] == '.':  # up
                        portal = (grid[y][x], grid[y + 1][x])
                        pos = (x, y)
                        portals_key_pos[pos] = portal
                        if portals_key_name.get(portal) is None:
                            portals_key_name[portal] = []
                        if y + 2 < height and grid[y + 2][x] == ' ':
                            portals_key_name[portal].insert(0, pos)
                        else:
                            portals_key_name[portal].append(pos)
                elif x + 1 < width and grid[y][x + 1].isupper():
                    if x + 2 < width and grid[y][x + 2] == '.':  # right
                        portal = (grid[y][x], grid[y][x + 1])
                        pos = (x + 1, y)
                        portals_key_pos[pos] = portal
                        if portals_key_name.get(portal) is None:
                            portals_key_name[portal] = []
                        if x - 1 > 0 and grid[y][x - 1] == ' ':
                            portals_key_name[portal].insert(0, pos)  # inner portal first
                        else:
                            portals_key_name[portal].append(pos)
                    elif x - 1 > 0 and grid[y][x - 1] == '.':  # left
                        portal = (grid[y][x], grid[y][x + 1])
                        pos = (x, y)
                        portals_key_pos[pos] = portal
                        if portals_key_name.get(portal) is None:
                            portals_key_name[portal] = []
                        if x + 2 < width and grid[y][x + 2] == ' ':
                            portals_key_name[portal].insert(0, pos)  # inner portal, goes level down
                        else:
                            portals_key_name[portal].append(pos)
    return portals_key_pos, portals_key_name


def warp_to(grid: list, x: int, y: int) -> (int, int):
    for dx_y in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        if grid[y + dx_y[1]][x + dx_y[0]] == '.':
            return x + dx_y[0], y + dx_y[1]


def within_bounds(grid: list, pos: (int, int)) -> bool:
    return 0 <= pos[0] < len(grid[0]) and 0 <= pos[1] < len(grid) and grid[pos[1]][pos[0]] != '#'


def bsf_min_steps(grid: list, portals_key_pos: dict, portals_key_name: dict, start: (int, int), recursive=False) -> int:
    q = [(start[0], start[1], 0)]
    visited = set()
    steps = -1
    while len(q) > 0:
        q_size = len(q)
        while q_size > 0:
            x, y, level = q.pop(0)
            q_size -= 1
            visited.add((x, y, level))
            portal = portals_key_pos.get((x, y))
            if portal is not None:
                if portal == ('A', 'A'):
                    continue
                if portal == ('Z', 'Z'):
                    if level == 0:
                        return steps
                    else:
                        continue
                coord_inner, coord_outer = portals_key_name.get(portal)
                if (x, y) == coord_inner:
                    if recursive:
                        level += 1
                    x, y = warp_to(grid, coord_outer[0], coord_outer[1])
                    visited.add((coord_outer[0], coord_outer[1], level))
                else:
                    if recursive:
                        if level == 0:  # outer portals are walls in level zero
                            continue
                        else:
                            level -= 1
                    x, y = warp_to(grid, coord_inner[0], coord_inner[1])
                    visited.add((coord_inner[0], coord_inner[1], level))
                visited.add((x, y, level))

            for dx_y in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                new_pos = (x + dx_y[0], y + dx_y[1], level)
                if within_bounds(grid, new_pos) and new_pos not in visited:
                    q.append((x + dx_y[0], y + dx_y[1], level))
        steps += 1
    return -1  # could not find ZZ portal


def part_one(filename: str) -> int:
    grid = read_map(filename)
    portals_key_pos, portals_key_name = find_portals(grid)
    return bsf_min_steps(grid, portals_key_pos, portals_key_name, find_start(grid))


def part_two(filename: str) -> int:
    grid = read_map(filename)
    portals_key_pos, portals_key_name = find_portals(grid)
    return bsf_min_steps(grid, portals_key_pos, portals_key_name, find_start(grid), True)
