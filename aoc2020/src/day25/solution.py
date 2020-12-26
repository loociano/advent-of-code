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


def part_one(card_public_key: int, door_public_key: int) -> int:
  """
  Args:
    card_public_key: card's public key
    door_public_key: door's public key
  Returns:
    Encryption key.
  """
  card_loop_size = find_loop_size(card_public_key)
  door_loop_size = find_loop_size(door_public_key)
  encryption_key = _calculate(door_public_key, card_loop_size)
  assert _calculate(card_public_key, door_loop_size) == encryption_key
  return encryption_key


def find_loop_size(public_key: int) -> int:
  """
  Finds the number of loops required to generate a public key with subject
  number 7.
  Args:
    public_key: an integer representing a public key.
  Returns:
    Number of loops.
  """
  subject_number = 7
  value = 1
  loop_size = 1
  while True:
    # Faster approach; instead of calling calculate()
    # https://github.com/r0f1/adventofcode2020/blob/master/day25/main.py
    value = (value * subject_number) % 20201227
    if value == public_key:
      return loop_size
    loop_size += 1


def _calculate(subject_number: int, loop_size: int) -> int:
  return int(pow(subject_number, loop_size, 20201227))
