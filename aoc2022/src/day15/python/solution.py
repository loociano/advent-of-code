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
  def __init__(self, x: int, y: int, bx: int, by: int):
    self._sensor_pos = (x, y)
    self._closest_beacon_pos = (bx, by)
    self._distance = get_manhattan_distance(position_a=self._sensor_pos,
                                            position_b=self._closest_beacon_pos)
    # Will be calculated later.
    self.intervals_at_row: Optional[tuple[Interval, ...]] = None

  def calc_intervals_at_row(self, row: int) -> Optional[tuple[Interval, ...]]:
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


def _parse_sensors_data(sensors_data: Sequence[str],
                        ) -> tuple[tuple[Sensor, ...], set[Position]]:
  sensors: list[Sensor] = []
  beacon_positions = set()
  for sensor_data in sensors_data:
    matches = re.search(
      r'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)',
      sensor_data)
    bx = int(matches.group(3))
    by = int(matches.group(4))
    sensors.append(Sensor(
      x=int(matches.group(1)),
      y=int(matches.group(2)),
      bx=bx,
      by=by))
    beacon_positions.add((bx, by))
  return tuple(sensors), beacon_positions


def _merge_intervals(intervals: tuple[Interval, ...]) -> tuple[Interval, ...]:
  merged = []
  for begin, end in sorted(intervals):
    if len(merged) and merged[-1][1] >= begin - 1:
      merged[-1][1] = max(merged[-1][1], end)
    else:
      merged.append([begin, end])
  copy = []
  for interval in merged:
    copy.append((interval[0], interval[1]))
  return tuple(copy)


def _count_positions(intervals: tuple[Interval, ...]) -> int:
  count = 0
  for interval in intervals:
    count += abs(interval[1] - interval[0] + 1)
  return count


def _calc_merged_intervals_at_row(
    sensors: tuple[Sensor, ...]) -> tuple[Interval, ...]:
  intervals = []
  for sensor in sensors:
    if sensor.intervals_at_row is not None:
      for interval_at_row in sensor.intervals_at_row:
        intervals.append(interval_at_row)
  return _merge_intervals(tuple(intervals))


def count_not_beacon_positions(sensors_data: Sequence[str], row: int) -> int:
  sensors, _ = _parse_sensors_data(sensors_data)
  for sensor in sensors:
    sensor.intervals_at_row = sensor.calc_intervals_at_row(row)
  return _count_positions(_calc_merged_intervals_at_row(sensors))


def find_tuning_frequency(sensors_data: Sequence[str],
                          known_range: Interval) -> int:
  sensors, beacon_positions = _parse_sensors_data(sensors_data)
  for row in range(known_range[0], known_range[1] + 1):
    for sensor in sensors:
      sensor.intervals_at_row = sensor.calc_intervals_at_row(row)
    merged = _calc_merged_intervals_at_row(sensors)
    if len(merged) > 1:
      x = merged[0][1] + 1
      if (x, row) not in beacon_positions:
        return 4000000 * x + row
  raise ValueError('Did not find frequency!')
