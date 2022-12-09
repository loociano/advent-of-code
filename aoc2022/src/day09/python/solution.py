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
from typing import List, Sequence, Tuple


def _is_touching(prev_knot_pos: List[int], knot_pos: List[int]) -> bool:
  if prev_knot_pos[0] == knot_pos[0] and prev_knot_pos[1] == knot_pos[1]:
    return True  # Overlap.
  if prev_knot_pos[0] == knot_pos[0] and abs(
      prev_knot_pos[1] - knot_pos[1]) == 1:
    return True  # Same column.
  if prev_knot_pos[1] == knot_pos[1] and abs(
      prev_knot_pos[0] - knot_pos[0]) == 1:
    return True  # Same row.
  if (abs(prev_knot_pos[0] - knot_pos[0]) == 1 and abs(
      prev_knot_pos[1] - knot_pos[1]) == 1):
    return True  # Diagonal
  return False


def _update_head(direction: str, head_pos: List[int]) -> None:
  if direction == 'R':
    head_pos[0] += 1
  elif direction == 'L':
    head_pos[0] -= 1
  elif direction == 'U':
    head_pos[1] -= 1
  elif direction == 'D':
    head_pos[1] += 1
  else:
    raise ValueError('Unknown direction %s', direction)


def _move_knot(prev_knot_pos: List[int], knot_pos: List[int]) -> List[int]:
  if prev_knot_pos[0] == knot_pos[0]:  # Same column?
    if prev_knot_pos[1] > knot_pos[1]:
      knot_pos[1] += 1
    else:
      knot_pos[1] -= 1
    return knot_pos
  elif prev_knot_pos[1] == knot_pos[1]:  # Same row?
    if prev_knot_pos[0] > knot_pos[0]:
      knot_pos[0] += 1
    else:
      knot_pos[0] -= 1
    return knot_pos
  else:  # Diagonal.
    right_up = [knot_pos[0] + 1, knot_pos[1] - 1]
    right_down = [knot_pos[0] + 1, knot_pos[1] + 1]
    left_up = [knot_pos[0] - 1, knot_pos[1] - 1]
    left_down = [knot_pos[0] - 1, knot_pos[1] + 1]
    if _is_touching(prev_knot_pos, right_up):
      return right_up
    elif _is_touching(prev_knot_pos, right_down):
      return right_down
    elif _is_touching(prev_knot_pos, left_up):
      return left_up
    elif _is_touching(prev_knot_pos, left_down):
      return left_down
    else:
      raise ValueError('Cannot find tail move to touch head!')


def count_tail_visited_positions(motions: Sequence[str], knots: int = 2) -> int:
  tail_visited_pos = set()
  positions = [[0, 0] for _ in range(knots)]
  for motion in motions:
    direction, steps = motion.split()
    for _ in range(int(steps)):
      for count, knot_pos in enumerate(positions):
        if count == 0:  # Head.
          _update_head(direction, knot_pos)
        else:  # Rest of knots.
          prev_knot_pos = positions[count - 1]
          if not _is_touching(prev_knot_pos, knot_pos):
            positions[count] = _move_knot(prev_knot_pos, knot_pos)
          if count == len(positions) - 1:
            tail_visited_pos.add(tuple(positions[count]))
  return len(tail_visited_pos)
