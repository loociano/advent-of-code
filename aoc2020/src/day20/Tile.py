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
from typing import Tuple, List


class Tile:
  def __init__(self, tile_id: int, image: List[List[str]]):
    self.tile_id = tile_id
    self.image = image
    self._calculate_borders()

  def _calculate_borders(self):
    self.top_border = ''.join(self.image[0])
    self.right_border = ''.join([i[len(self.image) - 1] for i in self.image])
    self.bottom_border = ''.join(self.image[len(self.image) - 1])[::-1]
    self.left_border = ''.join([i[0] for i in self.image])[::-1]

  def get_borders(self) -> Tuple[str, str, str, str]:
    return self.top_border, self.right_border, self.bottom_border, \
           self.left_border

  def get_flipped_borders(self) -> Tuple[str, str, str, str]:
    return self.top_border[::-1], self.right_border[::-1], \
           self.bottom_border[::-1], self.left_border[::-1]

  def rotate_clockwise(self, degrees: int):
    if degrees == 90:
      self.rotate_right()
    elif degrees == 180:
      self.rotate_right()
      self.rotate_right()
    elif degrees == 270:
      self.rotate_right()
      self.rotate_right()
      self.rotate_right()
    else:
      raise Exception('Unsupported rotation')


  def rotate_right(self) -> None:
    """
    Rotates 90 degrees to the right, in place
    """
    self.image = list(list(dot)[::-1] for dot in zip(*self.image))
    self._calculate_borders()

  def vertical_flip(self) -> None:
    """
    Mirrors image vertically, in place.
    """
    for line in self.image:
      line.reverse()
    self._calculate_borders()

  def horizontal_flip(self) -> None:
    """
    Mirrors image horizontally, in place.
    """
    self.vertical_flip()
    self.rotate_clockwise(180)