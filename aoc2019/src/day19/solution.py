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
from aoc2019.src.common.intcode import Intcode
from aoc2019.src.common.utils import read_program


def gen_inputs_map(width: int, height: int) -> (list, list):
    inputs, grid = [], []
    for y in range(0, height):
        grid.append([0] * width)
        for x in range(0, width):
            inputs.append((x, y))
    return inputs, grid


def serialize_grid(grid: list, width: int, height: int):
    return '\n'.join([''.join(['#' if grid[y][x] == 1 else '.' for x in range(0, width)]) for y in range(0, height)])


def part_one(filename: str, width: int, height: int):
    points = 0
    program = read_program(filename)
    inputs, grid = gen_inputs_map(width, height)
    while len(inputs) > 0:
        x, y = inputs.pop(0)
        vm = Intcode(program)
        vm.set_input(x)
        vm.run_until_io_or_done()
        vm.set_input(y)
        vm.run_until_io_or_done()
        output = vm.run_until_io_or_done()
        grid[y][x] = output
        points += 1 if output == 1 else 0
    print(serialize_grid(grid, width, height))
    return points
