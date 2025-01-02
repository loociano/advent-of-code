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
from typing import Sequence
from collections import defaultdict, deque
from itertools import product
import graphviz

type GateOp = tuple[str, str, str]


def _parse_input(input: Sequence[str]) -> tuple[
  dict[str | GateOp, list[str | GateOp]], dict[str | GateOp, int], dict[str, GateOp]]:
  graph = defaultdict(list)  # Adjacency list.
  initial_values = dict()  # Wires with initial values.
  ends = dict()  # Reverse map with gate output as keys and gate inputs as values.
  is_initial_values = True
  for line in input:
    if line == '':
      is_initial_values = False
    elif is_initial_values:
      name, value = line.split(': ')  # Example: 'x00: 1'
      initial_values[name] = int(value)
    else:
      source, dest = line.split(' -> ')  # Example: 'ntg XOR fgs -> mjb'
      wire1, gate, wire2 = source.split()
      graph[(wire1, gate, wire2)].append(dest)
      graph[wire1].append((wire1, gate, wire2))
      graph[wire2].append((wire1, gate, wire2))
      ends[dest] = (wire1, gate, wire2)
  return graph, initial_values, ends


def _get_in_degrees(graph: dict[str, list[str]]) -> dict[str, int]:
  """Computes the in-degree for each node in a graph."""
  in_degree = defaultdict(int)
  for vertex in graph.keys():
    in_degree[vertex] = 0
  for adj_list in graph.values():
    for vertex in adj_list:
      in_degree[vertex] += 1
  return in_degree


def _topological_sort(graph: dict[str, list[str]]) -> list[str]:
  """Returns nodes in a graph in topological order."""
  # https://en.wikipedia.org/wiki/Topological_sorting#Kahn's_algorithm
  queue = deque()  # Stores vertices with in_degree=0.
  in_degrees = _get_in_degrees(graph)
  for wire, in_degree in in_degrees.items():
    if in_degree == 0:
      queue.append(wire)
  result = []
  while queue:
    node = queue.popleft()
    result.append(node)
    for adjacent in graph.get(node, []):
      in_degrees[adjacent] -= 1
      if in_degrees[adjacent] == 0:
        queue.append(adjacent)
  return result


def _wires_to_integer(wire_values: dict[str | GateOp, int], wire_prefix: str) -> int:
  result = []  # Will contain pairs of z-wires and their values, example: ('z00', 1).
  for name, value in wire_values.items():
    if type(name) is str and name.startswith(wire_prefix):
      result.append((name, value))
  return int(''.join([str(value) for _, value in sorted(result, reverse=True)]), 2)


def _calculate(graph: dict[str | GateOp, list[str | GateOp]],
               wire_values: dict[str | GateOp, int],
               ends: dict[str, GateOp]) -> None:
  for task in _topological_sort(graph):
    if type(task) is tuple:  # Is a logic gate.
      wire1, gate, wire2 = task
      if gate == 'AND':
        wire_values[task] = wire_values[wire1] & wire_values[wire2]
      elif gate == 'OR':
        wire_values[task] = wire_values[wire1] | wire_values[wire2]
      elif gate == 'XOR':
        wire_values[task] = wire_values[wire1] ^ wire_values[wire2]
    elif task in ends:
      wire_values[task] = wire_values[ends.get(task)]


def get_output(input: Sequence[str]) -> int:
  graph, wire_values, ends = _parse_input(input)
  _calculate(graph=graph, wire_values=wire_values, ends=ends)
  return _wires_to_integer(wire_values=wire_values, wire_prefix='z')


def _swap(a: str, b: str, graph: dict[str | GateOp, list[str | GateOp]], ends: dict[str, GateOp]) -> None:
  for adj_list in graph.values():
    if len(adj_list) == 1 and adj_list[0] == a:
      adj_list[0] = ''
  for adj_list in graph.values():
    if len(adj_list) == 1 and adj_list[0] == b:
      adj_list[0] = a
  for adj_list in graph.values():
    if len(adj_list) == 1 and adj_list[0] == '':
      adj_list[0] = b
  tmp = ends[a]
  ends[a] = ends[b]
  ends[b] = tmp


def _print_graphviz(graph: dict[str | GateOp, list[str | GateOp]]) -> None:
  """Prints graph as Graphviz DOT."""
  dot = graphviz.Digraph()
  for key, values in graph.items():
    for value in values:
      dot.edge(str(key), str(value))
  print(dot.source)


def find_wrong_output_wires(input: Sequence[str], swaps: tuple[tuple[str, str], ...], operation: str = '&') -> str:
  graph, wire_values, ends = _parse_input(input)
  # _print_graphviz(graph)
  x = _wires_to_integer(wire_values, wire_prefix='x')
  y = _wires_to_integer(wire_values, wire_prefix='y')
  for swap in swaps:
    _swap(a=swap[0], b=swap[1], graph=graph, ends=ends)
  _calculate(graph=graph, wire_values=wire_values, ends=ends)
  z = _wires_to_integer(wire_values=wire_values, wire_prefix='z')
  expected = eval(f'{x} {operation} {y}')
  if expected == z:
    return ','.join(sorted(([wire for swap in swaps for wire in swap])))
  raise ValueError('Could not find wrong wires!')
