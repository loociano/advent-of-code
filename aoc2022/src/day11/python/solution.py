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
from typing import List, Sequence, Tuple


class Monkey:
  """A Monkey:

  items: a queue of items represented by integers (worry level).
  operation: an operation to apply to items.
  test: boolean check whose outcome determines which monkey to pass to.
  """

  def __init__(self, items: List[int], operation_body: str, divisor: int,
               true_monkey: int, false_monkey: int):
    self.items = items
    self.operation = lambda old: eval(operation_body)
    self.inspected_count = 0
    self.divisor = divisor
    self.true_monkey = true_monkey
    self.false_monkey = false_monkey

  def test(self, item: int):
    return self.true_monkey if item % self.divisor == 0 else self.false_monkey


def _parse(monkey_notes: Sequence[str]) -> List[Monkey]:
  monkeys = []
  i = 0
  while i < len(monkey_notes):
    note = monkey_notes[i]
    if note.lstrip().startswith('Starting items: '):
      items = list(
        map(int, note.lstrip()[len('Starting items: '):].split(', ')))
    elif note.lstrip().startswith('Operation: '):
      operation_body = note.lstrip()[len('Operation: new = '):]
    elif note.lstrip().startswith('Test: divisible by '):
      divisor = int(
        re.search(r'Test: divisible by (\d+)', note.lstrip()).group(1))
      true_monkey = int(
        re.search(r'If true: throw to monkey (\d+)',
                  monkey_notes[i + 1].lstrip()).group(1))
      false_monkey = int(
        re.search(r'If false: throw to monkey (\d+)',
                  monkey_notes[i + 2].lstrip()).group(1))
      curr_monkey = Monkey(items=items, operation_body=operation_body,
                           divisor=divisor, true_monkey=true_monkey,
                           false_monkey=false_monkey)
      monkeys.append(curr_monkey)
      i += 2  # Skip already parsed lines.
    i += 1  # Next line.
  return monkeys


def _simulate(monkeys: List[Monkey], rounds: int) -> None:
  for _ in range(0, rounds):
    for monkey in monkeys:
      while len(monkey.items) > 0:
        monkey.inspected_count += 1
        item = monkey.items.pop(0)
        updated_item = monkey.operation(item)
        updated_item //= 3  # Relief
        to_monkey = monkey.test(updated_item)
        monkeys[to_monkey].items.append(updated_item)


def calc_monkey_business(monkey_notes: Sequence[str], rounds: int = 20) -> int:
  monkeys = _parse(monkey_notes)
  _simulate(monkeys, rounds)
  inspected_counts = sorted((monkey.inspected_count for monkey in monkeys),
                            reverse=True)
  return inspected_counts[0] * inspected_counts[1]
