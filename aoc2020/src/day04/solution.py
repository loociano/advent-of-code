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

from aoc2020.src.day04.Passport import Passport


def part_one(batch_file: List[str]) -> int:
  return _count_valid_passports(batch_file)


def part_two(batch_file: List[str]) -> int:
  return _count_valid_passports(batch_file, validate_fields=True)


def _count_valid_passports(batch_file: List[str], validate_fields=False) -> int:
  num_valid_passports = 0
  passport = Passport()

  for line in batch_file:
    if line:
      _parse_line(line, passport)
    else:
      if passport.has_required_fields() \
          and (not validate_fields or passport.is_valid()):
        num_valid_passports += 1
      passport = Passport()  # reset
  # Last one
  if passport.has_required_fields() \
      and (not validate_fields or passport.is_valid()):
    num_valid_passports += 1
  return num_valid_passports


def _parse_line(line: str, passport: Passport) -> None:
  line_fields = line.split(' ')
  for line_field in line_fields:
    field, value = line_field.split(':')
    passport.__dict__[field] = value