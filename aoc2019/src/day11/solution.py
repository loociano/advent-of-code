# Copyright 2019 Google LLC
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
from aoc2019.src.common.intcode import Intcode, read_intcode


class RobotGrid:
  grid = {}
  robot_pos = tuple([0, 0])
  dirs = [[0, -1], [1, 0], [0, 1], [-1, 0]]  # up, right, down, left
  dir_index = 0

  def __init__(self, grid):
    self.grid = grid

  def get_panel_color(self) -> int:
    return int(self.grid.get(self.robot_pos, 0))

  def paint_panel(self, color: int) -> bool:
    newly_painted = self.grid.get(self.robot_pos) is None
    self.grid[self.robot_pos] = color
    return newly_painted

  def move_robot(self, next_dir: int):
    if next_dir == 1:  # turn right 90 degrees
      self.dir_index += 1
    elif next_dir == 0:  # turn left 90 degrees
      self.dir_index -= 1
    dir_vector = self.dirs[self.dir_index % len(self.dirs)]
    self.robot_pos = tuple([self.robot_pos[0] + dir_vector[0], self.robot_pos[1] + dir_vector[1]])


def _print_hull(hull: list):
  hull_str = []
  for row in hull:
    hull_str.append(''.join(row))
  return '\n'.join(hull_str)


def part_one(program: str, grid=None):
  if grid is None:
    grid = {}
  vm = Intcode(read_intcode(program))
  robot_grid = RobotGrid(grid)
  painted_count = 0
  while True:
    curr_color = robot_grid.get_panel_color()
    vm.set_input(curr_color)
    color = vm.run()
    if color is None:
      break
    painted_count += 1 if robot_grid.paint_panel(color) else 0
    vm.set_input(curr_color)
    robot_grid.move_robot(vm.run())
  return painted_count


def part_two(program: str):
  grid = {tuple([0, 0]): 1}  # starting panel is white
  grid_max_width = part_one(program, grid)
  hull = [[' '] * grid_max_width for i in range(0, grid_max_width)]

  origin_x, origin_y = grid_max_width // 2, grid_max_width // 2
  for key, value in grid.items():
    if value == 1:
      hull[origin_y + key[1]][origin_x + key[0]] = '█'
  return _print_hull(hull)
