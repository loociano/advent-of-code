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


import math


def _get_asteroid_grid(filename: str) -> list:
    asteroid_grid = []
    with open(filename) as f:
        for line in f.readlines():
            asteroid_grid.append([x for x in line.rstrip()])
    return asteroid_grid


def _find_asteroid_pos(asteroid_map: list, width: int, height: int, x: int, y: int, dx: int, dy: int) -> tuple or None:
    pos_x = x + dx
    pos_y = y + dy
    while width > pos_x >= 0 and height > pos_y >= 0:
        if asteroid_map[pos_y][pos_x] == '#':
            return tuple([pos_x, pos_y])
        pos_x += dx
        pos_y += dy
    return None


def _normalize(x: int, y: int) -> tuple:
    gcd = math.gcd(x, y)
    return tuple([x // gcd, y // gcd])


def _cmp_vector_angle(vector: tuple) -> float:
    hyp = math.sqrt(vector[0] * vector[0] + vector[1] * vector[1])
    return math.asin(vector[1] / hyp)


def _calc_quadrant_vectors(range_x: range, range_y: range, is_x_negative: bool):
    dirs = set()
    for w in range_x:
        for h in range_y:
            if w == 0 and h == 0:
                continue
            dirs.add(_normalize(w, h))
    return sorted(dirs, key=_cmp_vector_angle, reverse=is_x_negative)


def _calc_vectors(width: int, height: int):
    sorted_dirs = []
    # Clockwise order: quadrant 1, 4, 3 and 2
    range_x = [range(0, width), range(0, width), range(-width, 0), range(-width, 0)]
    range_y = [range(-height, 0), range(0, height), range(0, height), range(-height, 0)]
    is_x_negative = [False, False, True, True]
    for quadrant in range(0, 4):
        sorted_dirs.extend(_calc_quadrant_vectors(range_x[quadrant], range_y[quadrant], is_x_negative[quadrant]))
    return sorted_dirs


def _get_monitoring_station_position(asteroid_grid: list):
    best_position = tuple([0, 0])
    max_asteroids = 0
    width, height = len(asteroid_grid[0]), len(asteroid_grid)
    vectors = _calc_vectors(width, height)
    for y in range(0, height):
        for x in range(0, width):
            if asteroid_grid[y][x] == '#':
                count_asteroids = 0
                for vector in vectors:
                    pos = _find_asteroid_pos(asteroid_grid, width, height, x, y, vector[0], vector[1])
                    if pos is not None:
                        count_asteroids += 1
                if count_asteroids > max_asteroids:
                    max_asteroids = count_asteroids
                    best_position = tuple([x, y])
    return max_asteroids, best_position


def part_one(filename: str) -> int:
    return _get_monitoring_station_position(_get_asteroid_grid(filename))[0]


def part_two(filename: str, vaporized_target: int) -> int:
    asteroid_grid = _get_asteroid_grid(filename)
    width, height = len(asteroid_grid[0]), len(asteroid_grid)
    vectors = _calc_vectors(width, height)
    max_asteroids, station_pos = _get_monitoring_station_position(asteroid_grid)
    vaporized_count = 0
    while vaporized_count < vaporized_target:
        for vector in vectors:
            asteroid_pos = _find_asteroid_pos(asteroid_grid, width, height,
                                              station_pos[0], station_pos[1], vector[0], vector[1])
            if asteroid_pos is not None:
                asteroid_grid[asteroid_pos[1]][asteroid_pos[0]] = '.'  # vaporized
                vaporized_count += 1
                if vaporized_count == vaporized_target:
                    return asteroid_pos[0] * 100 + asteroid_pos[1]


print(part_one('input'))  # 276
print(part_two('input', 200))  # 1321
