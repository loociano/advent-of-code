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
from abc import abstractmethod
from dataclasses import dataclass
from typing import Sequence, Tuple


def _parse(instruction: str) -> Tuple[str, int]:
    """Parses an instruction.
    Args:
        instruction: A raw input instruction.
    Returns:
        command and command value.
    """
    command, value = instruction.split(' ')
    # TODO: handle incorrect instructions.
    if not command:
        raise ValueError('Missing command!')
    if not value:
        raise ValueError('Missing value!')
    return command, int(value)


@dataclass
class Submarine:
    """Represents a generic submarine."""
    horizontal_position: int = 0
    depth: int = 0

    @abstractmethod
    def execute(self, instruction: str) -> None:
        pass


@dataclass
class PartOneSubmarine(Submarine):
    """Submarine that follows specs from part two   ."""

    def execute(self, instruction: str) -> None:
        """Executes an instruction.
        Args:
            instruction: A raw input instruction.
        """
        command, value = _parse(instruction=instruction)
        if command == 'forward':
            self.horizontal_position += value
        elif command == 'down':
            self.depth += value
        elif command == 'up':
            self.depth -= value
        else:
            raise ValueError(f'Unrecognized command {command}.')


@dataclass
class PartTwoSubmarine(Submarine):
    """Submarine that follows specs from part one."""
    aim: int = 0

    def execute(self, instruction: str) -> None:
        """Executes an instruction.
        Args:
            instruction: A raw input instruction.
        """
        command, value = _parse(instruction=instruction)
        if command == 'forward':
            self.horizontal_position += value
            self.depth += self.aim * value
        elif command == 'down':
            self.aim += value
        elif command == 'up':
            self.aim -= value
        else:
            raise ValueError(f'Unrecognized command {command}.')


def _run(planned_course: Sequence[str], submarine: Submarine) -> int:
    """Runs the planned course and computes result.

    Returns:
      Final horizontal position multiplied by final depth.
    """
    for instruction in planned_course:
        submarine.execute(instruction=instruction)
    return submarine.horizontal_position * submarine.depth


def part_one(planned_course: Sequence[str]) -> int:
    """AOC 2021 Day 2 Part 1.

    Args:
      planned_course: sequence of instructions:
      - 'forward X' increases the horizontal position by X units.
      - 'down X' increases the depth by X units.
      - 'up X' decreases the depth by X units.
    Returns:
      Final horizontal position multiplied by final depth.
    """
    return _run(planned_course=planned_course, submarine=PartOneSubmarine())


def part_two(planned_course: Sequence[str]) -> int:
    """AOC 2021 Day 2 Part 2.

    Args:
      planned_course: sequence of instructions:
      - 'forward X' increases horizontal position by X units and increases depth
       by the aim multiplied by X.
      - 'down X' increases aim by X units.
      - 'up X' decreases aim by X units.
    Returns:
      Final horizontal position multiplied by final depth.
    """
    return _run(planned_course=planned_course, submarine=PartTwoSubmarine())
