# Copyright 2022 Google LLC
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
from typing import Callable, Sequence

_SCORE_TABLE = [
  [3, 6, 0],  # Rock:Rock, Rock:Paper, Rock:Scissors
  [0, 3, 6],  # Paper:Rock, Paper:Paper, Paper:Scissors
  [6, 0, 3]  # Scissors:Rock, Scissors:Paper, Scissors:Scissors
]

_SHAPE_SCORE = {
  'X': 1,
  'Y': 2,
  'Z': 3
}

_SCORE_TABLE2 = [
  [3, 1, 2],  # Rock:Lose, Rock:Draw, Rock:Win
  [1, 2, 3],  # Paper:Lose, Paper:Draw, Paper:Win
  [2, 3, 1]  # Scissors:Lose, Scissors:Draw, Scissors:Win
]


def _play_round(opponent: str, you: str) -> int:
  if opponent == 'A':
    i = 0
  elif opponent == 'B':
    i = 1
  else:
    i = 2
  if you == 'X':
    j = 0
  elif you == 'Y':
    j = 1
  else:
    j = 2
  return _SCORE_TABLE[i][j]


def _get_round_score(opponent: str, you: str) -> int:
  return _play_round(opponent, you) + _SHAPE_SCORE[you]


def _get_round_score2(opponent: str, you: str) -> int:
  if opponent == 'A':
    i = 0
  elif opponent == 'B':
    i = 1
  else:
    i = 2
  if you == 'X':
    j = 0
    result_score = 0  # Lose.
  elif you == 'Y':
    j = 1
    result_score = 3  # Draw.
  else:
    j = 2
    result_score = 6  # Win.
  return _SCORE_TABLE2[i][j] + result_score


def _get_score(rounds: Sequence[str],
               score_fn: Callable[[str, str], int]) -> int:
  total = 0
  for a_round in rounds:
    opponent, you = a_round.split(' ')
    total += score_fn(opponent, you)
  return total


def get_score(rounds: Sequence[str]) -> int:
  return _get_score(rounds, _get_round_score)


def get_score2(rounds: Sequence[str]) -> int:
  return _get_score(rounds, _get_round_score2)
