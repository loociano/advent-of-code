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
from functools import cache

computers = defaultdict(set)


def _build_computer_graph(connections: Sequence[str]) -> dict[str, set[str]]:
  computers: dict[str, set[str]] = defaultdict(set)
  for connection in connections:
    first, second = connection.split('-')  # Format is: '{name}-{name}'
    computers[first].add(second)
    computers[second].add(first)
  return computers


@cache
def _are_interconnected(a: str, b: str, c: str) -> bool:
  """Returns True iff computers a, b and c are interconnected."""
  return {b, c}.issubset(computers.get(a)) and {a, c}.issubset(computers.get(b)) and {a, b}.issubset(computers.get(c))


def _match_any(*computer_names: str, predicate: Callable) -> bool:
  return any(predicate(name) for name in computer_names)


def _find_cliques(r: set[str], p: set[str], x: set[str],
                  graph: dict[str, set[str]], cliques: list[tuple[str, ...]]) -> None:
  # https://en.wikipedia.org/wiki/Bron%E2%80%93Kerbosch_algorithm#With_pivoting
  # algorithm BronKerbosch2(R, P, X) is
  #   if P and X are both empty then
  #     report R as a maximal clique
  #   choose a pivot vertex u in P ⋃ X
  #   for each vertex v in P \ N(u) do
  #     BronKerbosch2(R ⋃ {v}, P ⋂ N(v), X ⋂ N(v))
  #     P := P \ {v}
  #     X := X ⋃ {v}
  if not p and not x:
    # Report R as the maximal clique.
    if len(r) > 2:
      cliques.append(tuple(sorted(r)))
    return
  # Choose a pivot vertex u in P ⋃ X.
  (d, pivot) = max([(len(graph[v]), v) for v in p.union(x)])
  # For each vertex v in P \ N(u) do:
  for v in p.difference(graph[pivot]):
    _find_cliques(r=r.union({v}), p=p.intersection(graph[v]), x=x.intersection(graph[v]),
                  graph=graph,
                  cliques=cliques)
    p.remove(v)
    x.add(v)


def count_computer_sets(connections: Sequence[str], starts_with: str) -> int:
  global computers
  computers = _build_computer_graph(connections)
  return sum(1
             if (_are_interconnected(a, b, c)
                 and _match_any(a, b, c, predicate=lambda x: x.startswith(starts_with)))
             else 0
             for a, b, c in combinations(computers.keys(), r=3))


def find_lan_password(connections: Sequence[str]) -> str:
  """Returns the LAN password.
  LAN Password is the alphabetical, comma-separated names of the largest set of interconnected computers."""
  global computers
  computers = _build_computer_graph(connections)
  cliques = []
  _find_cliques(r=set(), p=set(computers.keys()), x=set(), graph=computers, cliques=cliques)
  max_clique = max(cliques, key=len)  # Find the set with most computers.
  return ','.join(max_clique)
