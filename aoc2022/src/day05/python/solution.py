# Copyright 2022 Google LLC
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

from collections import deque
from typing import Sequence, Tuple

_CRATE_LENGTH = 3


def _parse_stacks(drawing: Sequence[str]) -> Sequence[deque]:
  stacks = []
  bottom_crates = drawing[-2]
  for i in range(0, len(bottom_crates), _CRATE_LENGTH + 1):
    stack = deque()
    stack.append(bottom_crates[i + 1])
    stacks.append(stack)
  # Bottom to top, skip stack numbers and bottom line.
  line_num = len(drawing) - 3
  while line_num >= 0:
    line = drawing[line_num]
    for i in range(0, len(line), _CRATE_LENGTH + 1):
      if line[i] == '[':  # There is a crate.
        stack_num = int(i / (_CRATE_LENGTH + 1))
        stacks[stack_num].append(line[i + 1])
    line_num -= 1
  return tuple(stacks)


def _execute_procedure(procedure: Sequence[str], stacks: Sequence[deque],
                       keep_order: bool = False) -> None:
  """Executes procedure on stacks in-place."""
  for instruction in procedure:
    # move 1 from 2 to 1
    match = re.search(r'move (\d+) from (\d+) to (\d+)', instruction)
    if match is None:
      raise ValueError('Wrong instruction [%s]', instruction)
    crate_amount = int(match.group(1))
    origin = int(match.group(2)) - 1
    dest = int(match.group(3)) - 1
    if keep_order:
      temp_stack = deque()
      for _ in range(crate_amount):
        if len(stacks[origin]) == 0:
          raise ValueError(f'Stack {origin + 1} is empty, cannot move.')
        temp_stack.append(stacks[origin].pop())
      while len(temp_stack):
        stacks[dest].append(temp_stack.pop())
    else:
      for _ in range(crate_amount):
        if len(stacks[origin]) == 0:
          raise ValueError(f'Stack {origin + 1} is empty, cannot move.')
        stacks[dest].append(stacks[origin].pop())


def _read_message(stacks: Sequence[deque]) -> str:
  return ''.join([stack[-1] if len(stack) else '' for stack in stacks])


def read_message_at_top(drawing_with_procedure: Sequence[str],
                        keep_order: bool = False) -> str:
  """Reads message at the top of the crates after executing a procedure.

  The message consist of the concatenated characters at the top of the piles.

  Args
    drawing_with_procedure: a drawing of initial state and desired move
      instructions.
    keep_order: whether to keep stack order when moving crates.
  Returns
    The message.
  """
  separator_line_index = drawing_with_procedure.index('')
  drawing = drawing_with_procedure[:separator_line_index]
  procedure = drawing_with_procedure[separator_line_index + 1:]
  stacks = _parse_stacks(drawing)
  _execute_procedure(procedure, stacks, keep_order)
  return _read_message(stacks)
