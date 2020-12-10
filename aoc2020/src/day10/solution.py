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


def part_one(adapter_list: List[int]) -> int:
  """
  Returns:
     Number of 1-jolt differences multiplied by number of 3-jolt differences.
  """
  voltage_range = 3
  last_voltage = 0
  one_jolt_diffs = 0
  # built-in joltage adapter is rated for 3 jolts higher than the highest-rated
  # adapter in your bag.
  three_jolt_diffs = 1
  sorted_adapters = sorted(adapter_list)
  while len(sorted_adapters):
    print(last_voltage)
    diff = sorted_adapters[0] - last_voltage
    if diff == 1:
      one_jolt_diffs += 1
    elif diff == 3:
      three_jolt_diffs += 1
    else:
      raise Exception(diff)
    last_voltage = sorted_adapters[0]
    del sorted_adapters[0]
  return one_jolt_diffs * three_jolt_diffs