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
import os
import re
import unittest

from os import path
from typing import Sequence

_EXAMPLE_FILENAME_TEMPLATE = 'example{}.txt'


def _get_path(root_dir: str, year: int, day: int, filename: str) -> str:
  """Returns the expected filepath for a given AoC year and day."""
  return os.path.join(os.path.dirname(root_dir), str(year), str(day), filename)


def _find_num_examples(root_dir: str, year: int, day: int) -> int:
  """Returns the number of examples given on a given day.

  Examples are provided in addition to the puzzle input. Can be zero."""
  num = 1
  while True:
    if path.exists(_get_path(root_dir=root_dir,
                             year=year, day=day,
                             filename=_EXAMPLE_FILENAME_TEMPLATE.format(num))):
      num += 1
    else:
      return num - 1


def _read(file_path: str) -> Sequence[str]:
  """Reads an ASCII file.

  Args
    file_path: location of the file to read.
  Returns:
    File content lines.
  """
  with open(file_path) as file:
    return tuple(line.rstrip('\n') for line in file.readlines())


class AdventOfCodeTestCase(unittest.TestCase):

  def __init__(self, test_filepath, *args, **kwargs) -> None:
    """Initializes AoC Test Case, reading example(s) and puzzle input.

    Examples may be provided as example1.txt, example2.txt, etc.
    Puzzle input must be provided as input.txt.

    Test cases can access self.examples tuple and self.input.
    """
    super().__init__(*args, **kwargs)
    inputs_directory = __file__[:__file__.index('advent-of-code')] + 'advent-of-code\\advent-of-code-inputs\\'
    matches = re.search(r'aoc(\d{4}).*day(\d{2})', test_filepath)
    year = int(matches[1])
    day = int(matches[2])
    num_examples = _find_num_examples(root_dir=inputs_directory, year=year, day=day)
    self.examples: Sequence[Sequence[str]] = tuple(
      _read(file_path=_get_path(root_dir=inputs_directory,
                                year=year, day=day,
                                filename=_EXAMPLE_FILENAME_TEMPLATE.format(num)))
      for num in range(1, num_examples + 1))  # Examples are numbered 1,2,3...
    input_path = _get_path(root_dir=inputs_directory, year=year, day=day, filename='input.txt')
    if path.exists(input_path):
      self.input: Sequence[str] = _read(file_path=input_path)
