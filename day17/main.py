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
from common.intcode import Intcode
from common.utils import read_program


def is_intersection(grid: dict, x: int, y: int, width: int, height: int) -> bool:
    if x == 0 or y == 0 or x == width - 1 or y == height - 1:
        return False
    return grid[(x - 1, y)] == 35 and grid[(x + 1, y)] == 35 \
        and grid[(x, y - 1)] == 35 and grid[(x, y + 1)] == 35


def get_alignment_param_sum(vm: Intcode) -> int:
    grid = {}
    x, y, width, height = 0, 0, 0, 0
    output = vm.run()
    while output is not None:
        if output == 10:  # newline
            y += 1
            width = max(width, x)
            x = 0
        else:
            grid[(x, y)] = output
            x += 1
        output = vm.run()
    height = y - 1  # input ends with newline

    alignment_param_sum = 0
    for y in range(0, height):
        for x in range(0, width):
            if grid[(x, y)] == 35 and is_intersection(grid, x, y, width, height):
                alignment_param_sum += x * y
    return alignment_param_sum


def part_one(filename: str) -> int:
    vm = Intcode(read_program(filename))
    return get_alignment_param_sum(vm)


print(part_one('input'))
