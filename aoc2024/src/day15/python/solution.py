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
from typing import Sequence, override

type WarehouseMap = Sequence[Sequence[str]]
type Position = tuple[int, int]  # (x,y)
type Direction = tuple[int, int]  # (x,y)


class BaseWarehouse:
  _ROBOT = '@'
  _WALL = '#'
  _EMPTY = '.'
  _BOX = 'O'
  _DIR_TO_OPPOSITE = {
    (0, 1): (0, -1),  # Right to left.
    (0, -1): (0, 1),  # Left to right.
    (-1, 0): (1, 0),  # Up to down.
    (1, 0): (-1, 0),  # Down to up.
  }

  def __init__(self, warehouse_map: WarehouseMap, robot_moves: Sequence[Position]):
    self._warehouse_map: list[list[str]] = [list(line) for line in warehouse_map]
    self._width = len(self._warehouse_map[0])
    self._height = len(self._warehouse_map)
    self._robot_pos = self._find_robot_pos()
    self._robot_moves = robot_moves
    self._next_move_index = 0

  def simulate(self) -> None:
    """Simulates all robot moves in the warehouse."""
    while self._next_move_index < len(self._robot_moves):
      # self._print_map()
      self._move_robot()
      self._next_move_index += 1

  def sum_all_boxes_gps_coordinates(self) -> int:
    raise NotImplementedError()

  def _print_map(self) -> None:
    """Prints the warehouse map to stdout."""
    dir_map = {
      (-1, 0): '<',
      (1, 0): '>',
      (0, -1): '^',
      (0, 1): 'v',
    }
    for y in range(self._height):
      print(''.join(self._warehouse_map[y]))
    next_move = self._robot_moves[self._next_move_index]
    print(f'Move {dir_map.get(next_move)}')
    print('')

  def _find_robot_pos(self) -> Position:
    """Returns the position of the robot."""
    for y in range(self._height):
      for x in range(self._width):
        if self._warehouse_map[y][x] == self._ROBOT:
          return x, y
    raise ValueError('Robot not found!')

  def _move_robot(self) -> None:
    """Attempts to move robot one step. If the robot cannot move, it is a NOP."""
    next_move = self._robot_moves[self._next_move_index]
    next_pos = (self._robot_pos[0] + next_move[0], self._robot_pos[1] + next_move[1])
    if self._charAt(next_pos) == self._EMPTY:
      self._update(self._robot_pos, self._EMPTY)
      self._robot_pos = next_pos
      self._update(self._robot_pos, self._ROBOT)
    elif self._charAt(next_pos) in self._BOX:
      self._push(box_pos=next_pos, dir=next_move)
      if self._charAt(next_pos) == self._EMPTY:
        self._update(self._robot_pos, self._EMPTY)
        self._robot_pos = next_pos
        self._update(self._robot_pos, self._ROBOT)

  def _push(self, box_pos: Position, dir: Direction) -> None:
    raise NotImplementedError()

  def _charAt(self, pos: Position) -> str:
    """Returns what element is on the warehouse at a given position."""
    return self._warehouse_map[pos[1]][pos[0]]

  def _update(self, pos: Position, value: str) -> None:
    """Updates a warehouse position with a given element."""
    self._warehouse_map[pos[1]][pos[0]] = value

  def _within_bounds(self, pos: Position):
    """Returns true if a position is within warehouse bounds."""
    return 0 <= pos[0] < self._width and 0 <= pos[1] < self._height


class Warehouse(BaseWarehouse):
  @override
  def sum_all_boxes_gps_coordinates(self) -> int:
    """Returns the sum of all the boxes' GPS coordinates.
    A box GPS coordinate is 100 times its distance from the top edge of the
    warehouse plus its distance from the left edge of the map.
    """
    result = 0
    for y in range(self._height):
      for x in range(self._width):
        if self._charAt(pos=(x, y)) == self._BOX:
          result += 100 * y + x
    return result

  @override
  def _push(self, box_pos: Position, dir: Direction) -> None:
    """Attempts to push boxes from given position towards given direction.
    If there is no space to move boxes, it is a NOP."""
    next_empty_pos = self._find_next_empty_pos(box_pos, dir)
    if next_empty_pos is not None:
      next_pos = next_empty_pos
      while next_pos != box_pos:
        self._update(next_pos, self._BOX)
        opposite_dir = self._DIR_TO_OPPOSITE.get(dir)
        next_pos = (next_pos[0] + opposite_dir[0], next_pos[1] + opposite_dir[1])
      self._update(box_pos, self._EMPTY)

  def _find_next_empty_pos(self, pos: Position, dir: Direction) -> Position | None:
    """Returns the next empty space from a position towards a given direction."""
    while self._within_bounds(pos):
      if self._charAt(pos) == self._WALL:
        return None  # We hit a wall before an empty space.
      if self._charAt(pos) == self._EMPTY:
        return pos
      pos = (pos[0] + dir[0], pos[1] + dir[1])
    # Empty space was not found.
    return None


class DoubleWarehouse(BaseWarehouse):
  _BOX = '[]'

  def __init__(self, warehouse_map: WarehouseMap, robot_moves: Sequence[Position]):
    super().__init__(warehouse_map, robot_moves)
    self._resize_warehouse()
    self._width = len(self._warehouse_map[0])
    self._height = len(self._warehouse_map)
    self._robot_pos = self._find_robot_pos()
    self._robot_moves = robot_moves
    self._next_move_index = 0

  @override
  def sum_all_boxes_gps_coordinates(self) -> int:
    """Returns the sum of all the boxes' GPS coordinates.
    A box GPS coordinate is 100 times its distance from the top edge of the
    warehouse plus its distance from the left edge of the map.
    """
    result = 0
    for y in range(self._height):
      for x in range(self._width):
        if self._charAt(pos=(x, y)) == self._BOX[0]:
          result += 100 * y + x
    return result

  def _resize_warehouse(self):
    # Resize (double) the map.
    resized_map = []
    for y in range(self._height):
      line = []
      for x in range(self._width):
        value = self._charAt(pos=(x, y))
        resized_value = None
        if value == self._WALL:
          resized_value = self._WALL * 2
        if value == super()._BOX:
          resized_value = self._BOX
        if value == self._EMPTY:
          resized_value = self._EMPTY * 2
        if value == self._ROBOT:
          resized_value = self._ROBOT + self._EMPTY
        line.append(resized_value)
      resized_map.append(list(''.join(line)))
    self._warehouse_map = resized_map

  @override
  def _push(self, box_pos: Position, dir: Direction) -> None:
    if dir in ((-1, 0), (1, 0)):  # Boxes are 1-tile when moving horizontally.
      next_empty_pos = self._find_next_empty_x(box_pos, dir)
      if next_empty_pos is not None:
        line = ''.join(self._warehouse_map[box_pos[1]])
        if dir == (-1, 0):  # Shift box(es) left.
          shifted_left_line = (line[:next_empty_pos[0]]
                               + line[next_empty_pos[0] + 1:box_pos[0] + 1]
                               + self._EMPTY
                               + line[box_pos[0] + 1:])
          self._warehouse_map[box_pos[1]] = list(shifted_left_line)
        elif dir == (1, 0):  # Shift box(es) right
          shifted_right_line = (line[:box_pos[0]]
                                + self._EMPTY
                                + line[box_pos[0]:next_empty_pos[0]]
                                + line[next_empty_pos[0] + 1:])
          self._warehouse_map[box_pos[1]] = list(shifted_right_line)
    elif dir in ((0, -1), (0, 1)):  # Boxes are 2-tile when moving vertically.
      box_side = self._charAt(box_pos)
      if box_side == '[':
        if self._can_move_boxes_vertically(left_pos=box_pos, dir=dir):
          self._move_boxes_vertically(left_pos=box_pos, dir=dir)
      elif box_side == ']':
        left_pos = (box_pos[0] - 1, box_pos[1])
        if self._can_move_boxes_vertically(left_pos, dir):
          self._move_boxes_vertically(left_pos, dir)
      else:
        raise ValueError(f'pos={box_pos} not a box, was: {box_side}')
    else:
      raise ValueError(f'Unrecognized dir={dir}')

  def _can_move_boxes_vertically(self, left_pos: Position, dir: Direction) -> bool:
    """Returns true if all boxes can be moved given a box position."""
    behind_left_pos = left_pos[0] + dir[0], left_pos[1] + dir[1]
    behind_right_pos = (behind_left_pos[0] + 1, behind_left_pos[1])
    behind_value = self._charAt(behind_left_pos) + self._charAt(behind_right_pos)
    # Base case. If the last adjacent box is against a wall, no box moves.
    if behind_value == self._WALL * 2:
      return False
    if behind_value == self._EMPTY * 2:
      return True
    if behind_value == self._BOX:
      return self._can_move_boxes_vertically(left_pos=behind_left_pos, dir=dir)
    if behind_value == self._EMPTY + self._BOX[0]:
      # Touching left side of another box.
      return self._can_move_boxes_vertically(left_pos=(behind_left_pos[0] + 1, behind_left_pos[1]), dir=dir)
    if behind_value == self._BOX[1] + self._EMPTY:
      # Touching right side of another box.
      return self._can_move_boxes_vertically(left_pos=(behind_left_pos[0] - 1, behind_left_pos[1]), dir=dir)
    if behind_value == self._BOX[::-1]:  # 2 boxes behind!
      return (self._can_move_boxes_vertically(left_pos=(behind_left_pos[0] - 1, behind_left_pos[1]), dir=dir)
              and self._can_move_boxes_vertically(left_pos=(behind_left_pos[0] + 1, behind_left_pos[1]), dir=dir))

  def _move_boxes_vertically(self, left_pos: Position, dir: Direction) -> None:
    """Moves all boxes that can be moved in the y-axis given direction."""
    behind_left_pos = left_pos[0] + dir[0], left_pos[1] + dir[1]
    behind_right_pos = (behind_left_pos[0] + 1, behind_left_pos[1])
    behind_value = self._charAt(behind_left_pos) + self._charAt(behind_right_pos)
    # Base case.
    if behind_value == self._EMPTY * 2:
      self._move_box_vertically(left_pos, dir)
      return
    if behind_value == self._BOX:
      self._move_boxes_vertically(left_pos=behind_left_pos, dir=dir)
      self._move_box_vertically(left_pos, dir)
    if behind_value == self._EMPTY + self._BOX[0]:
      self._move_boxes_vertically(left_pos=(behind_left_pos[0] + 1, behind_left_pos[1]), dir=dir)
      self._move_box_vertically(left_pos, dir)
    if behind_value == self._BOX[1] + self._EMPTY:
      self._move_boxes_vertically(left_pos=(behind_left_pos[0] - 1, behind_left_pos[1]), dir=dir)
      self._move_box_vertically(left_pos, dir)
    if behind_value == self._BOX[::-1]:  # 2 boxes behind!
      self._move_boxes_vertically(left_pos=(behind_left_pos[0] - 1, behind_left_pos[1]), dir=dir)
      self._move_boxes_vertically(left_pos=(behind_left_pos[0] + 1, behind_left_pos[1]), dir=dir)
      self._move_box_vertically(left_pos, dir)

  def _move_box_vertically(self, left_pos: Position, dir: Direction) -> None:
    """Moves box given up or down."""
    behind_left_pos = left_pos[0] + dir[0], left_pos[1] + dir[1]
    behind_right_pos = (behind_left_pos[0] + 1, behind_left_pos[1])
    self._update(pos=behind_left_pos, value=self._BOX[0])
    self._update(pos=behind_right_pos, value=self._BOX[1])
    self._update(pos=left_pos, value=self._EMPTY)
    self._update(pos=(left_pos[0] + 1, left_pos[1]), value=self._EMPTY)

  def _find_next_empty_x(self, pos: Position, dir: Direction) -> Position | None:
    while self._within_bounds(pos):
      if self._charAt(pos) == self._WALL:
        return None  # We hit a wall before an empty space.
      if self._charAt(pos) == self._EMPTY:
        return pos
      pos = (pos[0] + dir[0], pos[1] + dir[1])
    # Empty space was not found.
    return None


def _parse(input: Sequence[str]) -> tuple[WarehouseMap, Sequence[Position]]:
  """Parses the input and returns the warehouse map and sequence of robot moves."""
  is_map = True
  warehouse_map = []
  robot_moves = []
  for line in input:
    if line == '':
      is_map = False
    if is_map:
      warehouse_map.append(line)
    else:
      for i in line:
        if i == '^':  # Up.
          robot_moves.append((0, -1))
        if i == '<':  # Left.
          robot_moves.append((-1, 0))
        if i == '>':  # Right.
          robot_moves.append((1, 0))
        if i == 'v':  # Down.
          robot_moves.append((0, 1))
  return tuple(warehouse_map), tuple(robot_moves)


def sum_all_boxes_gps_coordinates(input: Sequence[str], double_size=False) -> int:
  """Simulates all the robot moves in the warehouse and
  returns the sum of all boxes GPS coordinates at the end state."""
  warehouse_map, robot_moves = _parse(input)
  warehouse = DoubleWarehouse(warehouse_map, robot_moves) if double_size else Warehouse(warehouse_map, robot_moves)
  warehouse.simulate()
  return warehouse.sum_all_boxes_gps_coordinates()
