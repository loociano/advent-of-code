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
import functools
import math
from typing import Any, Sequence, TypeAlias

Packet: TypeAlias = list[Any, ...]
PacketPair: TypeAlias = tuple[Packet, Packet]

_SEPARATOR_PACKETS = [[[2]], [[6]]]


def _parse_pairs(packet_pairs: Sequence[str]) -> tuple[PacketPair, ...]:
  result = []
  for line_number, packet in enumerate(packet_pairs):
    if packet == '':
      left_packet = eval(packet_pairs[line_number - 2])
      right_packet = eval(packet_pairs[line_number - 1])
      result.append((left_packet, right_packet))
  # Last pair.
  left_packet = eval(packet_pairs[-2])
  right_packet = eval(packet_pairs[-1])
  result.append((left_packet, right_packet))
  return tuple(result)


def _parse_packets(packet_pairs: Sequence[str]) -> list[Packet, ...]:
  result = []
  for line_number, packet in enumerate(packet_pairs):
    if packet == '':
      result.append(eval(packet_pairs[line_number - 2]))
      result.append(eval(packet_pairs[line_number - 1]))
  # Last pair.
  result.append(eval(packet_pairs[-2]))
  result.append(eval(packet_pairs[-1]))
  return result


def is_correct_order(left: Packet, right: Packet) -> bool | None:
  for i in range(max(len(left), len(right))):
    if i == len(left):
      return True  # left list ran out of elements.
    if i == len(right):
      return False  # right list ran out of elements.
    if not right:
      return False
    left_val = left[i]
    right_val = right[i]
    if isinstance(left_val, int) and isinstance(right_val, int):
      if left_val != right_val:
        return left_val < right_val
    else:
      if isinstance(left_val, int):  # Mixed types.
        result = is_correct_order(left=[left_val], right=right_val)
      elif isinstance(right_val, int):  # Mixed types.
        result = is_correct_order(left=left_val, right=[right_val])
      else:  # Both packets must be lists.
        result = is_correct_order(left=left_val, right=right_val)
      if result is not None:
        return result


def _compare_packets(left: Packet, right: Packet):
  result = is_correct_order(left, right)
  if result:
    return -1  # Right order. left < right.
  if result is None:
    return 0  # Packets are identical. left = right.
  return 1  # Packets are in wrong order. left > right.


def sum_indices_correct_order(packet_pairs: Sequence[str]) -> int:
  return sum(index + 1 if is_correct_order(*pair) else 0
              for index, pair in enumerate(_parse_pairs(packet_pairs)))


def calc_decoder_key(packet_pairs: Sequence[str]) -> int:
  packets = _parse_packets(packet_pairs) + _SEPARATOR_PACKETS
  sorted_packets = sorted(packets, key=functools.cmp_to_key(_compare_packets))
  return math.prod(
    [sorted_packets.index(packet) + 1 for packet in _SEPARATOR_PACKETS])
