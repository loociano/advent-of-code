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


def find_max_joltage(bank: str) -> int:
  return max(int(bank[i] + bank[j])
             for i in range(0, len(bank) - 1)
             for j in range(i + 1, len(bank)))


def calc_total_output_joltage(banks: Sequence[str]) -> int:
  return sum(find_max_joltage(bank) for bank in banks)
