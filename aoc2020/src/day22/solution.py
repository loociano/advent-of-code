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
from typing import List, Tuple


def part_one(player_decks: List[str]) -> int:
  """
  Returns:
    Player's winning score.
  """
  return _play_combat(*_parse_input(player_decks))


def part_two(player_decks: List[str]) -> int:
  """
  Returns:
    Player's winning score.
  """
  return _play_recursive_combat(*_parse_input(player_decks))


def _parse_input(player_decks: List[str]) -> Tuple[List[int], List[int]]:
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
  return deck1, deck2


def _play_combat(deck1: List[int], deck2: List[int]) -> int:
  while len(deck1) and len(deck2):
    card1 = deck1.pop(0)
    card2 = deck2.pop(0)
    if card1 > card2:
      deck1 += [card1, card2]  # Player 1 wins
    elif card2 > card1:  # player 2 wins
      deck2 += [card2, card1]  # Player 2 wins
    else:
      raise Exception('Tie')
  return _calculate_winning_score(deck1 if len(deck1) else deck2)


def _play_recursive_combat(deck1: List[int], deck2: List[int]) -> int:
  return _calculate_winning_score(deck1) \
    if _play_subgame(deck1, deck2) else _calculate_winning_score(deck2)


def _play_subgame(deck1: List[int], deck2: List[int]) -> bool:
  """
  Returns:
    True if player1 wins, false if player 2 wins.
  """
  states = set()
  round_num = 1
  while len(deck1) and len(deck2):
    state = ','.join([str(card) for card in deck1] + [' ']
                     + [str(card) for card in deck2])
    if state in states:  # Player 1 wins to prevent infinite loop
      return True
    else:
      states.add(state)
      card1 = deck1.pop(0)
      card2 = deck2.pop(0)
      if len(deck1) >= card1 and len(deck2) >= card2:
        if _play_subgame(deck1[:card1].copy(), deck2[:card2].copy()):
          deck1 += [card1, card2]  # Player 1 wins
        else:
          deck2 += [card2, card1]  # Player 2 wins
      else:
        # Not enough cards to play a subgame. Regular rules apply.
        if card1 > card2:
          deck1 += [card1, card2]  # Player 1 wins
        elif card2 > card1:
          deck2 += [card2, card1]  # Player 2 wins
        else:
          raise Exception('Tie')
    round_num += 1
  return len(deck1) > 0


def _calculate_winning_score(deck: List[int]) -> int:
  return sum([card * (len(deck) - pos) for pos, card in enumerate(deck)])
