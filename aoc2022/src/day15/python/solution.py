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
Interval: TypeAlias = tuple[int, int]


def get_manhattan_distance(position_a: Position, position_b: Position) -> int:
  return abs(position_a[0] - position_b[0]) + abs(position_a[1] - position_b[1])


class Sensor:
  def __init__(self, x: int, y: int, bx: int, by: int, row: int):
    self._sensor_pos = (x, y)
    self._closest_beacon_pos = (bx, by)
    self._distance = get_manhattan_distance(position_a=self._sensor_pos,
                                            position_b=self._closest_beacon_pos)
    self.intervals_at_row: tuple[Interval, ...] = self._calc_intervals_at_row(
      row=row)

  def _calc_intervals_at_row(self, row: int) -> Optional[tuple[Interval, ...]]:
    if (row < self._sensor_pos[1] - self._distance
        or row > self._sensor_pos[1] + self._distance):
      return None
    row_to_sensor = abs(row - self._sensor_pos[1])
    offset_x = self._distance - row_to_sensor
    min_x = self._sensor_pos[0] - offset_x
    max_x = self._sensor_pos[0] + offset_x
    if self._closest_beacon_pos[1] == row:
      if min_x == self._closest_beacon_pos[0] == max_x:
        # Edge case.
        return None
      if min_x == self._closest_beacon_pos[0]:
        return (
          (self._closest_beacon_pos[0] + 1, max_x),
        )
      if max_x == self._closest_beacon_pos[0]:
        return (
          (min_x, self._closest_beacon_pos[0] - 1),
        )
      if min_x < self._closest_beacon_pos[0] < max_x:
        return (
          (min_x, self._closest_beacon_pos[0] - 1),
          (self._closest_beacon_pos[0] + 1, max_x)
        )
    else:
      return (
        (min_x, max_x),
      )


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


def _merge_intervals(intervals: tuple[Interval, ...]) -> tuple[Interval, ...]:
  merged = []
  for begin, end in sorted(intervals):
    if len(merged) and merged[-1][1] >= begin - 1:
      merged[-1][1] = max(merged[-1][1], end)
    else:
      merged.append([begin, end])
  copy = []
  for i in merged:
    copy.append(tuple(i))
  return tuple(merged)


def _count_positions(intervals: tuple[Interval, ...]) -> int:
  count = 0
  for interval in intervals:
    count += abs(interval[1] - interval[0] + 1)
  return count


def count_not_beacon_positions(sensors_data: Sequence[str], row: int) -> int:
  sensors: tuple[Sensor] = _parse_sensors_data(sensors_data, row)
  print('Parsed all!')
  intervals = []
  for sensor in sensors:
    if sensor.intervals_at_row is not None:
      for interval_at_row in sensor.intervals_at_row:
        intervals.append(interval_at_row)
  merged_intervals = _merge_intervals(tuple(intervals))
  return _count_positions(merged_intervals)
