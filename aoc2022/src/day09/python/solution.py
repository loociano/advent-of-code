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


def _is_tail_touching_head(head_pos: List[int], tail_pos: List[int]) -> bool:
  if head_pos[0] == tail_pos[0] and head_pos[1] == tail_pos[1]:
    return True  # Overlap.
  if head_pos[0] == tail_pos[0] and abs(head_pos[1] - tail_pos[1]) == 1:
    return True  # Same column.
  if head_pos[1] == tail_pos[1] and abs(head_pos[0] - tail_pos[0]) == 1:
    return True  # Same row.
  if (abs(head_pos[0] - tail_pos[0]) == 1 and abs(
      head_pos[1] - tail_pos[1]) == 1):
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


def _move_tail(head_pos: List[int], tail_pos: List[int]) -> List[int]:
  if head_pos[0] == tail_pos[0]:  # Same column?
    if head_pos[1] > tail_pos[1]:
      tail_pos[1] += 1
    else:
      tail_pos[1] -= 1
    return tail_pos
  elif head_pos[1] == tail_pos[1]:  # Same row?
    if head_pos[0] > tail_pos[0]:
      tail_pos[0] += 1
    else:
      tail_pos[0] -= 1
    return tail_pos
  else:  # Diagonal.
    right_up = [tail_pos[0] + 1, tail_pos[1] - 1]
    right_down = [tail_pos[0] + 1, tail_pos[1] + 1]
    left_up = [tail_pos[0] - 1, tail_pos[1] - 1]
    left_down = [tail_pos[0] - 1, tail_pos[1] + 1]
    if _is_tail_touching_head(head_pos, right_up):
      return right_up
    elif _is_tail_touching_head(head_pos, right_down):
      return right_down
    elif _is_tail_touching_head(head_pos, left_up):
      return left_up
    elif _is_tail_touching_head(head_pos, left_down):
      return left_down
    else:
      raise ValueError('Cannot find tail move to touch head!')


def count_tail_visited_positions(motions: Sequence[str]) -> int:
  tail_visited_pos = set()
  head_pos = [0, 0]
  tail_pos = [0, 0]
  for motion in motions:
    direction, steps = motion.split()
    for _ in range(int(steps)):
      _update_head(direction, head_pos)
      if not _is_tail_touching_head(head_pos, tail_pos):
        tail_pos = _move_tail(head_pos, tail_pos)
      tail_visited_pos.add(tuple(tail_pos))
  return len(tail_visited_pos)
