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
from typing import List


class AdventOfCodeTestCase(unittest.TestCase):
  EXAMPLE_TEMPLATE = 'example{}.txt'

  def __init__(self, test_dir: str, *args, **kwargs):
    super(AdventOfCodeTestCase, self).__init__(*args, **kwargs)
    self.test_dir = test_dir
    self.examples = [self._read_as_list(
        self._get_path(self.EXAMPLE_TEMPLATE.format(num)))
        for num in range(1, self._get_num_examples() + 1)]
    input_path = self._get_path('input.txt')
    self.input = self._read_as_list(input_path) \
      if path.exists(input_path) else None

  def _get_num_examples(self) -> int:
    num = 1
    while True:
      if path.exists(self._get_path(self.EXAMPLE_TEMPLATE.format(num))):
        num += 1
      else:
        return num - 1

  @staticmethod
  def _read_as_list(file_path: str) -> List:
    with open(file_path) as file:
      return [x.strip() for x in file.readlines()]

  def _get_path(self, filename: str) -> str:
    return os.path.join(os.path.dirname(self.test_dir), filename)