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
from collections import Counter
from itertools import product

type Lock = tuple[int, ...]
type Key = Lock

_SCHEMATIC_HEIGHT = 7
_KEY_LOCK_SIZE = _SCHEMATIC_HEIGHT - 2  # Crop top and bottom lines.


def _parse_schematics(schematics: Sequence[str]) -> tuple[tuple[Lock, ...], tuple[Key, ...]]:
  """
  Returns keys and locks represented by pin heights.

  Example lock: (0,5,3,4,3) and key: (5,0,2,1,3).
  """
  width = len(schematics[0])
  locks = []
  keys = []
  for i in range(0, len(schematics), _SCHEMATIC_HEIGHT + 1):  # Include separator line.
    first_line = schematics[i]
    if first_line == '#####':
      is_lock = True
    elif first_line == '.....':
      is_lock = False
    else:
      raise ValueError('Invalid input')
    counter = Counter()
    for j in range(i + 1, i + _SCHEMATIC_HEIGHT - 1):  # Skip last schematic line.
      counter.update(enumerate(list(schematics[j])))
    histogram = tuple([counter[(i, '#')] for i in range(width)])
    if is_lock:
      locks.append(histogram)
    else:
      keys.append(histogram)
  return tuple(locks), tuple(keys)


def _fits(lock: Lock, key: Key) -> bool:
  """
  Returns true iff a key fits in a lock.

  Unlike a real key, key does not have to fit perfectly in lock. Gaps are allowed.
  """
  for i, pin_height in enumerate(key):
    available_space = _KEY_LOCK_SIZE - lock[i]
    if available_space - pin_height < 0:
      return False
  return True


def count_unique_lock_key_pairs(schematics: Sequence[str]) -> int:
  """Counts unique pairs of (key,lock) that fit."""
  locks, keys = _parse_schematics(schematics)
  return sum(1 if _fits(key=key, lock=lock) else 0 for lock, key in product(locks, keys))
