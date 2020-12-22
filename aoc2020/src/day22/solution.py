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


def part_one(player_decks: List[str]) -> int:
  """
  Returns:
    Player's winning score.
  """
  player1_done = False
  deck1 = []
  deck2 = []
  for line in player_decks:
    if 'Player' in line:
      continue
    if not line:
      player1_done = True
    else:
      if player1_done:
        deck2.append(int(line))
      else:
        deck1.append(int(line))
  return _play(deck1, deck2)


def _play(deck1: List[int], deck2: List[int]) -> int:
  while len(deck1) and len(deck2):
    card1 = deck1.pop(0)
    card2 = deck2.pop(0)
    if card1 > card2:  # player 1 wins
      deck1.append(card1)
      deck1.append(card2)
    elif card2 > card1:  # player 2 wins
      deck2.append(card2)
      deck2.append(card1)
    else:
      raise Exception('Tie')
  return _calculate_winning_score(deck1 if len(deck1) else deck2)


def _calculate_winning_score(deck: List[int]) -> int:
  return sum([card * (len(deck) - pos) for pos, card in enumerate(deck)])
