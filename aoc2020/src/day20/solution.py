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
import math
from functools import reduce
from typing import List, Tuple, Union
from aoc2020.src.day20.Tile import Tile


def part_one(input_lines: List[str]) -> int:
  """
  Returns:
    Product of the IDs of the four corner tiles.
  """
  return reduce((lambda x, y: x * y), _find_corners(_parse_tiles(input_lines)))


def part_two(input_lines: List[str]) -> int:
  """
  Returns
    Number of # in the full image that are not part of a sea monster.
  """
  build_image(input_lines)
  # TODO: find position with monsters
  # TODO: count number of # that are not part of monsters
  return -1


def build_image(input_lines: List[str]) -> List[List[str]]:
  full_image = []
  first_ids_in_rows = []
  tiles = _parse_tiles(input_lines)
  length_in_tiles = int(math.sqrt(len(tiles)))
  corner_ids = _find_corners(tiles)
  top_left_tile = _find_tile(tiles, corner_ids[0])
  corner_id, adj1_id, adj2_id = _is_corner_tile(tiles, top_left_tile)
  right_border = _find_matching_border(top_left_tile,
                                       _find_tile(tiles, adj1_id))
  bottom_border = _find_matching_border(top_left_tile,
                                        _find_tile(tiles, adj2_id))
  _position_top_left_tile(top_left_tile, right_border, bottom_border)
  full_image.append([top_left_tile.image])
  first_ids_in_rows.append(top_left_tile.tile_id)
  last_tile = top_left_tile
  for row in range(length_in_tiles):
    if row > 0:
      target_bottom_border = ''.join(full_image[row - 1][0][9])[::-1]
      top_tile_id = first_ids_in_rows[row - 1]
      last_tile = _find_bottom_tile(top_tile_id, tiles, target_bottom_border)
      first_ids_in_rows.append(last_tile.tile_id)
      full_image.append([last_tile.image])
    for col in range(1, length_in_tiles):
      last_tile = _find_right_tile(last_tile.tile_id, tiles,
                                   last_tile.right_border)
      full_image[row].append(last_tile.image)
  return _remove_borders_and_join(full_image)


def _remove_borders_and_join(full_image: List[List[List[List[str]]]]) \
    -> List[List[str]]:
  result_length = len(full_image) * 8  # tile length without borders
  result = [['' for i in range(result_length)] for j in range(result_length)]
  for row in range(len(full_image)):
    for col in range(len(full_image[row])):
      tile = full_image[row][col]
      for x in range(len(tile)):
        for y in range(len(tile)):
          if x == 0 or x == 9 or y == 0 or y == 9:
            continue
          result[row * 8 + (x - 1)][col * 8 + (y - 1)] = tile[x][y]
  return result


def _find_bottom_tile(tile_id: int, tiles: List[Tile], target_bottom_border: str) -> Tile:
  for tile in tiles:
    if tile.tile_id == tile_id:
      continue
    if _matches_bottom_border(tile, target_bottom_border):
      return tile
  raise Exception('Did not find tile')


def _find_right_tile(tile_id: int, tiles: List[Tile], target_right_border: str) -> Tile:
  for tile in tiles:
    if tile.tile_id == tile_id:
      continue
    if _matches_right_border(tile, target_right_border):
      return tile
  raise Exception('Did not find tile')


def _matches_right_border(tile: Tile, target_right_border: str) -> bool:
  rotations = 0
  while rotations < 4:
    if tile.left_border[::-1] == target_right_border:
      return True
    tile.rotate_right()
    rotations += 1
  tile.vertical_flip()
  rotations = 0
  while rotations < 4:
    if tile.left_border[::-1] == target_right_border:
      return True
    tile.rotate_right()
    rotations += 1
  return False


def _matches_bottom_border(tile: Tile, target_bottom_border: str) -> bool:
  rotations = 0
  while rotations < 4:
    if tile.top_border[::-1] == target_bottom_border:
      return True
    tile.rotate_right()
    rotations += 1
  tile.vertical_flip()
  rotations = 0
  while rotations < 4:
    if tile.top_border[::-1] == target_bottom_border:
      return True
    tile.rotate_right()
    rotations += 1
  return False


def _position_top_left_tile(top_and_left: Tile, right_border: str, bottom_border: str) -> None:
  # First match right border
  rotations = 0
  while top_and_left.right_border != right_border:
    if rotations == 3:
      top_and_left.rotate_right()
      top_and_left.vertical_flip()
      rotations = 0
    else:
      top_and_left.rotate_right()
      rotations += 1

  if top_and_left.bottom_border != bottom_border:
    # It means that the image it upside-down. Flip horizontally.
    top_and_left.horizontal_flip()
  if top_and_left.bottom_border != bottom_border[::-1]:
    raise Exception('Could not position top-left tile')


def _find_matching_border(tile: Tile, other: Tile) -> str:
  for border in tile.get_borders():
    for other_border in other.get_borders() + other.get_flipped_borders():
      if border == other_border:
        return border
  raise Exception('No matching border was found')


def _find_tile(tiles: List[Tile], tile_id: int) -> Tile:
  return next((tile for tile in tiles if tile.tile_id == tile_id), None)


def _find_corners(tiles: List[Tile]) -> Tuple[int, int, int, int]:
  """
  Returns:
    Tile IDs of the 4 corners of the image.
  """
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
  return corners_ids[0], corners_ids[1], corners_ids[2], corners_ids[3]


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