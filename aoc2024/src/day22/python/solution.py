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
