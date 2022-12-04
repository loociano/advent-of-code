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
from typing import Dict, Sequence

_SCORE_TABLE = [
  [3, 6, 0],  # Rock:Rock, Rock:Paper, Rock:Scissors
  [0, 3, 6],  # Paper:Rock, Paper:Paper, Paper:Scissors
  [6, 0, 3]  # Scissors:Rock, Scissors:Paper, Scissors:Scissors
]

_SCORE_TABLE2 = [
  [3, 1, 2],  # Rock:Lose, Rock:Draw, Rock:Win
  [1, 2, 3],  # Paper:Lose, Paper:Draw, Paper:Win
  [2, 3, 1]  # Scissors:Lose, Scissors:Draw, Scissors:Win
]

_MOVE_SCORE = {
  'X': 1,
  'Y': 2,
  'Z': 3
}

_MOVE_SCORE2 = {
  'X': 0,
  'Y': 3,
  'Z': 6
}


def _get_round_score(score_table: Sequence[Sequence[int]],
                     move_score: Dict[str, int], opponent: str,
                     you: str) -> int:
  return (
      score_table[ord(opponent) - ord('A')][ord(you) - ord('X')]
      + move_score[you]
  )


def _get_score(score_table: Sequence[Sequence[int]], rounds: Sequence[str],
               move_score: Dict[str, int]) -> int:
  return sum(
    [_get_round_score(score_table, move_score, *r.split(' ')) for r in rounds])


def get_score(rounds: Sequence[str]) -> int:
  return _get_score(rounds=rounds, score_table=_SCORE_TABLE,
                    move_score=_MOVE_SCORE)


def get_score2(rounds: Sequence[str]) -> int:
  return _get_score(rounds=rounds, score_table=_SCORE_TABLE2,
                    move_score=_MOVE_SCORE2)
