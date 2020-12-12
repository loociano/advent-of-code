class Ship:
  def __init__(self):
    self._x = 0
    self._y = 0
    self._dir_x = 0
    self._dir_y = 0
    self._point_east()

  def manhattan_distance(self) -> int:
    return abs(self._x) + abs(self._y)

  def navigate(self, instruction: str):
    if 'N' in instruction:
      self._y -= int(instruction.split('N')[1])
    elif 'S' in instruction:
      self._y += int(instruction.split('S')[1])
    elif 'E' in instruction:
      self._x += int(instruction.split('E')[1])
    elif 'W' in instruction:
      self._x -= int(instruction.split('W')[1])
    elif 'L' in instruction:
      self._turn_left(int(instruction.split('L')[1]))
    elif 'R' in instruction:
      self._turn_right(int(instruction.split('R')[1]))
    elif 'F' in instruction:
      steps = int(instruction.split('F')[1])
      self._x += self._dir_x * steps
      self._y += self._dir_y * steps
    else:
      raise Exception('Unrecognized instruction: {}'.format(instruction))

  def _point_west(self):
    self._dir_x = -1
    self._dir_y = 0

  def _point_north(self):
    self._dir_x = 0
    self._dir_y = -1

  def _point_south(self):
    self._dir_x = 0
    self._dir_y = 1

  def _point_east(self):
    self._dir_x = 1
    self._dir_y = 0

  def _turn_left(self, deg: int) -> None:
    if deg == 90:
      if self._dir_x == 1:  # east to north
        self._point_north()
      elif self._dir_y == -1:  # north to west
        self._point_west()
      elif self._dir_x == -1:  # west to south
        self._point_south()
      else:  # south to east
        self._point_east()
    elif deg == 180:
      if self._dir_x == 1:  # east to west
        self._point_west()
      elif self._dir_y == -1:  # north to south
        self._point_south()
      elif self._dir_x == -1:  # west to east
        self._point_east()
      else:  # south to north
        self._point_north()
    elif deg == 270:
      if self._dir_x == 1:  # east to south
        self._point_south()
      elif self._dir_y == -1:  # north to east
        self._point_east()
      elif self._dir_x == -1:  # west to north
        self._point_north()
      else:  # south to west
        self._point_west()
    else:
      raise Exception('Unsupported turn')

  def _turn_right(self, deg: int) -> None:
    if deg == 90:
      if self._dir_x == 1:  # east to south
        self._point_south()
      elif self._dir_y == -1:  # north to east
        self._point_east()
      elif self._dir_x == -1:  # west to north
        self._point_north()
      else:  # south to west
        self._point_west()
    elif deg == 180:
      if self._dir_x == 1:  # east to west
        self._point_west()
      elif self._dir_y == -1:  # north to south
        self._point_south()
      elif self._dir_x == -1:  # west to east
        self._point_east()
      else:  # south to north
        self._point_north()
    elif deg == 270:
      if self._dir_x == 1:  # east to north
        self._point_north()
      elif self._dir_y == -1:  # north to west
        self._point_west()
      elif self._dir_x == -1:  # west to south
        self._point_south()
      else:  # south to east
        self._point_east()
    else:
      raise Exception('Unsupported turn')