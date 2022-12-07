# Copyright 2022 Google LLC
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
import logging
from typing import Any, Dict, Sequence, Tuple, Union

_FILESYSTEM_SIZE = 70_000_000
_REQUIRED_EMPTY_SPACE = 30_000_000


class File:
  def __init__(self, name: str, size: int):
    self.name = name
    self.size = size


class Directory:
  # TODO: how can parent type be Directory?
  def __init__(self, name: str, parent: Any = None, size: int = 0):
    self.name = name
    self.parent = parent
    self.children = []  # List[Union[Directory, File]]
    self.size = size

  def find_dir(self, name: str):
    for child in self.children:
      if child.name == name and isinstance(child, Directory):
        return child
    raise ValueError('Child %s was not found!', name)


def _traverse(root: Union[Directory, File], path: str,
              dir_sizes: Dict[str, int]) -> Tuple[str, int]:
  # Base case.
  if isinstance(root, File):
    return path + root.name, root.size
  # Recursive step.
  if root.name == '/':
    current_path = '/'
  else:
    current_path = path + root.name + '/'
  for child in root.children:
    _, sub_size = _traverse(root=child, path=current_path,
                            dir_sizes=dir_sizes)
    root.size += sub_size
  dir_sizes[current_path] = root.size
  return current_path, root.size


def _parse(terminal_output: Sequence[str]) -> Directory:
  root = Directory(name='/')
  current = root
  # Convert terminal output to tree.
  for line in terminal_output:
    if line[0] == '$':  # This is a command.
      if line == '$ cd /':
        continue
      if line == '$ ls':
        continue
      if line.startswith('$ cd '):
        dest = line[5:]
        if dest == '..':  # Special case: go up.
          current = current.parent
        else:  # Go down.
          current = current.find_dir(name=dest)
    else:  # ls command output (no other supported commands...yet).
      if line.startswith('dir'):
        _, dir_name = line.split(' ')
        current.children.append(Directory(name=dir_name, parent=current))
      else:
        # Must be a file.
        size, name = line.split(' ')
        current.children.append(File(name=name, size=int(size)))
  return root


def sum_directory_sizes(terminal_output: Sequence[str],
                        max_directory_size: int = 100000) -> int:
  dir_sizes = {}
  path, total_size = _traverse(root=_parse(terminal_output), path='',
                               dir_sizes=dir_sizes)
  logging.debug(f'{path}: {total_size}')
  return sum([size if size <= max_directory_size else 0 for size in
              dir_sizes.values()])


def smallest_dir_size_to_delete(terminal_output: Sequence[str]) -> int:
  dir_sizes = {}
  path, total_size = _traverse(root=_parse(terminal_output), path='',
                               dir_sizes=dir_sizes)
  unused_space = _FILESYSTEM_SIZE - total_size
  target_delete_size = _REQUIRED_EMPTY_SPACE - unused_space
  return min(
    filter(lambda size: size >= target_delete_size, dir_sizes.values()))
