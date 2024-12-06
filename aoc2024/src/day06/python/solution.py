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

type Position = tuple[int, int]
type Direction = tuple[int, int]

_OBSTACLE_SYMBOL = '#'
_GUARD_SYMBOL = '^'


class World:
  def __init__(self, world_map: Sequence[str], add_obstacle: Position = None):
    """Assumes guard always starts looking up (y negative axis).
    Args:
      world_map: grid. '.' means empty space and '#' means obstacle.
      add_obstacle: (Optional) Position to add an obstacle to.
    """
    self.visited_pos: set[Position] = set()
    self._path: set[tuple[Position, Direction]] = set()
    if add_obstacle is None:
      self._world_map = world_map
    else:
      # Insert obstacle into world map.
      world_map_copy = list(world_map)
      line = world_map_copy[add_obstacle[0]]
      line_with_obstacle = line[:add_obstacle[1]] + _OBSTACLE_SYMBOL + line[add_obstacle[1] + 1:]
      world_map_copy[add_obstacle[0]] = line_with_obstacle
      self._world_map = tuple(world_map_copy)
    self.start_guard_pos: Position = self._find_guard_pos()
    self._guard_pos: Position = self.start_guard_pos
    self._guard_dir: Direction = (-1, 0)  # Up.
    self.visited_pos.add(self._guard_pos)

  def move(self) -> bool:
    """Moves the guard and returns false when out of world map."""
    next_pos = (self._guard_pos[0] + self._guard_dir[0], self._guard_pos[1] + self._guard_dir[1])
    if not self._is_pos_valid(next_pos):
      return False
    if self._world_map[next_pos[0]][next_pos[1]] == _OBSTACLE_SYMBOL:
      self._turn_right()
    else:
      self._guard_pos = next_pos
      self.visited_pos.add(self._guard_pos)
    return True

  def is_stuck_in_loop(self) -> bool:
    """Returns true if the guard moves in an infinite loop."""
    while True:
      before_moving_state = (self._guard_pos, self._guard_dir)
      if before_moving_state in self._path:
        return True  # Guard is looping
      moved = self.move()
      if moved:
        self._path.add(before_moving_state)
      else:
        return False  # Guard exited the map.

  def _find_guard_pos(self) -> Position:
    """Finds the starting guard position in the map."""
    for y in range(len(self._world_map)):
      for x in range(len(self._world_map[0])):
        if self._world_map[y][x] == _GUARD_SYMBOL:
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

  def _is_pos_valid(self, pos: Position):
    """Returns true if a position is within map bounds."""
    return (0 <= pos[0] < len(self._world_map)
            and 0 <= pos[1] < len(self._world_map[0]))


def _move_until_exit(world: World) -> set[Position]:
  """Moves guard until it exits the map."""
  while True:
    if not world.move():
      return world.visited_pos


def count_distinct_positions(world_map: Sequence[str]) -> int:
  """Moves the guard until it exits the map.
  A guard only moves forward. When facing an obstacle, it turns right.
  Returns the positions the guard has been to."""
  world = World(world_map)
  visited_positions = _move_until_exit(world)
  return len(visited_positions)


def count_positions_with_loop(world_map: Sequence[str]) -> int:
  """Returns the number of positions that cause the guard
  to get stuck in a loop if an obstacle was placed on it."""
  world = World(world_map)
  visited_positions = _move_until_exit(world)
  visited_positions.remove(world.start_guard_pos)  # Guard will notice obstacle, skip.
  # Try adding an obstacle on each of the positions leading to the exit.
  return sum(1 if World(world_map, add_obstacle=pos).is_stuck_in_loop() else 0
             for pos in visited_positions)
