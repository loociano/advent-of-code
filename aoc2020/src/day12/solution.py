# Copyright 2020 Google LLC
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
from typing import List
from aoc2020.src.day12.Ship import Ship
from aoc2020.src.day12.ShipWithWaypoint import ShipWithWaypoint


def part_one(instructions: List[str]) -> int:
  ship = Ship()
  for instruction in instructions:
    ship.navigate(instruction)
  return ship.manhattan_distance()


def part_two(instructions: List[str]) -> int:
  ship = ShipWithWaypoint()
  for instruction in instructions:
    ship.navigate(instruction)
  return ship.manhattan_distance()