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
import unittest

from os import path
from typing import Tuple, Union


def _read(file_path: str, read_raw: bool = False) -> Union[Tuple[str], str]:
  """Reads an ASCII file.

  Args
    file_path: location of the file to read.
    read_raw: whether to read the file as is or line by line.
  Returns:
    File content lines.
  """
  with open(file_path) as file:
    if read_raw:
      return file.read()
    return tuple(x.strip() for x in file.readlines())


class AdventOfCodeTestCase(unittest.TestCase):
  EXAMPLE_TEMPLATE = 'example{}.txt'

  def __init__(self, test_dir: str, *args, **kwargs):
    """Initializes AoC Test Case, reading example(s) and puzzle input.

    Args:
      test_dir: directory where test are located.
      *args: arguments
      **kwargs: keyword arguments.
        - read_raw: whether to read examples and puzzle input as is or line by
        line.
    """
    if 'read_raw' in kwargs:
      read_raw = kwargs['read_raw']
      del kwargs['read_raw']
    else:
      read_raw = False
    super(AdventOfCodeTestCase, self).__init__(*args, **kwargs)
    self.test_dir = test_dir
    self.examples = tuple(_read(
      file_path=self._get_path(self.EXAMPLE_TEMPLATE.format(num)),
      read_raw=read_raw)
                          for num in range(1, self._get_num_examples() + 1))
    input_path = self._get_path('input.txt')
    if path.exists(input_path):
      self.input = _read(file_path=input_path, read_raw=read_raw)

  def _get_num_examples(self) -> int:
    num = 1
    while True:
      if path.exists(self._get_path(self.EXAMPLE_TEMPLATE.format(num))):
        num += 1
      else:
        return num - 1

  def _get_path(self, filename: str) -> str:
    return os.path.join(os.path.dirname(self.test_dir), filename)
