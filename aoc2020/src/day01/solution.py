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


def part_one(expense_report: List[int]) -> int:
  seen = {}
  for entry in expense_report:
    if (2020 - entry) in seen:
      return (2020 - entry) * entry
    seen[entry] = True
  raise Exception('Did not find 2 numbers that sum 2020.')


def part_two(expense_report: List[int]) -> int:
  precompute = {}
  for i in expense_report:
    for j in expense_report:
      precompute[i + j] = i * j

  for entry in expense_report:
    if (2020 - entry) in precompute:
      return precompute[2020 - entry] * entry
  raise Exception('Did not find 3 numbers that sum 2020.')