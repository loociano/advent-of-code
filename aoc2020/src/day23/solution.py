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


def part_one(start_cups: str, moves: int) -> str:
  """
  Returns:
    Labels on cups after cup one.
  """
  cups = list(map(int, list(start_cups)))
  move = 0
  current_cup = cups[0]
  while move < moves:
    # Extract 3 cups after current cup
    pos_curr = cups.index(current_cup)
    left_cups = cups[:pos_curr + 1]
    right_cups = cups[pos_curr + 1:]
    picked = 0
    picked_cups = []
    while picked < 3:
      if len(right_cups):
        picked_cups.append(right_cups.pop(0))
      else:
        picked_cups.append(left_cups.pop(0))
      picked += 1
    if current_cup > 1:
      destination_cup = current_cup - 1
    else:
      destination_cup = 9
    cups = left_cups + right_cups

    # Find destination cup
    while destination_cup in picked_cups:
      destination_cup -= 1
      if destination_cup == 0:
        destination_cup = 9
    pos_destination_cup = cups.index(destination_cup)

    # Re-insert picked cups
    left_cups = cups[:pos_destination_cup + 1]
    right_cups = cups[pos_destination_cup + 1:]
    cups = left_cups + picked_cups + right_cups
    current_cup_pos = cups.index(current_cup)
    if current_cup_pos < len(cups) - 1:
      current_cup = cups[current_cup_pos + 1]
    else:
      current_cup = cups[0]
    move += 1
  cup_one_pos = cups.index(1)
  return ''.join(str(i) for i in cups[cup_one_pos + 1:] + cups[:cup_one_pos])
