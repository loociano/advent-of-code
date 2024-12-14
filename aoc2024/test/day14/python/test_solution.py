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
import unittest

from common.python3.AdventOfCodeTestCase import AdventOfCodeTestCase
from aoc2024.src.day14.python.solution import get_safety_factor, get_seconds_to_easter_egg


class TestSolution(AdventOfCodeTestCase):
  def __init__(self, *args, **kwargs):
    (super(TestSolution, self).__init__(__file__, *args,
                                        **kwargs))

  def test_part1_withExample_correct(self):
    self.assertEqual(12, get_safety_factor(self.examples[0],
                                           world_size=(11, 7), elapsed_seconds=100))

  def test_part1_withPuzzleInput_correct(self):
    self.assertEqual(215987200, get_safety_factor(self.input, elapsed_seconds=100))

  def test_part2_withPuzzleInput_correct(self):
    self.assertEqual(8050, get_seconds_to_easter_egg(self.input, elapsed_seconds=10000))
    """
  t=8050
  .....................................................................................................
  ............X........................................................................................
  ............................................................................................X........
  ......X.........................................................X....................................
  ................X....................................................................................
  .........................X........................................................X..................
  .............................X.......................................................................
  ...........................................................X.........................................
  X....................................................................................................
  ...................................X.........................................................X.......
  ...................................................X.................................................
  .............................................................................................X.......
  ......................X.................................X............................................
  ..X......................................................................................X...........
  .....................................................................................................
  .......X.........................X...................................................................
  .....................................................................................................
  ......................................XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX................................
  ...........X..........................X.............................X................................
  ......................................X.............................X................................
  ......................................X.............................X..X....X........................
  ........X.............................X.............................X...........................X....
  ......................................X..............X..............X....................X...........
  .......................X..............X.............XXX.............X................................
  ......................................X............XXXXX............X........X.......................
  ......................................X...........XXXXXXX...........X................................
  .....X................................X..........XXXXXXXXX..........X................................
  ......................................X............XXXXX............X......X.........................
  ......................................X...........XXXXXXX...........X................................
  X.....................................X..........XXXXXXXXX..........X................................
  ......................................X.........XXXXXXXXXXX.........X....X...........................
  ......X...........X...................X........XXXXXXXXXXXXX........X...................X..X.........
  ......................................X..........XXXXXXXXX..........X................................
  .X....................................X.........XXXXXXXXXXX.........X.....X.X...................X....
  ......................................X........XXXXXXXXXXXXX........X................................
  ........X...........X.................X.......XXXXXXXXXXXXXXX.......X...............X................
  .......X.......X......................X......XXXXXXXXXXXXXXXXX......X................................
  ............................X.........X........XXXXXXXXXXXXX........X......................X....X....
  ..............X.......................X.......XXXXXXXXXXXXXXX.......X................................
  ........................X.............X......XXXXXXXXXXXXXXXXX......X....................X...........
  X.X...................................X.....XXXXXXXXXXXXXXXXXXX.....X...X............................
  ......................................X....XXXXXXXXXXXXXXXXXXXXX....X...........X....................
  ..............................X.......X.............XXX.............X.X..............................
  ......................................X.............XXX.............X................................
  ......................................X.............XXX.............X.................X..............
  ..................X.......X....X......X.............................X................................
  ......................................X.............................X................................
  ......................................X.............................X.........X.....X................
  ......................................X.............................X................................
  ......................................XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX................................
  .......X...................................................................................X.........
  ...........................................................X.........................................
  ...X................................................................X................................
  ................................................................................X....................
  .....................................................................................................
  ...X.................................................................................................
  ...........................X.........................................................................
  .......................................................................X.............................
  ..............X.........X......................................X..................X..................
  .....................................................................................X..X.......X....
  ....................X................................................................................
  .....................................................................................................
  ................................................................................................X....
  ...........X.........................................................................................
  .......................X............................X.X..............................................
  .....................................................................................................
  ..................................................X.X..........................X.....................
  ...............X......................................................X..............................
  X...................................................................................X................
  ...................................................X......................................X..........
  ...............................................X.....................................................
  .................................................................X...................................
  .........X......................X.X...............X.................................X................
  .....................................................................................................
  .X...................................................................................................
  ...........................................X.........X...............................................
  ..............X...........................X........................................................X.
  .....................................................................................................
  ........................................X.................X..........................................
  .....................................................................................................
  ................................................................X....................................
  ............................................X.................X.............X.....X..........X.......
  .....................................................X...............................................
  ..................X......................X.......X....................X..............................
  ...............................................................X..............X.........X............
  .......X....................................................................................X........
  ...............X......................................................................X..............
  .................................................................X...................................
  ................................................X....................................................
  .....................................................................................................
  ......X............................................X.................................................
  ...............................................................X......X..............................
  .....................................................................................................
  .....................................................................................................
  .....................................................................................................
  .............X........X..............................................................................
  ................................................................................................X....
  .....................................................................................................
  ...X...................X.......................X..............................................X......
  .......................................................................X.............................
  ...........................................................X.........................................
  .......X.................X.....................................................X......X..............
  .........................................................X...........................................
  """


if __name__ == '__main__':
  unittest.main()
