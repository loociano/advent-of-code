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
from math import ceil

from aoc2019.src.common.file_utils import read_intcode
from aoc2019.src.common.intcode import Intcode


def gen_inputs(x1: int, x2: int, y1: int, y2: int) -> list:
    inputs = []
    for y in range(y1, y2):
        for x in range(x1, x2):
            inputs.append((x, y))
    return inputs


def gen_grid(width: int, height: int) -> list:
    grid = []
    for y in range(0, height):
        grid.append(['.'] * width)
    return grid


def serialize_grid(grid: list, width: int, height: int):
    return '\n'.join([''.join([grid[y][x] for x in range(0, width)]) for y in range(0, height)])


def is_in_beam(program: list, x: int, y: int):
    vm = Intcode(program)
    vm.set_input(x)
    vm.run_until_io_or_done()
    vm.set_input(y)
    vm.run_until_io_or_done()
    return vm.run_until_io_or_done() == 1


def find_right_edge(program: list, x: int, y: int) -> int:
    while True:
        if is_in_beam(program, x, y):
            break
        x -= 1
    return x


def get_slope(program: list) -> float:
    y = 10000
    x_right_edge = find_right_edge(program, 10000, y)
    return y / x_right_edge


def get_area_points(program: list, grid: list, inputs: list):
    offset = inputs[0]
    points = 0
    while len(inputs) > 0:
        x, y = inputs.pop(0)
        if is_in_beam(program, x, y):
            grid[y - offset[1]][x - offset[0]] = '#'
            points += 1
    return points


def part_one(filename: str, width: int, height: int):
    program = read_intcode(filename)
    grid = gen_grid(width, height)
    inputs = gen_inputs(0, width, 0, height)
    points = get_area_points(program, grid, inputs)
    print(serialize_grid(grid, width, height))
    return points


def binary_search(program: list, slope: float) -> int:
    y_low = 0
    y_high = 10000
    while y_low < y_high:
        y_mid = (y_high + y_low) // 2
        x_mid = find_right_edge(program, y_mid, y_mid)  # search in square y_mid
        y_mid = ceil(x_mid * slope)
        if is_in_beam(program, x_mid - 99, y_mid + 99):
            y_high = y_mid
        else:
            y_low = y_mid + 1
    return find_right_edge(program, y_high, y_high)


def part_two(filename: str):
    program = read_intcode(filename)
    slope = get_slope(program)
    x = binary_search(program, slope)
    y = ceil(x * slope)
    return (x - 99) * 10000 + y
