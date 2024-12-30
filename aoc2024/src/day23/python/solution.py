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
from typing import Callable, Sequence
from collections import defaultdict
from itertools import combinations


def _build_computer_graph(connections: Sequence[str]) -> dict[str, set[str]]:
  computers: dict[str, set[str]] = defaultdict(set)
  for connection in connections:
    first, second = connection.split('-')  # Format is: '{name}-{name}'
    computers[first].add(second)
    computers[second].add(first)
  return computers


def _are_interconnected(a: str, b: str, c: str, computers: dict[str, set[str]]) -> bool:
  return {b, c}.issubset(computers.get(a)) and {a, c}.issubset(computers.get(b)) and {a, b}.issubset(computers.get(c))


def _match_any(*args, predicate: Callable) -> bool:
  return any(predicate(computer) for computer in args)


def count_computer_sets(connections: Sequence[str], starts_with: str) -> int:
  computers = _build_computer_graph(connections)
  return sum(1
             if (_are_interconnected(a, b, c, computers)
                 and _match_any(a, b, c, predicate=lambda x: x.startswith(starts_with)))
             else 0
             for a, b, c in combinations(computers.keys(), r=3))
