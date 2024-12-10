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
from typing import Sequence

type Pos = tuple[int, int]

_TRAILHEAD = 0
_SUMMIT = 9
_IS_GRADUAL_SLOPE = lambda level, next_level: next_level == level + 1


def _find_trailheads(topographic_map: Sequence[str]) -> tuple[Pos, ...]:
  """Finds the positions of trailheads. A trailhead is represented by '0'."""
  trailhead_positions = []
  for y in range(len(topographic_map)):
    for x in range(len(topographic_map[0])):
      if int(topographic_map[y][x]) == _TRAILHEAD:
        trailhead_positions.append((y, x))
  return tuple(trailhead_positions)


def _count_reachable_summits(topo_map: Sequence[str], curr_pos: Pos, visited: set[Pos], num_summits: list[int]):
  curr_level = int(topo_map[curr_pos[0]][curr_pos[1]])
  if curr_level == _SUMMIT and curr_pos not in visited:
    num_summits[0] += 1
    visited.add(curr_pos)
    return
  visited.add(curr_pos)
  for step in ((-1, 0), (0, 1), (1, 0), (0, -1)):
    next_pos = (curr_pos[0] + step[0]), (curr_pos[1] + step[1])
    within_map = 0 <= next_pos[0] < len(topo_map) and 0 <= next_pos[1] < len(topo_map[0])
    if next_pos not in visited and within_map:
      next_level = int(topo_map[next_pos[0]][next_pos[1]])
      if _IS_GRADUAL_SLOPE(curr_level, next_level):
        _count_reachable_summits(topo_map, next_pos, visited, num_summits)


def get_score_sum(topographic_map: Sequence[str]) -> int:
  """Gets the sum of all the trails from all the trailheads."""
  sum_scores = 0
  trailheads_positions: tuple[Pos, ...] = _find_trailheads(topographic_map)
  for trailhead_pos in trailheads_positions:
    num_summits = [0]  # Pass by reference.
    _count_reachable_summits(topographic_map, trailhead_pos, set(), num_summits)
    sum_scores += num_summits[0]
  return sum_scores
