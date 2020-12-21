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
from typing import Tuple


class Tile:
  def __init__(self, tile_id: int, image: List[List[str]]):
    self.tile_id = tile_id
    self._image = image
    self._top_border = ''.join(self._image[0])
    self._right_border = ''.join([i[len(image) - 1] for i in self._image])
    self._bottom_border = ''.join(self._image[len(image) - 1])[::-1]
    self._left_border = ''.join([i[0] for i in self._image])[::-1]


  def get_borders(self) -> Tuple[str, str, str, str]:
    return self._top_border, self._right_border, self._bottom_border, \
           self._left_border

  def get_flipped_borders(self) -> Tuple[str, str, str, str]:
    return self._top_border[::-1], self._right_border[::-1], \
           self._bottom_border[::-1], self._left_border[::-1]