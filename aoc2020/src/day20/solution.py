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
from functools import reduce
from typing import List, Tuple, Union
from aoc2020.src.day20.Tile import Tile


def part_one(input_lines: List[str]) -> int:
  """
  Returns:
    Product of the IDs of the four corner tiles.
  """
  tiles = _parse_tiles(input_lines)
  corners_ids = []
  not_corners_ids = []
  while len(corners_ids) < 4:
    for tile in tiles:
      if tile.tile_id in corners_ids or tile.tile_id in not_corners_ids:
        continue
      result = _is_corner_tile(tiles, tile)
      if result is not None:
        corners_ids.append(result[0])
        not_corners_ids.append(result[1])
        not_corners_ids.append(result[2])
  return reduce((lambda x, y: x * y), corners_ids)


def _parse_tiles(input_lines: List[str]) -> List[Tile]:
  tiles = []
  tile_id = None
  image = []
  for line in input_lines:
    if not line:  # flush
      tiles.append(Tile(tile_id, image))
      image = []
    elif 'Tile' in line:
      tile_id = int(line.split(' ')[1].split(':')[0])
    else:
      image.append(list(line))
  # Last tile
  tiles.append(Tile(tile_id, image))
  return tiles


def _is_corner_tile(tiles: List[Tile], tile: Tile) \
    -> Union[Tuple[int, int, int], None]:
  """
  Returns:
    Tile ID of the corner tile and tile IDs of the 2 adjacent tiles.
    None if the tile is not a corner tile.
  :return:
  """
  result = _find_adj_tiles(tiles, tile.tile_id, tile.get_borders())
  if result is not None:
    return result
  result = _find_adj_tiles(tiles, tile.tile_id, tile.get_flipped_borders())
  if result is not None:
    return result


def _find_adj_tiles(tiles: List[Tile],
                    tile_id: int, borders: Tuple[str, str, str, str]) \
    -> Union[Tuple[int, int, int], None]:
  candidates = []
  for other_tile in tiles:
    if other_tile.tile_id == tile_id or other_tile.tile_id in candidates:
      continue
    if _is_adj_tile(borders, other_tile):
      candidates.append(other_tile.tile_id)
  if len(candidates) == 2:
    return tile_id, candidates[0], candidates[1]


def _is_adj_tile(borders: Tuple[str, str, str, str], tile: Tile) -> bool:
  return _count_matching_borders(borders, tile.get_borders()) == 1 \
         or _count_matching_borders(borders, tile.get_flipped_borders()) == 1


def _count_matching_borders(borders: Tuple[str, str, str, str],
                            other_borders: Tuple[str, str, str, str]) -> int:
  matching_borders = 0
  for border in borders:
    for other_border in other_borders:
      if border == other_border:
        matching_borders += 1
  return matching_borders