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


def _calculate_offset(report: Sequence[str], position: int) -> int:
    """Calculates offset in a given position of a report.

    Args:
        report: A sequence of binary numbers.
        position: Position to calculate offset.
    Returns:
        Positive value indicates that there are more ones than zeroes, negative
        value that thare are more zeroes than ones, and zero means equal number
        of ones and zeroes.
    """
    offset = 0
    for binary_str in report:
        offset += 1 if binary_str[position] == '1' else -1
    return offset


def _reduce(report: Sequence[str],
            position: int, match: int) -> Sequence[str]:
    """Reduces a list of binary numbers based on position and match.

    Args:
        report: A sequence of binary numbers.
        position: Digit position to evaluate.
        match: Binary value to match, 0 or 1.
    Returns:
        A reduced copy of the report containing the matching binary numbers.
    """
    reduced_report = []
    for binary_str in report:
        if int(binary_str[position]) == match:
            reduced_report.append(binary_str)
    return reduced_report


def _find_rating(report: Sequence[str], most_common: bool) -> int:
    """Finds rating in report.

    Args:
        report: A sequence of binary numbers.
        most_common: Whether to keep numbers with the most common value if True,
        or keep numbers with the least common value if False.
    Returns:
        A decimal number representing a rating.
    """
    num_bits = len(report[0])
    position = 0
    working_report = list(report)
    while len(working_report) > 1:
        if position >= num_bits:
            raise Exception('Could not find number.')
        offset = _calculate_offset(report=working_report, position=position)
        if most_common:
            criteria = 1 if offset >= 0 else 0
        else:
            criteria = 0 if offset >= 0 else 1
        working_report = _reduce(report=working_report,
                                 position=position,
                                 match=criteria)
        position += 1
    return int(working_report[0], 2)


def part_one(diagnostic_report: Sequence[str]) -> int:
    """AOC 2021 Day 3 Part 1.

    Args:
        diagnostic_report: A sequence of binary numbers.
    Returns:
      Gamma rate multiplied by the epsilon rate.
    """
    if not diagnostic_report:
        raise ValueError('Missing diagnostic report!')
    num_bits = len(diagnostic_report[0])
    most_common_bits = [
        '1' if _calculate_offset(diagnostic_report, position) > 0 else '0' for
        position in range(0, num_bits)]
    gamma_rate = ''.join(most_common_bits)
    epsilon_rate = ''.join(
        '0' if bit == '1' else '1' for bit in most_common_bits)
    return int(gamma_rate, 2) * int(epsilon_rate, 2)


def part_two(report: Sequence[str]) -> int:
    """AOC 2021 Day 3 Part 2.

    Args:
        report: A sequence of binary numbers.
    Returns:
      Oxygen generator rating multiplied by the CO2 scrubber rating.
    """
    if not report:
        raise ValueError('Missing diagnostic report!')
    oxygen_generator_rating = _find_rating(report=report, most_common=True)
    co2_scrubber_rating = _find_rating(report=report, most_common=False)
    return oxygen_generator_rating * co2_scrubber_rating
