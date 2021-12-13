# Copyright 2021 Google LLC
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


def _calculate_fuel(positions: Sequence[int], align_position: int) -> int:
    return sum([abs(p - align_position) for p in positions])


def part_one(positions: Sequence[int]) -> int:
    """AOC 2021 Day 7 Part 1.

    Args:
        positions: Sequence of crabs horizontal positions.
    Returns:
        The least amount of fuel needed to align.
    """
    valid_positions = set(positions)
    min_fuel = 100000000
    for p in valid_positions:
        fuel = _calculate_fuel(positions, p)
        if fuel < min_fuel:
            min_fuel = fuel
    return min_fuel


def part_two(positions: Sequence[int]) -> int:
    """AOC 2021 Day 7 Part 2.
    """
    return 0
