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
from math import inf
from typing import Sequence
from collections import deque, defaultdict
from itertools import product
from functools import cache
from common.python3.types import Position

type KeyPad = tuple[tuple[str, str, str], ...]
type Path = tuple[str, ...]

_EMPTY_KEY = ' '
_NUMPAD: KeyPad = (
  ('7', '8', '9'),
  ('4', '5', '6'),
  ('1', '2', '3'),
  (_EMPTY_KEY, '0', 'A'),
)
_DIR_KEYPAD: KeyPad = (
  (_EMPTY_KEY, '^', 'A'),
  ('<', 'v', '>'),
)
_DIR_MAP = {
  (0, -1): '^',
  (1, 0): '>',
  (0, 1): 'v',
  (-1, 0): '<',
}


def get_pos(keypad: KeyPad, key_value: str) -> Position:
  """Returns the position of a key in a given keypad."""
  for y in range(len(keypad)):
    for x in range(len(keypad[0])):
      if keypad[y][x] == key_value:
        return x, y
  raise ValueError(f'Could not find {key_value} in keypad!')


def _find_shortest_paths_between_key_pairs(keypad: KeyPad, keys: tuple[str, ...]) -> dict[(str, str), tuple[Path, ...]]:
  """Returns shortest path(s) between all pairs of keys in a keypad using BFS."""
  shortest_paths: dict[(str, str), list[Path]] = defaultdict(list)
  for permutation in product(keys, repeat=2):
    start_pos = get_pos(keypad, permutation[0])
    end_pos = get_pos(keypad, permutation[1])
    queue = deque()
    queue.append((start_pos, []))
    visited: set[Position] = {start_pos}
    while queue:
      curr_pos, path = queue.popleft()
      if curr_pos == end_pos:
        complete_path = path.copy()
        complete_path.append('A')  # Press the button.
        shortest_paths[(permutation[0], permutation[1])].append(tuple(complete_path))
      else:
        for dxy in ((0, -1), (1, 0), (0, 1), (-1, 0)):
          next_pos = (curr_pos[0] + dxy[0], curr_pos[1] + dxy[1])
          if (0 <= next_pos[0] < len(keypad[0]) and 0 <= next_pos[1] < len(keypad)
                  and keypad[next_pos[1]][next_pos[0]] != _EMPTY_KEY
                  and next_pos not in visited):
            new_path = path.copy()
            new_path.append(_DIR_MAP.get(dxy))
            queue.append((next_pos, new_path))
      visited.add(curr_pos)
  # Return a copy with immutable paths.
  result = dict()
  for k, v in shortest_paths.items():
    result[k] = tuple(v)
  return result


# Precompute the shortest paths between key pairs in numpad and directional keypad.
_NUMPAD_PATHS = _find_shortest_paths_between_key_pairs(keypad=_NUMPAD,
                                                       keys=('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A'))
_DIR_KEYPAD_PATHS = _find_shortest_paths_between_key_pairs(keypad=_DIR_KEYPAD, keys=('A', '^', 'v', '<', '>'))


@cache
def _shortest_sequence_length(start_key: str, end_key: str, num_dir_keypads: int, remaining_dir_keypads: int) -> int:
  if remaining_dir_keypads == 0:
    return len(_DIR_KEYPAD_PATHS.get((start_key, end_key))[0])  # All shortest path(s) have same length.
  min_button_presses = inf
  key_paths = _NUMPAD_PATHS if remaining_dir_keypads == num_dir_keypads else _DIR_KEYPAD_PATHS
  for key_pair_path in key_paths.get((start_key, end_key)):
    button_presses = 0
    last_key = 'A'  # Important for recursion and memoize: robot movements start and end at the 'A' key!
    for target_key in key_pair_path:
      button_presses += _shortest_sequence_length(start_key=last_key, end_key=target_key,
                                                  num_dir_keypads=num_dir_keypads,
                                                  remaining_dir_keypads=remaining_dir_keypads - 1)
      last_key = target_key
    min_button_presses = min(min_button_presses, button_presses)
  return min_button_presses


def get_complexity(door_code: str, num_dir_keypads: int = 2) -> int:
  """Returns the complexity of a door code.
  The complexity is minimum button presses required multiplied by the numeric part of the door code."""
  min_button_presses = 0
  last_key = 'A'  # Robot arm always starts at 'A' in the numpad.
  for target_key in door_code:
    min_button_presses += _shortest_sequence_length(start_key=last_key, end_key=target_key,
                                                    num_dir_keypads=num_dir_keypads,
                                                    remaining_dir_keypads=num_dir_keypads)
    last_key = target_key
  return min_button_presses * int(door_code[:-1])


def get_total_complexity(door_codes: Sequence[str], num_dir_keypads: int = 2) -> int:
  """Returns the total complexity of door codes."""
  return sum(get_complexity(door_code, num_dir_keypads) for door_code in door_codes)
