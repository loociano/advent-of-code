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


def run_springscript(vm: Intcode) -> (int, str):
    ascii_image = []
    while True:
        ascii_int = vm.run_until_io_or_done()
        if ascii_int is None:
            break
        if ascii_int > 127:  # ascii table size
            return ascii_int, ''
        ascii_image.append(chr(ascii_int))
    return -1, ''.join(ascii_image)


def send_instr(vm: Intcode, script: list):
    ascii_chars = list(map(ord, list(''.join(script))))
    while len(ascii_chars) > 0:
        ascii_int = ascii_chars.pop(0)
        vm.set_input(ascii_int)
        vm.run_until_input_or_done()


def get_hull_damage(vm: Intcode, script: list) -> int:
    send_instr(vm, script)
    damage, ascii_images = run_springscript(vm)
    if ascii_images:
        print(ascii_images)
    return damage


def part_one(filename: str) -> int:
    # (!A or !B or !C) and D
    script = [
        'NOT A T\n',
        'NOT B J\n',
        'OR T J\n',
        'NOT C T\n',
        'OR T J\n',
        'AND D J\n',
        'WALK\n']
    return get_hull_damage(Intcode(read_program(filename)), script)


def part_two(filename: str) -> int:
    script = [
        # (!A or !B or !C) and D and (E or H)
        # Inferred experimentally by inspecting the failed scenarios
        'NOT A T\n',
        'NOT B J\n',
        'OR T J\n',
        'NOT C T\n',
        'OR T J\n',
        'AND D J\n',
        'NOT E T\n',
        'NOT T T\n',
        'OR H T\n',
        'AND T J\n',
        'RUN\n']
    return get_hull_damage(Intcode(read_program(filename)), script)
