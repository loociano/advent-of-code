# Copyright 2020 Google LLC
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
from typing import Union, Dict, Tuple


class Cup:
  def __init__(self, label: int):
    self.label = label
    self.next = None  # type:Union[None, Cup]


def part_one(start_cups: str, moves: int) -> str:
  """
  Returns:
    Labels on cups after cup one.
  """
  cups, first_cup = _parse_input(start_cups)
  cup = _play_game(cups, first_cup, moves)
  result = []
  for _ in range(len(cups) - 1):
    cup = cup.next
    result.append(str(cup.label))
  return ''.join(result)


def part_two(start_cups: str, moves: int) -> int:
  """
  Returns:
    Product of two cups situated clockwise immediately after cup 1.
  """
  cups, first_cup = _parse_input(start_cups)
  last_cup = cups[int(start_cups[-1])]
  # Break loop
  last_cup.next = None
  # Insert cups until reaching cup one million.
  for label in range(len(cups) + 1, 1000001):
    cup = Cup(label)
    cups[label] = cup
    last_cup.next = cup
    last_cup = cup
  # Link last cup to first cup.
  last_cup.next = first_cup
  cup1 = _play_game(cups, first_cup, moves)
  return cup1.next.label * cup1.next.next.label


def _parse_input(start_cups: str) -> Tuple[Dict[int, Cup], Cup]:
  mem = {}
  last_cup = None
  # Create cups and link them.
  for label in list(map(int, list(start_cups))):
    cup = Cup(label)
    if last_cup:
      last_cup.next = cup
    last_cup = cup
    mem[label] = cup
  # Link last cup to first cup.
  first_cup = mem[int(start_cups[0])]
  last_cup.next = first_cup
  return mem, first_cup

def _play_game(cups: Dict[int, Cup], current_cup: Cup, moves: int) -> Cup:
  """
  Plays game for a number of moves.
  Args:
    cups: index of cups.
    current_cup: starting cup
    moves: game turns
  Returns:
    Cap labeled 1.
  """
  for _ in range(moves):
    # Extract 3 cups after current cup
    first_picked_cup = current_cup.next
    right_cup = first_picked_cup
    picked_labels = []
    for _ in range(3):
      picked_labels.append(right_cup.label)
      right_cup = right_cup.next
    current_cup.next = right_cup

    # Find destination cup
    destination_label = current_cup.label - 1 \
      if current_cup.label > 1 else len(cups)
    while destination_label in picked_labels:
      destination_label -= 1
      if destination_label == 0:
        destination_label = len(cups)
    destination_cup = cups[destination_label]

    # Re-insert picked cups
    first_picked_cup.next.next.next = destination_cup.next
    destination_cup.next = first_picked_cup

    # Update current
    current_cup = current_cup.next
  return cups[1]
