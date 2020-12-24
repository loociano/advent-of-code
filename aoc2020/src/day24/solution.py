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
from typing import List, Tuple


def part_one(move_list: List[str]) -> int:
  """
  Returns:
    Number of tiles with black side up.
  """
  # Dictionary of hexagons and their state: white (1), black (-1)
  mem = {}  # type:Dict[Tuple[int, int, int], int]
  for tile_moves in move_list:
    pos = (0, 0, 0)  # x,y,z
    for move in _decode_moves(tile_moves):
      pos = tuple([sum(coord) for coord in zip(pos, move)])
    mem[pos] = -mem[pos] if mem.get(pos) is not None else -1
  return sum(1 if value == -1 else 0 for value in mem.values())


def _decode_moves(moves: str) -> List[Tuple[int, int, int]]:
  result = []
  pos = 0
  while pos < len(moves):
    if moves[pos] == 'e':
      result.append((1, -1, 0))
    elif moves[pos] == 'w':
      result.append((-1, 1, 0))
    elif pos < len(moves) - 1:
      if moves[pos] == 's' and moves[pos + 1] == 'e':
        result.append((0, -1, 1))
      elif moves[pos] == 's' and moves[pos + 1] == 'w':
        result.append((-1, 0, 1))
      elif moves[pos] == 'n' and moves[pos + 1] == 'w':
        result.append((0, 1, -1))
      elif moves[pos] == 'n' and moves[pos + 1] == 'e':
        result.append((1, 0, -1))
      else:
        raise Exception('Unknown direction.')
      pos += 1
    pos += 1
  return result
