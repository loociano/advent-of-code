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


def part_one(card_public_key: int, door_public_key: int, card_subject=7) -> int:
  """
  Returns:
    Encryption key
  """
  card_loop_size = find_loop_size(card_public_key, card_subject)
  return _calculate(door_public_key, card_loop_size)


def find_loop_size(public_key: int, subject_number=7) -> int:
  """
  Returns:
    Loop size.
  """
  loop_size = 1
  while True:
    if loop_size > public_key:
      raise Exception('Could not find loop size for: {}'.format(public_key))
    if _calculate(subject_number, loop_size) == public_key:
      return loop_size
    loop_size += 1


def _calculate(subject_number: int, loop_size: int) -> int:
  return int(pow(subject_number, loop_size, 20201227))
