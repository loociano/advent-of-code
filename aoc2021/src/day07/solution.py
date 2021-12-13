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


def _calculate_fuel(positions: Sequence[int], align_position: int,
                    constant_rate: bool = True) -> int:
    """Calculates fuel to align all positions to one position.

    Args
        positions: Sequence of horizontal positions.
        align_position: Position to align to.
        constant_rate: Whether the fuel cost increases at constant rate.
    Returns:
        Fuel cost.
    """
    if constant_rate:
        return sum([abs(p - align_position) for p in positions])
    else:
        total = 0
        for p in positions:
            distance = abs(p - align_position)
            # Sum of sequence of natural numbers: 1 + 2 + 3...
            total += int(distance * (distance + 1) / 2)
        return total


def _calculate_min_fuel(positions: Sequence[int],
                        constant_rate: bool = True) -> int:
    valid_positions = range(0, max(positions))
    min_fuel = 100000000
    for p in valid_positions:
        fuel = _calculate_fuel(positions=positions, align_position=p,
                               constant_rate=constant_rate)
        if fuel < min_fuel:
            min_fuel = fuel
    return min_fuel


def part_one(positions: Sequence[int]) -> int:
    """AOC 2021 Day 7 Part 1.

    Args:
        positions: Sequence of crabs horizontal positions.
    Returns:
        The least amount of fuel needed to align.
    """
    return int(_calculate_min_fuel(positions=positions))


def part_two(positions: Sequence[int]) -> int:
    """AOC 2021 Day 7 Part 2.

    Crab submarine engines don't burn fuel at a constant rate. Instead, each
    change of 1 step in horizontal position costs 1 more unit of fuel than the
    last: the first step costs 1, the second step costs 2, the third step costs
    3, and so on.

    Args:
        positions: Sequence of crabs horizontal positions.
    Returns:
        The least amount of fuel needed to align.
    """
    return _calculate_min_fuel(positions=positions, constant_rate=False)
