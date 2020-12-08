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
from typing import List, Dict


class Bag:
  def __init__(self, color):
    self.color = color
    self.bags = {}  # type: Dict[str, Bag]
    self.amounts = {}  # type: Dict[str, int]


def part_one(rules: List[str], target_color: str) -> int:
  num_bag_colors = 0
  bags = _build_bag_graph(rules)
  for color, bag in bags.items():
    if color != target_color:
      num_bag_colors += _can_contain_target(bag, target_color)
  return num_bag_colors


def part_two(rules: List[str], target_color: str) -> int:
  bags = _build_bag_graph(rules)
  return _count_bag_and_inside(bags.get(target_color))


def _count_bag_and_inside(curr_bag: Bag) -> int:
  if not len(curr_bag.bags):
    return 0
  num_bags = 0
  for color, bag in curr_bag.bags.items():
    num_bags += curr_bag.amounts[color] * (1 + _count_bag_and_inside(bag))
  return num_bags


def _can_contain_target(bag: Bag, target_color: str) -> bool:
  if bag.color == target_color:
    return True
  if len(bag.bags) == 0:
    return False

  for amount, child_bag in bag.bags.items():
    if _can_contain_target(child_bag, target_color):
      return True
  return False


def _build_bag_graph(rules: List[str]) -> Dict[str, Bag]:
  graph = {}
  for rule in rules:
    parent_rule, children_rule = rule.split(' contain ')
    parent_color = parent_rule.split(' bags')[0]
    if graph.get(parent_color) is None:
      parent_bag = Bag(parent_color)
      graph[parent_color] = parent_bag
    else:
      parent_bag = graph.get(parent_color)
    if children_rule != 'no other bags.':
      children_rules = children_rule.split(', ')
      for children_rule in children_rules:
        amount, adjective, color = \
          children_rule.split('bag')[0].rstrip(' ').split(' ')
        child_color = '{} {}'.format(adjective, color)
        if graph.get(child_color) is None:
          child_bag = Bag(child_color)
          graph[child_color] = child_bag
        else:
          child_bag = graph.get(child_color)
        parent_bag.bags[child_color] = child_bag
        parent_bag.amounts[child_color] = int(amount)
  return graph
