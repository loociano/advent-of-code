# Copyright 2024 Google LLC
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
import re
from typing import Sequence
from collections import deque
from aoc2024.src.day17.python.computer import Computer


def _parse_input(program_info: Sequence[str]) -> tuple[int, int, int, Sequence[int]]:
  """Reads initial values of registers A,B,C and program from input."""
  reg_a_match = re.match(r'Register A: (\d+)', program_info[0])
  reg_b_match = re.match(r'Register B: (\d+)', program_info[1])
  reg_c_match = re.match(r'Register C: (\d+)', program_info[2])
  program_match = re.match(r'Program: (.*)', program_info[4])  # Blank line between registers and program.
  return int(reg_a_match[1]), int(reg_b_match[1]), int(reg_c_match[1]), tuple(map(int, program_match[1].split(',')))


def print_stdout(program_info: Sequence[str]) -> str:
  reg_a, reg_b, reg_c, program = _parse_input(program_info)
  computer = Computer(program=program, reg_a=reg_a, reg_b=reg_b, reg_c=reg_c)
  computer.execute()
  return computer.flush()


def find_reg_a_init_value(program_info: Sequence[str], brute_force: bool = False) -> int:
  """Finds the initial value of register A so that the output matches the program."""
  _, reg_b, reg_c, program = _parse_input(program_info)
  searching_match = ','.join(map(str, program))
  reg_a = 0
  if brute_force:
    while True:
      computer = Computer(program=program, reg_a=reg_a, reg_b=reg_b, reg_c=reg_c)
      computer.execute()
      stdout = computer.flush()
      if stdout == searching_match:
        return reg_a
      reg_a += 1
  else:
    # Super helpful comments:
    # https://www.reddit.com/r/adventofcode/comments/1hg38ah/comment/m2vn8nx/
    # https://www.reddit.com/r/adventofcode/comments/1hg38ah/comment/m2ovom3/
    queue = deque()
    queue.append((len(program), 0))  # unmatched_length, starting_reg_a_value.
    while queue:
      unmatched_length, reg_a = queue.popleft()
      for i in range(8):
        possible_reg_a = reg_a * 8 + i  # Try values that satisfy A % 8 = i.
        computer = Computer(program=program, reg_a=possible_reg_a, reg_b=reg_b, reg_c=reg_c)
        computer.execute()
        stdout = computer.stdout()
        if stdout == program[unmatched_length - 1:]:
          # Matching one more character from the right.
          queue.append((unmatched_length - 1, possible_reg_a))
          if stdout == program:
            return possible_reg_a
    raise ValueError('Could not find register A value!')
