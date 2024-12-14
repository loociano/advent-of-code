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
from collections import Counter

type Position = tuple[int, int]  # (x,y)
type Velocity = tuple[int, int]  # (dx,dy)
type WorldSize = tuple[int, int]  # (width, height)

_DEFAULT_SIZE: WorldSize = (101, 103)


class Robot:
  def __init__(self, position: Position, velocity: Velocity, world_size: WorldSize) -> None:
    self._x = position[0]
    self._y = position[1]
    self._dx = velocity[0]
    self._dy = velocity[1]
    self._width = world_size[0]
    self._height = world_size[1]

  def position(self) -> Position:
    return self._x, self._y

  def move(self) -> None:
    """Moves robot from its position according to its constant velocity."""
    self._x += self._dx
    if self._x > self._width - 1:
      self._x -= self._width  # Wrap around right edge.
    if self._x < 0:
      self._x = self._width + self._x  # Wrap around left edge.
    self._y += self._dy
    if self._y > self._height - 1:
      self._y -= self._height  # Wrap around bottom edge.
    if self._y < 0:
      self._y = self._height + self._y

  def get_quadrant(self) -> int:
    """Returns the quadrant where the robot is located.
    Quadrant can be 1, 2, 3, 4 or 0 if located between quadrants."""
    mid_x = self._width // 2
    mid_y = self._height // 2
    if 0 <= self._x < mid_x and 0 <= self._y < mid_y:
      return 1
    if mid_x < self._x < self._width and 0 <= self._y < mid_y:
      return 2
    if 0 <= self._x < mid_x and mid_y < self._y < self._height:
      return 3
    if mid_x < self._x < self._width and mid_y < self._y < self._height:
      return 4
    return 0  # At quadrant division.


def _parse(input: Sequence[str], world_size: WorldSize) -> tuple[Robot, ...]:
  """Parses the input. Each line represents a robot."""
  robots = []
  for line in input:
    matches = re.match(r'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)', line)
    if matches is None:
      raise ValueError(f'Cannot parse input line: {line}')
    position = int(matches[1]), int(matches[2])
    velocity = int(matches[3]), int(matches[4])
    robots.append(Robot(position, velocity, world_size))
  return tuple(robots)


def _simulate(robots: tuple[Robot, ...], elapsed_seconds):
  for _ in range(elapsed_seconds):
    for robot in robots:
      robot.move()


def _calc_safety_factor(robots: tuple[Robot, ...]) -> int:
  quadrant_counts = Counter(map(lambda r: r.get_quadrant(), robots))
  # Assumes there will be at least one robot per quadrant.
  return math.prod(quadrant_counts.get(quadrant_num) for quadrant_num in range(1, 5))


def get_safety_factor(input: Sequence[str], world_size: WorldSize = _DEFAULT_SIZE,
                      elapsed_seconds: int = 0) -> int:
  """Returns safety factor as the multiplication of robots per quadrant after a number of seconds.
  Robots that end up between quadrants do not count towards safety factor."""
  robots = _parse(input, world_size)
  _simulate(robots, elapsed_seconds)
  return _calc_safety_factor(robots)


def _print_world(robots: tuple[Robot, ...], world_size: WorldSize) -> None:
  counter = Counter(map(lambda r: r.position(), robots))
  for y in range(world_size[1]):
    line = []
    for x in range(world_size[0]):
      line.append('X' if counter.get((x, y)) is not None else '.')
    print(''.join(line))


def get_seconds_to_easter_egg(input: Sequence[str], world_size: WorldSize = _DEFAULT_SIZE,
                              elapsed_seconds: int = 0) -> int:
  """Returns number of seconds that must elapse to display an Easter egg.
  The Easter egg is a picture of a Christmas tree.
  """
  robots = _parse(input, world_size)
  min_safety_factor = math.inf
  result = 0
  for t in range(1, elapsed_seconds + 1):
    for robot in robots:
      robot.move()
    safety_factor = _calc_safety_factor(robots)
    # Thanks to reddit.com/r/adventofcode we know that the picture is small and
    # fits in one quadrant. In other words, it's when the safest factor is the
    # lowest.
    if safety_factor < min_safety_factor:
      min_safety_factor = safety_factor
      result = t
      # Only print state when finding a lower safety factor.
      print(f't={t}')
      _print_world(robots, world_size)
  return result
