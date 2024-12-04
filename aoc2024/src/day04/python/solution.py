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
from typing import Sequence

def _extract_all_lines(input: Sequence[str]) -> Sequence[str]:
    lines = []
    width = len(input[0])
    height = len(input)
    # Horizontals
    for line in input:
        lines.append(line)
    # Verticals
    for x in range(width):
        vertical = []
        for y in range(len(input)):
            vertical.append(input[y][x])
        lines.append(''.join(vertical))
    # Decreasing diagonals
    for delta in range(-width+2, width):
        diagonal = []
        for y in range(height):
            if 0 <= y+delta < width:
                diagonal.append(input[y][y+delta])
        lines.append(''.join(diagonal))
    # Increasing diagonals
    for delta in range(-width, width-2):
        diagonal = []
        for y in range(height-1, -1, -1):
            if 0 <= width-y+delta < width:
                diagonal.append(input[y][width-y+delta])
        lines.append(''.join(diagonal))
    return lines

def count_xmas_words(input: Sequence[str]) -> int:
    lines = _extract_all_lines(input)
    return sum(line.count('XMAS') for line in lines) + sum(line.count('SAMX') for line in lines)