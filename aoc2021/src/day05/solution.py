# Copyright 2021 Google LLC
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
from typing import Sequence, List, Tuple


class Segment:
    x1: int
    y1: int
    x2: int
    y2: int

    def __init__(self, x1: int, y1: int, x2: int, y2: int) -> None:
        """Initializes segment."""
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def is_horizontal(self) -> bool:
        return self.y1 == self.y2

    def is_vertical(self) -> bool:
        return self.x1 == self.x2

    def is_ascending_diagonal(self):
        return not self.is_vertical() and not self.is_horizontal() and self.x1 < self.x2

    def is_descending_diagonal(self):
        return not self.is_vertical() and not self.is_horizontal() and self.x2 > self.x1


class Grid:
    grid: List[List[int]]

    def __init__(self, width: int):
        """Initializes the grid."""
        self.grid = [[0] * width for _ in range(0, width)]

    def populate_horizontal(self, x_start: int, x_end: int,
                            y: int) -> None:
        for x in range(x_start, x_end + 1):
            self.grid[y][x] += 1

    def populate_vertical(self, y_start: int, y_end: int,
                          x: int) -> None:
        for y in range(y_start, y_end + 1):
            self.grid[y][x] += 1

    def populate_diagonal(self, x_start: int, x_end: int, y_start: int,
                          y_end: int):
        if x_start < x_end and y_start < y_end:
            # Descending onwards.
            y = y_start
            for x in range(x_start, x_end + 1):
                self.grid[y][x] += 1
                y += 1
        elif x_start > x_end and y_end < y_start:
            # Descending backwards.
            y = y_end
            for x in range(x_end, x_start + 1):
                self.grid[y][x] += 1
                y += 1
        elif x_start < x_end and y_end < y_start:
            # Ascending onwards.
            y = y_start
            for x in range(x_start, x_end + 1):
                self.grid[y][x] += 1
                y -= 1
        elif x_start > x_end and y_start < y_end:
            # Ascending backwards.
            y = y_end
            for x in range(x_end, x_start + 1):
                self.grid[y][x] += 1
                y -= 1
        else:
            raise ValueError('Not a diagonal?')

    def count_overlap_points(self) -> int:
        total = 0
        for row in self.grid:
            total += sum(value > 1 for value in row)
        return total


def _process_input(segment_lines: str) -> Tuple[Sequence[Segment], int]:
    segments = []
    max_position = -1
    # Process input.
    for line in segment_lines:
        start, end = line.split(' -> ')
        x1, y1 = map(int, start.split(','))
        x2, y2 = map(int, end.split(','))
        segments.append(Segment(x1=x1, y1=y1, x2=x2, y2=y2))
        # Determine grid width.
        if x1 > max_position:
            max_position = x1
        if y1 > max_position:
            max_position = y1
        if x2 > max_position:
            max_position = x2
        if y2 > max_position:
            max_position = y2
    return tuple(segments), max_position


def part_one(segment_lines: str) -> int:
    """AOC 2021 Day 5 Part 1.

    Part 1 only considers horizontal and vertical segments.

    Args:
        segment_lines: List of segments with format x1,y1 -> x2,y2.
    Returns:
        Number of points where at least 2 segments overlap.
    """
    segments, max_position = _process_input(segment_lines=segment_lines)
    grid = Grid(width=max_position + 1)  # Index between 0 and max_position.
    for segment in segments:
        if segment.is_horizontal():
            grid.populate_horizontal(x_start=min(segment.x1, segment.x2),
                                     x_end=max(segment.x1, segment.x2),
                                     y=segment.y1)
        elif segment.is_vertical():
            grid.populate_vertical(y_start=min(segment.y1, segment.y2),
                                   y_end=max(segment.y1, segment.y2),
                                   x=segment.x1)
    return grid.count_overlap_points()


def part_two(segment_lines: str) -> int:
    """AOC 2021 Day 4 Part 2.

    Args:
        segment_lines: List of segments with format x1,y1 -> x2,y2.
    Returns:
        Number of points where at least 2 segments overlap.
    """
    segments, max_position = _process_input(segment_lines=segment_lines)
    grid = Grid(width=max_position + 1)  # Index between 0 and max_position.
    for segment in segments:
        if segment.is_horizontal():
            grid.populate_horizontal(x_start=min(segment.x1, segment.x2),
                                     x_end=max(segment.x1, segment.x2),
                                     y=segment.y1)
        elif segment.is_vertical():
            grid.populate_vertical(y_start=min(segment.y1, segment.y2),
                                   y_end=max(segment.y1, segment.y2),
                                   x=segment.x1)
        else:
            # Must be diagonal.
            grid.populate_diagonal(x_start=segment.x1, x_end=segment.x2,
                                   y_start=segment.y1, y_end=segment.y2)
    return grid.count_overlap_points()
