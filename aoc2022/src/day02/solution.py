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
from typing import Sequence


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


def get_score(rounds: Sequence[str]) -> int:
  total = 0
  for a_round in rounds:
    opponent, you = a_round.split(' ')
    total += _get_round_score(opponent, you)
  return total
