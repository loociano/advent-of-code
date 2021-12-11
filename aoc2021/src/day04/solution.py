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
from typing import List, Sequence, Tuple

_BOARD_SIZE = 5


class BingoBoard:
    """Represents a bingo board of 5x5 numbers."""
    numbers: Sequence[Sequence[int]]
    marked: List[List[bool]]  # Mutable.

    def __init__(self, numbers: Sequence[Sequence[int]]) -> None:
        """Initializes a bingo board.
        Args:
            numbers: A 5x5 board of numbers.
        """
        self.numbers = numbers
        self.marked = [[False] * _BOARD_SIZE for _ in range(0, _BOARD_SIZE)]

    def _has_marked_row(self) -> bool:
        """Returns True if the board has one full marked row."""
        for row in self.marked:
            if row.count(False) == 0:
                return True
        return False

    def _has_marked_column(self) -> bool:
        """Returns True if the board has one full marked column."""
        for column_pos in range(0, _BOARD_SIZE):
            column = [row[column_pos] for row in self.marked]
            if column.count(False) == 0:
                return True
        return False

    def _is_winning(self) -> bool:
        """True if the board won."""
        return self._has_marked_row() or self._has_marked_column()

    def mark(self, drawing_number: int) -> bool:
        """Marks a number, if it exists, in the board.

        Args:
            drawing_number: A number. It may not appear in the board.
        Returns
            True if the board wins.
        """
        for i, row in enumerate(self.numbers):
            for j, board_number in enumerate(row):
                if board_number == drawing_number:
                    self.marked[i][j] = True
        return self._is_winning()

    def sum_unmarked(self) -> int:
        """Returns the sum of all numbers that have not been marked."""
        sum_unmarked = 0
        for i, row in enumerate(self.marked):
            for j, is_marked in enumerate(row):
                if not is_marked:
                    sum_unmarked += self.numbers[i][j]
        return sum_unmarked


def _parse_line(board_line: str) -> Sequence[int]:
    return tuple(int(x) for x in board_line.split(' ') if x)


def _parse_bingo(bingo: str) -> Tuple[Sequence[int], Sequence[BingoBoard]]:
    numbers = tuple(map(int, bingo[0].split(',')))
    boards = []
    cursor = 2  # Skip first line and separator.
    while cursor < len(bingo) - _BOARD_SIZE + 1:
        board_numbers = tuple(_parse_line(bingo[i]) for i in
                              range(cursor, cursor + _BOARD_SIZE))
        boards.append(BingoBoard(board_numbers))
        cursor += _BOARD_SIZE + 1  # Skip empty line separating boards.
    return numbers, tuple(boards)


def part_one(bingo: str) -> int:
    """AOC 2021 Day 4 Part 1.

    Args:
        bingo: The bingo input. First line contains comma-separated numbers to
        be drawn, next lines contain 5x5 bingo boards.
    Returns:
      Score of the winning board. It is the sum of all unmarked numbers on that
      board multiplied by the number last called.
    """
    drawing_numbers, boards = _parse_bingo(bingo)
    for drawing_number in drawing_numbers:
        for board in boards:
            if board.mark(drawing_number=drawing_number):
                return drawing_number * board.sum_unmarked()
    raise Exception('No board won!')


def part_two(bingo: str) -> int:
    """AOC 2021 Day 4 Part 2.

    Args:
        bingo: The bingo input. First line contains comma-separated numbers to
        be drawn, next lines contain 5x5 bingo boards.
    Returns:
      Score of the last winning board. It is the sum of all unmarked numbers on
      that board multiplied by the number last called.
    """
    drawing_numbers, boards = _parse_bingo(bingo)
    winning_boards = [False] * len(boards)
    for drawing_number in drawing_numbers:
        for board_no, board in enumerate(boards):
            if board.mark(drawing_number=drawing_number):
                winning_boards[board_no] = True
                if winning_boards.count(False) == 0:  # Last winning board.
                    return drawing_number * board.sum_unmarked()
    raise Exception('No board won!')
