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


def _parse_stacks(drawing: str) -> Tuple[deque]:
  lines = drawing.split('\n')
  stacks = []
  bottom_crates = lines[-2]
  for i in range(0, len(bottom_crates), _CRATE_LENGTH + 1):
    stack = deque()
    stack.append(bottom_crates[i + 1])
    stacks.append(stack)
  # Bottom to top, skip stack numbers and bottom line.
  line_num = len(lines) - 3
  while line_num >= 0:
    line = lines[line_num]
    for i in range(0, len(line), _CRATE_LENGTH + 1):
      if line[i] == '[':  # There is a crate.
        stack_num = int(i / (_CRATE_LENGTH + 1))
        stacks[stack_num].append(line[i + 1])
    line_num -= 1
  return tuple(stacks)


def _execute_procedure(procedure: Sequence[str], stacks: Tuple[deque]) -> None:
  """Executes procedure on stacks in-place."""
  for instruction in procedure:
    # move 1 from 2 to 1
    match = re.search(r'move (\d+) from (\d+) to (\d+)', instruction)
    if match is None:
      raise ValueError('Wrong instruction [%s]', instruction)
    crate_amount = int(match.group(1))
    origin = int(match.group(2)) - 1
    dest = int(match.group(3)) - 1
    for _ in range(crate_amount):
      if len(stacks[origin]) == 0:
        raise ValueError(f'Stack {origin + 1} is empty, cannot move.')
      crate = stacks[origin].pop()
      stacks[dest].append(crate)


def _read_message(stacks: Tuple[deque]) -> str:
  return ''.join([stack[-1] if len(stack) else '' for stack in stacks])


def read_message_at_top(drawing_with_procedure: str) -> str:
  drawing, procedure = drawing_with_procedure.split('\n\n')
  stacks = _parse_stacks(drawing)
  _execute_procedure(procedure.split('\n'), stacks)
  return _read_message(stacks)
