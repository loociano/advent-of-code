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
import math
from typing import Sequence

type Vector = tuple[int, int]
type Machine = tuple[Vector, ...]
_BUTTON_A_COST = 3  # Tokens
_BUTTON_B_COST = 1  # Token
# Buttons will not be pressed more than 100 times.
_MAX_BUTTON_PRESSES = 100


def _parse(input: Sequence[str]) -> tuple[Machine, ...]:
  part = 0
  machines = []
  machine = []
  for i in range(len(input)):
    if part == 0 and input[i] != '':
      a_matches = re.match(r'Button A: X\+(\d+), Y\+(\d+)', input[i])
      machine.append((int(a_matches[1]), int(a_matches[2])))
      part = 1
    elif part == 1:
      b_matches = re.match(r'Button B: X\+(\d+), Y\+(\d+)', input[i])
      machine.append((int(b_matches[1]), int(b_matches[2])))
      part = 2
    elif part == 2:
      price_matches = re.match(r'Prize: X=(\d+), Y=(\d+)', input[i])
      machine.append((int(price_matches[1]), int(price_matches[2])))
      machines.append(tuple(machine))
      machine = []
      part = 0
  return tuple(machines)


def _calc_tokens(vector_0: Vector, vector_1: Vector, vector_2: Vector) -> int | None:
  b = (vector_2[1] - vector_2[0] * vector_0[1] / vector_0[0]) / (vector_1[1] - vector_1[0] * vector_0[1] / vector_0[0])
  a = (vector_2[0] - b * vector_1[0]) / vector_0[0]
  a, b = round(a, 2), round(b, 2)
  if a.is_integer() and b.is_integer():
    return int(a) * _BUTTON_A_COST + int(b) * _BUTTON_B_COST
  return None


def min_tokens_to_win(input: Sequence[str], price_offset: int = 0) -> int | None:
  def add_price_offset(machine: Machine) -> Machine:
    """Adds a given offset to price position."""
    new_price_vector = (machine[2][0] + price_offset, machine[2][1] + price_offset)
    return machine[0], machine[1], new_price_vector

  claw_machines = _parse(input)
  if price_offset > 0:
    claw_machines = tuple(map(add_price_offset, claw_machines))
  num_tokens = 0
  for machine in claw_machines:
    tokens = _calc_tokens(machine[0], machine[1], machine[2])
    if tokens is not None:
      num_tokens += tokens
  return num_tokens if num_tokens > 0 else None
