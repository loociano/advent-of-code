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


class World:
  def __init__(self, world_map: Sequence[str]):
    self._world_map = world_map
    self._visited_pos = set()
    # Assumption: guard always starts looking up (-y).
    self._guard_pos: tuple[int, int] = self._find_guard_pos()
    self._visited_pos.add(self._guard_pos)
    self._guard_dir: tuple[int, int] = (-1, 0)  # Up.

  def move(self) -> bool:
    """Moves the guard and returns false when out of world map."""
    next_pos = (self._guard_pos[0] + self._guard_dir[0], self._guard_pos[1] + self._guard_dir[1])
    if not self._is_pos_valid(next_pos):
      return False
    if self._world_map[next_pos[0]][next_pos[1]] == '#':  # Obstacle.
      self._turn_right()
    else:
      self._guard_pos = next_pos
      self._visited_pos.add(self._guard_pos)
    return True

  def get_visited_pos(self) -> int:
    """Returns the number of distinct positions the guard has been to."""
    return len(self._visited_pos)

  def _find_guard_pos(self) -> tuple[int, int]:
    """Finds the starting guard position in the map."""
    for y in range(len(self._world_map)):
      for x in range(len(self._world_map[0])):
        if self._world_map[y][x] == '^':
          return y, x
    raise ValueError('Guard not found!')

  def _turn_right(self):
    """Turns the guard's direction 90 degrees right."""
    self._guard_dir = {
      (-1, 0): (0, 1),  # Up -> Right
      (0, 1): (1, 0),  # Right -> Down
      (1, 0): (0, -1),  # Down -> Left
      (0, -1): (-1, 0)  # Left -> Up
    }.get(self._guard_dir)

  def _is_pos_valid(self, pos: tuple[int, int]):
    """Returns true if a position is within map bounds."""
    return (0 <= pos[0] < len(self._world_map)
            and 0 <= pos[1] < len(self._world_map[0]))


def count_distinct_positions(world_map: Sequence[str]) -> int:
  """Moves the guard until it exits the map.
  A guard only moves forward. When facing an obstacle, it turns right.
  Returns the positions the guard has been to."""
  world = World(world_map)
  while True:
    if not world.move():
      break
  return world.get_visited_pos()
