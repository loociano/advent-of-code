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
  """Breaks down the input grid into lines to facilitate word search.

  Time complexity: O(n) + O(nm) + O(2m*n) + O(2m*n) = O(nm)
  Space complexity: O(n) + O(m) + O(m+n) + O(m+n) = O(3m+3n) = O(m+n)
  """
  lines = []
  width = len(input[0])
  height = len(input)
  # Horizontals
  for line in input:
    lines.append(line)
  # Verticals
  for x in range(width):
    vertical = []
    for y in range(height):
      vertical.append(input[y][x])
    lines.append(''.join(vertical))
  # Decreasing diagonals
  for delta in range(-width + 2, width):
    diagonal = []
    for y in range(height):
      if 0 <= y + delta < width:
        diagonal.append(input[y][y + delta])
    lines.append(''.join(diagonal))
  # Increasing diagonals
  for delta in range(-width, width - 2):
    diagonal = []
    for y in range(height - 1, -1, -1):
      if 0 <= width - y + delta < width:
        diagonal.append(input[y][width - y + delta])
    lines.append(''.join(diagonal))
  return lines


def count_xmas_words(input: Sequence[str]) -> int:
  """Counts occurrences of the word XMAS in a grid.

  The word XMAS may appear horizontally, vertically and diagonally.
  It may appear reversed SMAX too.

  Time complexity: O(nm) + O(2(m+n)) = O(nm)
  Space complexity: O(n+m)
  """
  lines = _extract_all_lines(input)
  return sum(line.count('XMAS') for line in lines) + sum(line.count('SAMX') for line in lines)


def count_xmas_shapes(input: Sequence[str]) -> int:
  """Counts occurrences of the X-MAS shape in a grid.

  An X-MAS shape consists two 'MAS' crossing words that looks like this:
  M S
   A
  M S

  Time complexity: O(nm)
  Space complexity: O(1)
  """
  width = len(input[0])
  height = len(input)
  counter = 0
  for y in range(height):
    for x in range(width):
      # X-MAS shape must fit within bounds.
      if 0 < y < height - 1 and 0 < x < width - 1 and input[y][x] == 'A':
        # There are 4 possible X-MAS shapes:
        # M S  S S  M M  S M
        #  A    A    A    A
        # M S  M M  S S  S M
        found_shape = (((input[y - 1][x - 1] == 'M' and input[y + 1][x + 1] == 'S')
                        or (input[y - 1][x - 1] == 'S' and input[y + 1][x + 1] == 'M'))
                       and ((input[y + 1][x - 1] == 'M' and input[y - 1][x + 1] == 'S')
                            or (input[y + 1][x - 1] == 'S' and input[y - 1][x + 1] == 'M')))
        counter += 1 if found_shape else 0
  return counter
