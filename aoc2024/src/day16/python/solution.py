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
from math import inf
from typing import Sequence
from collections import deque, defaultdict
from dataclasses import dataclass, field

type Position = tuple[int, int]  # (x,y)
type Direction = tuple[int, int]  # (dx,dy) where -1 <= dx,dy <= 1.
_START = 'S'
_END = 'E'
_WALL = '#'
_SPACE = '.'
_MOVE_POINTS = 1
_TURN_POINTS = 1000
_TURN_RIGHT_MAP = {
  (0, -1): (1, 0),
  (1, 0): (0, 1),
  (0, 1): (-1, 0),
  (-1, 0): (0, -1),
}
_TURN_LEFT_MAP = {v: k for k, v in _TURN_RIGHT_MAP.items()}


def _charAt(maze: Sequence[str], pos: Position) -> str:
  return maze[pos[1]][pos[0]]


@dataclass
class Node:
  pos: Position
  dir: Direction
  score: int = 0
  path: set[Position] = field(default_factory=set)


def _bfs(maze: Sequence[str], start_pos: Position, start_dir: Direction, end_pos: Position) -> int:
  """Returns the minimum score from start position and direction to end position.
  A step has a score of 1 and a 90-degree turn has a score of 1000.
  """
  min_score_at = defaultdict(int)
  queue = deque()
  queue.append(Node(pos=start_pos, dir=start_dir))
  while len(queue):
    curr = queue.popleft()
    current_score = curr.score + _MOVE_POINTS
    if _charAt(maze, curr.pos) != _WALL:
      left_dir = _TURN_LEFT_MAP.get(curr.dir)
      right_dir = _TURN_RIGHT_MAP.get(curr.dir)
      neighbours = (
        Node(pos=(curr.pos[0] + curr.dir[0], curr.pos[1] + curr.dir[1]),
             dir=curr.dir,
             score=current_score),
        Node(pos=(curr.pos[0] + left_dir[0], curr.pos[1] + left_dir[1]),
             dir=left_dir,
             score=current_score + _TURN_POINTS),
        Node(pos=(curr.pos[0] + right_dir[0], curr.pos[1] + right_dir[1]),
             dir=right_dir,
             score=current_score + _TURN_POINTS),
      )
      for neighbour in neighbours:
        if neighbour.pos not in min_score_at or current_score < min_score_at[neighbour.pos]:
          min_score_at[neighbour.pos] = current_score
          if neighbour.pos != end_pos:
            queue.append(neighbour)
  return min_score_at[end_pos]


def _get_unique_tiles_bfs(maze: Sequence[str], start_pos: Position, start_dir: Direction, end_pos: Position,
                          min_score: int) -> int:
  """Returns the number of unique positions from all the best paths.
  The best paths are those with the given minimum score."""
  tiles: set[Position] = set()
  # Track visited "nodes" and their score.
  # Node is not hashable because it contains a mutable set().
  scores_at: dict[tuple[Position, Direction], int] = defaultdict(lambda: 100000000)
  queue = deque()
  start_path: set[Position] = set()
  start_path.add(start_pos)
  queue.append(Node(pos=start_pos, dir=start_dir, path=start_path))
  while queue:
    curr = queue.popleft()
    if curr.score <= scores_at[(curr.pos, curr.dir)] and curr.score <= min_score:
      scores_at[(curr.pos, curr.dir)] = curr.score
      if curr.pos == end_pos and curr.score == min_score:
        # Found one of the best paths. Save their tiles.
        tiles.update(curr.path)
      else:
        # Try moving one step in the same direction.
        ahead_pos = (curr.pos[0] + curr.dir[0], curr.pos[1] + curr.dir[1])
        if _charAt(maze, ahead_pos) != _WALL:
          new_path = curr.path.copy()
          new_path.add(ahead_pos)
          queue.append(Node(pos=ahead_pos, dir=curr.dir, score=curr.score + _MOVE_POINTS, path=new_path))
        # Try turning left:
        left_dir = _TURN_LEFT_MAP.get(curr.dir)
        queue.append(Node(pos=curr.pos, dir=left_dir, score=curr.score + _TURN_POINTS, path=curr.path.copy()))
        # Try turning right:
        right_dir = _TURN_RIGHT_MAP.get(curr.dir)
        queue.append(Node(pos=curr.pos, dir=right_dir, score=curr.score + _TURN_POINTS, path=curr.path.copy()))
  return len(tiles)


def _find_pos(maze: Sequence[str], value: str) -> Position:
  """Finds the starting position represented by char 'S' in the maze."""
  for y in range(len(maze)):
    for x in range(len(maze[0])):
      if _charAt(maze=maze, pos=(x, y)) == value:
        return x, y
  raise ValueError(f'value={value} not found in maze!')


def get_min_score(maze: Sequence[str]) -> int:
  """Returns the minimum score from the start to the end position of the maze."""
  start_pos = _find_pos(maze, _START)
  end_pos = _find_pos(maze, _END)
  start_dir = (1, 0)  # Right (East).
  # DFS with recursion causes stack overflow.
  return _bfs(maze=maze, start_pos=start_pos, start_dir=start_dir, end_pos=end_pos)


def get_total_tiles_in_best_paths(maze: Sequence[str]) -> int:
  """Returns the number of tiles that are part of at least one of the best paths through the maze."""
  start_pos = _find_pos(maze, _START)
  end_pos = _find_pos(maze, _END)
  start_dir = (1, 0)  # Right (East).
  min_score = get_min_score(maze)
  return _get_unique_tiles_bfs(maze=maze,
                               start_pos=start_pos, start_dir=start_dir,
                               end_pos=end_pos, min_score=min_score)
