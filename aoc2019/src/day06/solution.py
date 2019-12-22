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


def get_orbits(file: str) -> dict:
    graph = {}
    with open(file) as f:
        orbits = list(f.readlines())
        for orbit in orbits:
            node1, node2 = orbit.rstrip().split(')')
            graph[node2] = node1
    return graph


def count_orbits(graph: dict, node: str) -> int:
    orbit_count = 0
    curr_node = node
    while graph.get(curr_node) is not None:
        curr_node = graph.get(curr_node)
        orbit_count += 1
    return orbit_count


def get_path(graph: dict, node: str) -> list:
    orbits = []
    curr_node = node
    while graph.get(curr_node) is not None:
        curr_node = graph.get(curr_node)
        orbits.append(curr_node)
    return orbits


def part_one(filename: str) -> int:
    graph = get_orbits(filename)
    orbit_count = 0
    for node in graph.keys():
        orbit_count += count_orbits(graph, node)
    return orbit_count


def part_two(filename: str) -> int:
    graph = get_orbits(filename)
    ancestors_you = get_path(graph, 'YOU')
    ancestors_santa = get_path(graph, 'SAN')
    count_you = len(ancestors_you) - 1
    count_san = len(ancestors_santa) - 1
    while ancestors_you[count_you] == ancestors_santa[count_san]:
        count_you -= 1
        count_san -= 1
    return count_you + count_san + 2

