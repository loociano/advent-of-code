# Copyright 2019 Google LLC
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
from aoc2019.src.common.file_utils import read_lines


class Shuffler:
    def __init__(self, deck_size: int):
        self.deck = [i for i in range(0, deck_size)]

    def deal_into_new_stack(self) -> list:
        self.deck.reverse()
        return self.deck

    def deal_with_increment(self, increment: int) -> list:
        new_deck = [0] * len(self.deck)  # space complex. could be O(increment) instead of O(n)
        step = 0
        for i in range(0, len(self.deck)):
            new_deck[step % len(self.deck)] = self.deck[i]
            step += increment
        self.deck = new_deck
        return self.deck

    def cut(self, cut_num: int) -> list:
        if cut_num > 0:
            while cut_num > 0:
                self.deck.append(self.deck.pop(0))
                cut_num -= 1
        else:
            while cut_num < 0:
                self.deck.insert(0, self.deck.pop(len(self.deck) - 1))
                cut_num += 1
        return self.deck

    def apply_techniques(self, techniques: list) -> list:
        for technique in techniques:
            if technique == 'deal into new stack':
                self.deal_into_new_stack()
            elif technique[0:len('deal with increment')] == 'deal with increment':
                increment = int(technique[len('deal with increment'):])
                self.deal_with_increment(increment)
            elif technique[0:len('cut')] == 'cut':
                cut_num = int(technique[len('cut'):])
                self.cut(cut_num)
        return self.deck


def part_one(filename: str, deck_size: int, target: int) -> int:
    shuffler = Shuffler(deck_size)
    shuffler.apply_techniques(read_lines(filename))
    for i, val in enumerate(shuffler.deck):
        if val == target:
            return i
