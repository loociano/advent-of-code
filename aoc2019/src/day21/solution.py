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


def get_hull_damage(vm: Intcode) -> (int, str):
    line = []
    while True:
        output = vm.run_until_io_or_done()
        if output > 127:  # ascii table size
            return output, ''
        if output is None:
            break
        line.append(chr(output))
    return -1, ''.join(line)


def send_instr(vm: Intcode, instrs: list):
    while len(instrs) > 0:
        ascii_int = instrs.pop(0)
        vm.set_input(ascii_int)
        vm.run_until_input_or_done()


def part_one(filename: str) -> int:
    vm = Intcode(read_program(filename))
    instrs = list(map(ord, list(
        'NOT A T\n'
        'NOT B J\n'
        'OR T J\n'
        'NOT C T\n'
        'OR T J\n'
        'AND D J\n'
        'WALK\n')))
    send_instr(vm, instrs)
    damage, ascii_images = get_hull_damage(vm)
    if ascii_images:
        print(ascii_images)
    return damage
