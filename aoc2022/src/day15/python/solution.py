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
from typing import Optional, Sequence, TypeAlias

Position: TypeAlias = tuple[int, int]


def get_manhattan_distance(position_a: Position, position_b: Position) -> int:
  return abs(position_a[0] - position_b[0]) + abs(position_a[1] - position_b[1])


class Sensor:
  def __init__(self, x: int, y: int, bx: int, by: int, row: int):
    self._sensor_pos = (x, y)
    self._closest_beacon_pos = (bx, by)
    self._distance = get_manhattan_distance(position_a=self._sensor_pos,
                                            position_b=self._closest_beacon_pos)
    self.positions_at_row: set[Position, ...] = self._calc_positions_at_row(
      row=row)

  def _calc_positions_at_row(self, row: int) -> Optional[set[Position, ...]]:
    if (row < self._sensor_pos[1] - self._distance
        or row > self._sensor_pos[1] + self._distance):
      return None
    positions = set()
    row_to_sensor = abs(row - self._sensor_pos[1])
    offset_x = self._distance - row_to_sensor
    for x in range(-offset_x, offset_x + 1):
      position = (self._sensor_pos[0] - x, row)
      if position != self._closest_beacon_pos:
        positions.add(position)
    return positions


def _parse_sensors_data(sensors_data: Sequence[str], row: int) -> tuple[Sensor]:
  sensors: list[Sensor] = []
  for sensor_data in sensors_data:
    matches = re.search(
      r'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)',
      sensor_data)
    sensors.append(Sensor(
      x=int(matches.group(1)),
      y=int(matches.group(2)),
      bx=int(matches.group(3)),
      by=int(matches.group(4)),
      row=row))
  return tuple(sensors)


def count_not_beacon_positions(sensors_data: Sequence[str], row: int) -> int:
  sensors: tuple[Sensor] = _parse_sensors_data(sensors_data, row)
  print('Parsed all!')
  within_beacon_positions = set()
  for sensor in sensors:
    if sensor.positions_at_row is not None:
      within_beacon_positions = within_beacon_positions.union(
        sensor.positions_at_row)
  return len(within_beacon_positions)
