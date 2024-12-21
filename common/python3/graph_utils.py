"""Common graph utility functions."""
from collections import deque
from typing import Any, Callable
from common.python3.types import Direction, Position


def find(grid: list[list[str]], symbol: str) -> Position:
  """Returns the position of a symbol in the grid if found."""
  for y in range(len(grid)):
    for x in range(len(grid[0])):
      if grid[y][x] == symbol:
        return x, y
  raise ValueError(f'Symbol {symbol} not found.')


def char_at(grid: list[list[str]], pos: Position) -> str:
  """Returns the character at the position in the grid."""
  return grid[pos[1]][pos[0]]


def within_bounds(grid: list[list[str]], pos: Position) -> bool:
  return 0 <= pos[0] < len(grid[0]) and 0 <= pos[1] < len(grid)


def shortest_distance_bfs(grid: list[list[str]], visited: set[Position] = None,
                          start_pos: Position = (0, 0), end_pos: Position = None,
                          directions: tuple[Direction, ...] = ((0, -1), (1, 0), (0, 1), (-1, 0)),
                          predicate: Callable[[Any, ...], bool] = None) -> int:
  """Returns the shortest distance between two points in a grid.
  An optional predicate can be provided to detect obstacles:
  predicate=lambda x,y: grid[y][x] != OBSTACLE_CHAR
  """
  if visited is None:
    visited = set()
  if end_pos is None:
    end_pos = (len(grid[0]) - 1, len(grid) - 1)  # (x,y)
  queue = deque()
  queue.append((start_pos, 0))  # Append level.
  while queue:
    pos, level = queue.popleft()
    if pos == end_pos:
      return level
    for dxy in directions:
      next_pos = (pos[0] + dxy[0], pos[1] + dxy[1])
      if (next_pos not in visited
              and 0 <= next_pos[0] < len(grid[0])
              and 0 <= next_pos[1] < len(grid)
              and predicate(next_pos[0], next_pos[1])):
        visited.add(next_pos)
        queue.append((next_pos, level + 1))
  raise ValueError('Could not reach the exit.')
