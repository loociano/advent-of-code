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
from typing import List

SEAT_ROWS = 128
SEAT_COLUMNS = 8


def part_one(boarding_pass_list: List[str]) -> int:
  max_seat_id = 0
  for boarding_pass in boarding_pass_list:
    seat_id = _calculate_seat_id(boarding_pass)
    if seat_id > max_seat_id:
      max_seat_id = seat_id
  return max_seat_id


def part_two(boarding_pass_list: List[str]) -> int:
  seats = [False] * SEAT_ROWS * SEAT_COLUMNS
  for boarding_pass in boarding_pass_list:
    seats[_calculate_seat_id(boarding_pass)] = True
  for i in range(0, len(seats)):
    if 0 < i < len(seats) - 1 \
        and seats[i - 1] and not seats[i] and seats[i + 1]:
      return i
  raise Exception('Seat not found.')


def _calculate_seat_id(boarding_pass: str) -> int:
  lower = 0
  upper = SEAT_ROWS - 1
  for i in range(0, 7):
    if boarding_pass[i] == 'F':
      upper = (lower + upper) // 2
    elif boarding_pass[i] == 'B':
      lower = (lower + upper) // 2 + 1
    else:
      raise Exception('Unrecognized: {}'.format(boarding_pass[i]))
  row = lower if boarding_pass[6] == 'F' else upper
  lower = 0
  upper = SEAT_COLUMNS - 1
  for j in range(7, 10):
    if boarding_pass[j] == 'L':
      upper = (lower + upper) // 2
    elif boarding_pass[j] == 'R':
      lower = (lower + upper) // 2 + 1
    else:
      raise Exception('Unrecognized: {}'.format(boarding_pass[j]))
  column = lower if boarding_pass[9] == 'L' else upper
  return row * SEAT_COLUMNS + column