class ShipWithWaypoint:
  def __init__(self):
    # Waypoint start coords: 1N,10E
    self._x = 10
    self._y = -1
    self._ship_x = 0
    self._ship_y = 0

  def manhattan_distance(self) -> int:
    return abs(self._ship_x) + abs(self._ship_y)

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
      self._turn_waypoint_left(int(instruction.split('L')[1]))
    elif 'R' in instruction:
      self._turn_waypoint_right(int(instruction.split('R')[1]))
    elif 'F' in instruction:
      steps = int(instruction.split('F')[1])
      self._ship_x += self._x * steps
      self._ship_y += self._y * steps
    else:
      raise Exception('Unrecognized instruction: {}'.format(instruction))

  def _turn_waypoint_left(self, deg: int) -> None:
    if deg == 90:
      x = self._x
      y = self._y
      self._x = y
      self._y = -x
    elif deg == 180:
      x = self._x
      y = self._y
      self._x = -x
      self._y = -y
    elif deg == 270:
      x = self._x
      y = self._y
      self._x = -y
      self._y = x
    else:
      raise Exception('Unsupported turn')

  def _turn_waypoint_right(self, deg: int) -> None:
    if deg == 90:
      x = self._x
      y = self._y
      self._x = -y
      self._y = x
    elif deg == 180:
      x = self._x
      y = self._y
      self._x = -x
      self._y = -y
    elif deg == 270:
      x = self._x
      y = self._y
      self._x = y
      self._y = -x
    else:
      raise Exception('Unsupported turn')