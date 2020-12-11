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
from typing import List, Dict


def part_one(adapter_list: List[int]) -> int:
  """
  Returns:
     Number of 1-jolt differences multiplied by number of 3-jolt differences.
  """
  last_voltage = 0
  one_jolt_diffs = 0
  # built-in joltage adapter is rated for 3 jolts higher than the highest-rated
  # adapter in your bag.
  three_jolt_diffs = 1
  sorted_adapters = sorted(adapter_list)
  while len(sorted_adapters):
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


def part_two(adapters: List[int]) -> int:
  """
  Returns:
    Total number of distinct ways you can arrange the adapters to connect the
    charging outlet to the device.
  """
  return calc_paths(curr=0, adapters=sorted([0] + adapters), memo = {})


def calc_paths(curr: int, adapters: List[int], memo: Dict[int, int]) -> int:
  if curr == len(adapters) - 1:
    return 1

  if adapters[curr + 1] - adapters[curr] == 3:
    # Only one possible path
    if memo.get(adapters[curr]) is None:
      memo[adapters[curr]] = calc_paths(curr + 1, adapters, memo)
    return memo.get(adapters[curr])

  sub_paths = 0
  for i in range(1, 4):  # voltage range = 3
    if curr + i < len(adapters) \
        and adapters[curr + i] - adapters[curr] - i + 1 == 1:
        if memo.get(adapters[curr + i]) is None:
          memo[adapters[curr + i]] = calc_paths(curr + i, adapters, memo)
        sub_paths += memo.get(adapters[curr + i])
  return sub_paths