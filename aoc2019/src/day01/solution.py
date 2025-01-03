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
from typing import Sequence


def _get_mass_list(masses: Sequence[str]) -> Sequence[int]:
  return tuple(map(int, masses))


def _calculate_fuel(mass):
  return mass // 3 - 2


def part_one(masses: Sequence[str]):
  total_fuel_req = 0
  for mass in _get_mass_list(masses):
    total_fuel_req += _calculate_fuel(mass)
  return total_fuel_req


def part_two(masses: Sequence[str]):
  total_fuel = 0
  for module_mass in _get_mass_list(masses):
    module_fuel = _calculate_fuel(module_mass)
    while module_fuel > 0:
      total_fuel += module_fuel
      module_fuel = _calculate_fuel(module_fuel)
  return total_fuel
