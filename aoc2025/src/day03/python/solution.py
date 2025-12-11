# Copyright 2025 Google LLC
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


def find_max_joltage(bank: str, curr: str = '', digits_left: int = 12,
                     max_joltage: int = 0) -> int:
  """Returns the maximum joltage for a given bank and number of digits
  (batteries) to swap.

  Assumes the length of the bank is equal or greater than the digits left.
  """
  if digits_left == 0:
    return max(int(curr), max_joltage)
  for i in range(9, 0, -1):
    pos = bank.find(str(i))
    if pos != -1 and len(bank) - pos >= digits_left:
      return find_max_joltage(bank=bank[pos + 1:],
                              curr=curr + str(i),
                              digits_left=digits_left - 1,
                              max_joltage=max_joltage)
  return max_joltage


def calc_total_output_joltage(banks: Sequence[str], batteries: int = 2) -> int:
  """Calculates the total output joltage for the given banks."""
  return sum(find_max_joltage(bank, digits_left=batteries) for bank in banks)
