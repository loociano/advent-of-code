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


class _BinaryTree:
  def __init__(self, value: int, parent=None, left=None, right=None):
    self.value: int = value
    self.parent: _BinaryTree | None = parent
    self.left: _BinaryTree | None = left
    self.right: _BinaryTree | None = right


def _has_even_num_digits(number: int) -> bool:
  return len(str(number)) % 2 == 0


def _parse(initial_state: str) -> tuple[_BinaryTree, ...]:
  """Returns binary tree roots."""
  return tuple(
      [_BinaryTree(value=int(stone)) for stone in initial_state.split()])


class Simulation:
  def __init__(self, initial_state: str):
    self._roots = _parse(initial_state)
    # Tracks value and descendants by iteration.
    self._cache: dict[int, list[int, ...]] = defaultdict(list)

  def _update_cache(self, node, add_value):
    # TODO: fix.
    self._cache[node.value].append(add_value)
    # Update ascendants
    curr = node.parent
    while curr is not None:
      values = self._cache[curr.value]
      last_value = self._cache[curr.value][len(values) - 1]
      self._cache[curr.value].append(last_value + add_value)
      curr = curr.parent

  def _iterate(self, node: _BinaryTree, num_iterations: int = 0) -> int:
    """Returns the number of stones after iteration."""
    if num_iterations == 0:
      return 1  # Leaf node
    # TODO: use cache.
    # if node.value in self._cache:
    #   return self._cache[node.value][num_iterations - 1]
    if node.value == 0:
      node.left = _BinaryTree(value=1, parent=node)
      self._update_cache(node=node, add_value=1)
      return self._iterate(node.left, num_iterations - 1)
    elif _has_even_num_digits(node.value):
      half_digits = len(str(node.value)) // 2
      # Break stone into 2:
      left_node = _BinaryTree(value=int(str(node.value)[:half_digits]),
                              parent=node)
      right_node = _BinaryTree(value=int(str(node.value)[half_digits:]),
                               parent=node)
      node.left = left_node
      node.right = right_node
      self._update_cache(node=node, add_value=2)
      return (self._iterate(node.left, num_iterations - 1)
              + self._iterate(node.right, num_iterations - 1))
    else:
      node.left = _BinaryTree(value=node.value * 2024, parent=node)
      self._update_cache(node=node, add_value=1)
      return self._iterate(node.left, num_iterations - 1)

  def simulate(self, num_iterations=0) -> int:
    result = 0
    for root in self._roots:
      result += self._iterate(root, num_iterations)
    return result


def count_stones(initial_state: str, blinks: int = 0) -> int:
  return Simulation(initial_state).simulate(num_iterations=blinks)
