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
from typing import Sequence
from functools import cache
from collections import defaultdict

type ChangeSequence = tuple[int, int, int, int]

_SEQUENCE_LENGTH = 4


def _mix(secret_number: int, value: int) -> int:
  """Mixes a value and the secret number."""
  return secret_number ^ value


def _prune(secret_number: int) -> int:
  """Prunes the secret number."""
  return secret_number % 16777216


@cache
def _generate_secret_number(secret_number: int) -> int:
  result = secret_number
  result = _prune(_mix(result, result * 64))
  result = _prune(_mix(result, result // 32))
  return _prune(_mix(result, result * 2048))


def generate_secret_number(secret_number: int, times: int = 1) -> int:
  result = secret_number
  for _ in range(times):
    result = _generate_secret_number(result)
  return result


def sum_2000th_secret_numbers(secret_numbers: Sequence[str]) -> int:
  return sum(generate_secret_number(secret_number=int(secret_number), times=2000) for secret_number in secret_numbers)


def _generate_change_sequences(secret_number: int, times: int = 2000) -> dict[ChangeSequence, int]:
  sequence_to_bananas = defaultdict(int)
  change_sequence = list()
  last_one_digit = int(str(secret_number)[-1])
  for _ in range(times):
    secret_number = _generate_secret_number(secret_number)
    one_digit = int(str(secret_number)[-1])
    if len(change_sequence) == _SEQUENCE_LENGTH:
      change_sequence = change_sequence[1:]  # Shift left.
    change_sequence.append(one_digit - last_one_digit)
    last_one_digit = one_digit
    if len(change_sequence) == _SEQUENCE_LENGTH and sequence_to_bananas.get(tuple(change_sequence)) is None:
      # Only record first time seen after a sequence.
      sequence_to_bananas[tuple(change_sequence)] = last_one_digit
  return sequence_to_bananas


def find_max_bananas(secret_numbers: Sequence[str]) -> int:
  merged_sequences = defaultdict(int)
  # Brute force.
  for secret_number in secret_numbers:
    change_sequences = _generate_change_sequences(int(secret_number))
    for sequence, bananas in change_sequences.items():
      merged_sequences[sequence] = merged_sequences.get(sequence, 0) + bananas
  return max(merged_sequences.values())
