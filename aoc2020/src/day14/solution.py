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
from typing import List


def part_one(program: List[str]) -> int:
  """
  Executes bitmask program and computes sum of values in memory.

  Args:
    program: bitmask program. It only supports 2 instructions:
    1. Mask assignment. Example: mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
    2. Memory assignment. Example: mem[8] = 11
  Returns:
    Sum of all values left in memory after program completes.
  """
  mask = None
  mem = {}
  for line in program:
    if 'mask' in line:
      mask = line.split('mask = ')[1]
    else:  # write into memory
      dest, value = line.split(' = ')
      mem[dest] = apply_mask(mask, int(value))
  return sum(mem.values())


def part_two(program: List[str]) -> int:
  """
  Executes bitmask program version 2.0 and computes sum of values in memory.

  Args:
    program: bitmask program. It only supports 2 instructions:
    1. Mask assignment. Example: mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
    2. Memory assignment. Example: mem[8] = 11
  Returns:
    Sum of all values left in memory after it completes.
  """
  mask = None
  mem = {}
  for line in program:
    if 'mask' in line:
      mask = line.split('mask = ')[1]
    else:  # write into memory
      dest, value = line.split(' = ')
      address = int((dest.split('mem[')[1]).split(']')[0])
      for address in calculate_addresses(apply_mask2(mask, address)):
        mem[address] = int(value)
  return sum(mem.values())


def apply_mask(mask: str, value: int) -> int:
  """
  Applies mask to a value with following rules:
  - 0 or 1 overwrites the corresponding bit in the value
  - X leaves the bit in the value unchanged

  Args:
    mask: 36-character string. Accepted values are X, 0 and 1.
    value: to integer to apply the mask to.
  Returns:
    Integer resulting from applying the mask to the input integer.
  """
  result = value
  for i, mask_value in enumerate(mask):
    pos = len(mask) - i - 1
    if mask_value == '0' and (value & (1 << pos)) >> pos == 1:
      result -= 1 << pos  # Overwrite
    elif mask_value == '1' and (value & (1 << pos)) >> pos == 0:
      result += 1 << pos  # Overwrite
  return result


def apply_mask2(mask: str, value: int) -> str:
  """
  Applies mask to a value following version 2.0 rules:
  - 0 does not change the bit in the value
  - 1 overwrites the bit in the value with 1
  - X overwrites the bit in the value with X

  Args:
    mask: 36-character string. Accepted values are X, 0 and 1.
    value: to integer to apply the mask to.
  Returns:
    String resulting from applying the mask to the input integer.
  """
  result = ['0'] * len(mask)
  for i, mask_value in enumerate(mask):
    pos = len(mask) - i - 1
    if mask_value == 'X':
      result[i] = 'X'  # Floating
    elif mask_value == '0':
      result[i] = str((value & (1 << pos)) >> pos)
    elif mask_value == '1':
      result[i] = '1'
    else:
      raise Exception('Unrecognized mask bit value')
  return ''.join(result)


def calculate_addresses(masked_address: str) -> List[int]:
  """
  Calculates the possible addresses, by producing all possible combinations
  of values X represented by 0 or 1.

  Args:
    masked_address: a 36-character string containing 0, 1 or X. X denotes
    floating bit.
  Returns:
    All combinations, in decimal.
  """
  addresses = []
  floating_positions = [i for i, mask_value in enumerate(masked_address)
                        if mask_value == 'X']

  for value in range(2**len(floating_positions)):
    address = list(masked_address)
    binary_array = [i for i in bin(value)[2:]]
    padded_binary_array = ['0'] * (len(floating_positions) - len(binary_array)) \
                          + binary_array
    for i, floating_pos in enumerate(floating_positions):
      address[floating_pos] = padded_binary_array[i]
    addresses.append(int(''.join(address), 2))
  return addresses