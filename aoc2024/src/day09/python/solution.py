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

_EMPTY_SPACE = '.'


def _generate_disk(disk_map: str) -> list[str]:
  """Generates actual disk from a disk map.
  A disk map alternates between blocks of files and empty space."""
  disk = []
  file_id = 0
  is_file = True
  for digit in disk_map:
    for i in range(int(digit)):
      # Disk layout alternates between files and free space.
      value = str(file_id) if is_file else _EMPTY_SPACE
      disk.append(value)
    if is_file:
      file_id += 1
    is_file = not is_file
  return disk


def _shift_files(disk: list[str]) -> list[str]:
  """
  Shift files in a disk starting from the rightmost file to the leftmost empty space.
  """
  i = len(disk) - 1
  first_empty = disk.index(_EMPTY_SPACE)
  while first_empty < i:
    if disk[i] != _EMPTY_SPACE:
      # Swap rightmost file and leftmost empty space.
      disk[first_empty] = disk[i]
      disk[i] = _EMPTY_SPACE
    first_empty = disk.index(_EMPTY_SPACE)
    i -= 1
  return disk


def _checksum(disk: list[str]) -> int:
  """Calculates disk checksum as the sum of each position multiplied by its file ID.
  Example: checksum(['0','2','2','1','.']) = 0*0 + 1*2 + 2*2 + 3*1 = 9.

  Time complexity: O(n)
  Space complexity: O(1)
  """
  check_sum = 0
  for index, value in enumerate(disk):
    if value == _EMPTY_SPACE:
      # Disk is organized so there should not be more files to sum.
      return check_sum
    check_sum += index * int(value)
  return check_sum


def checksum(disk_map: str) -> int:
  """Calculates the disk checksum given a disk map."""
  return _checksum(_shift_files(_generate_disk(disk_map)))
