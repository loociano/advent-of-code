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
import re
from typing import Any, Callable, List, Sequence, Tuple
from dataclasses import dataclass


@dataclass
class Monkey:
  """A Monkey:

  items: a queue of items represented by integers (worry level).
  operation: an operation to apply to items.
  test: boolean check whose outcome determines which monkey to pass to.
  """
  items: List[int] = None
  operation: Callable[[Any, int], int] = None
  inspected_count: int = 0
  sum_amount: int = 0
  product_amount: int = 1
  divisor: int = 0
  true_monkey: int = -1
  false_monkey: int = -1

  def operation_sum(self, old: int):
    return old + self.sum_amount

  def operation_product(self, old: int):
    return old * self.product_amount

  def operation_power(self, old: int):
    return old * old

  def test(self, item: int):
    return self.true_monkey if item % self.divisor == 0 else self.false_monkey


def _parse(monkey_notes: Sequence[str]) -> List[Monkey]:
  monkeys = []
  curr_monkey = None
  i = 0
  while i < len(monkey_notes):
    note = monkey_notes[i]
    if note.startswith('Monkey '):
      curr_monkey = Monkey()
      monkeys.append(curr_monkey)
    elif note.lstrip().startswith('Starting items: '):
      curr_monkey.items = list(
        map(int, note.lstrip()[len('Starting items: '):].split(', ')))
    elif note.lstrip().startswith('Operation: '):
      matches = re.search(
        r'Operation: new = (.*) ([+*]) (.*)', note.lstrip())
      if matches.group(2) == '+':
        curr_monkey.sum_amount = int(matches.group(3))
        curr_monkey.operation = Monkey.operation_sum
      else:
        if matches.group(3) == 'old':
          curr_monkey.operation = Monkey.operation_power
        else:
          curr_monkey.product_amount = int(matches.group(3))
          curr_monkey.operation = Monkey.operation_product
    elif note.lstrip().startswith('Test: divisible by '):
      curr_monkey.divisor = int(
        re.search(r'Test: divisible by (\d+)', note.lstrip()).group(1))
      curr_monkey.true_monkey = int(
        re.search(r'If true: throw to monkey (\d+)',
                  monkey_notes[i + 1].lstrip()).group(1))
      curr_monkey.false_monkey = int(
        re.search(r'If false: throw to monkey (\d+)',
                  monkey_notes[i + 2].lstrip()).group(1))
      i += 2  # Skip already parsed lines.
    i += 1  # Next line.
  return monkeys


def _simulate(monkeys: List[Monkey], rounds: int) -> None:
  for _ in range(0, rounds):
    for monkey in monkeys:
      while len(monkey.items) > 0:
        monkey.inspected_count += 1
        item = monkey.items.pop(0)
        updated_item = monkey.operation(monkey, item)
        updated_item //= 3  # Relief
        to_monkey = monkey.test(updated_item)
        monkeys[to_monkey].items.append(updated_item)


def _find_top2_inspection_times(monkeys: List[Monkey]) -> Tuple[int, int]:
  top1 = 0
  top2 = 0
  for monkey in monkeys:
    if monkey.inspected_count > top1:
      top2 = top1
      top1 = monkey.inspected_count
    elif monkey.inspected_count > top2:
      top2 = monkey.inspected_count
  return top1, top2


def calc_monkey_business(monkey_notes: Sequence[str], rounds: int = 20) -> int:
  monkeys = _parse(monkey_notes)
  _simulate(monkeys, rounds)
  times1, times2 = _find_top2_inspection_times(monkeys)
  return times1 * times2
