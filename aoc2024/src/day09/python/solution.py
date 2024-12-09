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

_EMPTY_SPACE = '.'


class SpaceNotFoundError(ValueError):
  pass


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


def _defrag(disk: list[str]) -> list[str]:
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


def _find_first_available_space(disk: list[str], file_start_index: int, file_size: int) -> int:
  """Returns first index at which a file will fit."""
  next_start = 0
  while next_start < file_start_index:
    try:
      index = disk.index(_EMPTY_SPACE, next_start)
      for i in range(index, index + file_size):
        # Last empty space, it fits!
        if i == index + file_size - 1 and disk[i] == _EMPTY_SPACE:
          return index
        if disk[i] != _EMPTY_SPACE:
          next_start = i
          break
    except ValueError:
      raise SpaceNotFoundError('Did not find empty space!')
  raise SpaceNotFoundError('Did not find empty space!')


def _defrag_whole_files(disk_map: str, disk: list[str]) -> list[str]:
  # Assumption: disk_map ends in file not empty block.
  for file_id in range(len(disk_map) // 2, 0, -1):
    file_size = int(disk_map[file_id * 2])  # map alternates between files and empty space.
    try:
      file_start_index = disk.index(str(file_id))
      free_space_index = _find_first_available_space(disk, file_start_index, file_size)
      # Clear from previous location.
      for i in range(file_start_index, file_start_index + file_size):
        disk[i] = _EMPTY_SPACE
      # Move to empty space.
      for i in range(free_space_index, free_space_index + file_size):
        disk[i] = str(file_id)
    except SpaceNotFoundError:
      # Skip file IDs with size zero.
      # Only attempt to move file once.
      pass
  return disk


def _checksum(disk: list[str], move_whole_files) -> int:
  """Calculates disk checksum as the sum of each position multiplied by its file ID.
  Example: checksum(['0','2','2','1','.']) = 0*0 + 1*2 + 2*2 + 3*1 = 9.

  Time complexity: O(n)
  Space complexity: O(1)
  """
  check_sum = 0
  if move_whole_files:
    # Need to scan the whole disk.
    # There can be empty space between files.
    return sum(index * int(file_id) if file_id != _EMPTY_SPACE else 0
               for index, file_id in enumerate(disk))
  else:
    for index, value in enumerate(disk):
      # Disk is organized so we can stop here. No need to scan whole disk.
      if value == _EMPTY_SPACE:
        return check_sum
      check_sum += index * int(value)
  return check_sum


def checksum(disk_map: str, move_whole_files=False) -> int:
  """Calculates the disk checksum given a disk map."""
  disk = _generate_disk(disk_map)
  disk = _defrag_whole_files(disk_map=disk_map, disk=disk) if move_whole_files else _defrag(disk)
  return _checksum(disk, move_whole_files)
