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


def _most_common_bit(diagnostic_report: Sequence[str], position: int) -> bool:
    offset = 0
    for binary_str in diagnostic_report:
        offset += 1 if binary_str[position] == '1' else -1
    return offset > 0


def part_one(diagnostic_report: Sequence[str]) -> int:
    """AOC 2021 Day 3 Part 1.

    Args:
        diagnostic_report: A list of binary numbers.
    Returns:
      Gamma rate multiplied by the epsilon rate.
    """
    if not diagnostic_report:
        raise ValueError('Missing diagnostic report!')
    num_bits = len(diagnostic_report[0])
    most_common_bits = []
    for position in range(0, num_bits):
        most_common_bits.append(_most_common_bit(diagnostic_report, position))
    gamma_rate = ''.join('1' if bit else '0' for bit in most_common_bits)
    epsilon_rate = ''.join('0' if bit else '1' for bit in most_common_bits)
    return int(gamma_rate, 2) * int(epsilon_rate, 2)
