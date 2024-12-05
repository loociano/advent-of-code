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
from collections import defaultdict
from typing import Sequence

# Tracks pages to downstream pages.
type RuleGraph = defaultdict[int, set]


def _generate_graph(order_rules: Sequence[str]) -> RuleGraph:
  """Generates graph from order rules. A|B means A precedes B."""
  graph = defaultdict(set)
  for rule in order_rules:
    first, second = map(int, rule.split('|'))
    graph[first].add(second)
  return graph


def _is_valid(graph: RuleGraph, update: Sequence[int]) -> bool:
  """Returns true if an update (sequence of pages) complies with rules."""
  if len(update) == 1:
    return True
  curr_page = update[0]
  next_page = update[1]
  if curr_page not in graph:
    return False
  children = graph.get(curr_page)
  if next_page not in children:
    return False
  return _is_valid(graph, update[1:])


def sum_middle_pages(input: Sequence[str]) -> int:
  """Sums the middle page of all the valid updates."""
  breakline_num = list(input).index('')
  graph = _generate_graph(input[:breakline_num])
  updates = (list(map(int, input[i].split(',')))
             for i in range(breakline_num + 1, len(input)))
  return sum(update[len(update) // 2] if _is_valid(graph, update) else 0
             for update in updates)
