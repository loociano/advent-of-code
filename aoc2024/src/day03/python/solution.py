# Copyright 2024 Google LLC
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
import re
from functools import reduce

def calculate(input: str) -> int:
    """Sums all the valid multiplications.
    Example multiplication: mul(1,2)
    """
    matches = re.findall(r'mul\(((\d+),(\d+))\)', input)
    if matches is None:
        raise ValueError('No multiplications were found.')
    muls = tuple(tuple(map(int, (match[1], match[2]))) for match in matches)  # O(n)
    return sum(reduce(lambda a,b: a*b, mul) for mul in muls)  # O(n)