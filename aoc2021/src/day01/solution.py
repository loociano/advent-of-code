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
from typing import Tuple


def part_one(depth_report: Tuple[int]) -> int:
    """AOC 2021 Day 1 Part 1.

    Args:
      depth_report: A sonar sweep report which consist of depth measurements.
    Returns:
      Number of times a depth measurement increases.
    """
    count_depth_increases = 0
    last_depth = None
    for depth in depth_report:
        count_depth_increases += 1 if (last_depth and depth > last_depth) else 0
        last_depth = depth
    return count_depth_increases
