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
from typing import List, Tuple, Dict


def part_one(move_list: List[str]) -> int:
  """
  Returns:
    Number of tiles with black side up.
  """
  return sum(1 if value == -1 else 0
             for value in _calculate_initial_state(move_list).values())


def part_two(move_list: List[str], days=100) -> int:
  """
  Returns:
    Number of black tiles after n days.
  """
  hexagons = _calculate_initial_state(move_list)
  for _ in range(days):
    # Initialize neighbours
    for known_coord in list(hexagons):
      adj_coords = _get_adjacent_coords(known_coord)
      for adj_coord in adj_coords:
        if hexagons.get(adj_coord) is None:
          hexagons[adj_coord] = 1  # Default white
    # Simulate new state
    new_hexagons = hexagons.copy()
    for pos, state in hexagons.items():
      adj_coords = _get_adjacent_coords(pos)
      num_adj_black = sum([1 if hexagons.get(adj_coord) == -1 else 0
                           for adj_coord in adj_coords])
      if state == -1 and (num_adj_black == 0 or num_adj_black > 2):
        new_hexagons[pos] = 1  # Flip black to white
      elif state == 1 and num_adj_black == 2:
        new_hexagons[pos] = -1  # Flip white to black
    hexagons = new_hexagons
  return sum(1 if value == -1 else 0 for value in hexagons.values())


def _calculate_initial_state(move_list: List[str]) \
    -> Dict[Tuple[int, int, int], int]:
  # Dictionary of hexagons and their state: white (1), black (-1)
  state = {}  # type:Dict[Tuple[int, int, int], int]
  for tile_moves in move_list:
    pos = (0, 0, 0)  # x,y,z
    for move in _decode_moves(tile_moves):
      pos = tuple([sum(coord) for coord in zip(pos, move)])
    state[pos] = -state[pos] if state.get(pos) is not None else -1
  return state


def _get_adjacent_coords(pos: Tuple[int, int, int]) \
    -> List[Tuple[int, int, int]]:
  result = []
  adjacent_coords = [(0, 1, -1), (1, 0, -1), (1, -1, 0), (0, -1, 1), (-1, 0, 1),
               (-1, 1, 0)]
  x, y, z = pos
  for coords in adjacent_coords:
    dx, dy, dz = coords
    result.append((x + dx, y + dy, z + dz))
  return result


def _get_num_adj_black(hexagons: Dict[Tuple[int, int, int], int],
                       pos: Tuple[int, int, int]) -> int:
  """
  Args:
    hexagons: all hexagons
    pos: hexagon to check
  Returns:
    Number of adjacent black tiles.
  """
  adjacents = [(0, 1, -1), (1, 0, -1), (1, -1, 0), (0, -1, 1), (-1, 0, 1),
               (-1, 1, 0)]
  return sum([1 if hexagons.get((pos[0] + adj[0],
                                 pos[1] + adj[1],
                                 pos[2] + adj[2])) == -1
              else 0 for adj in adjacents])


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
