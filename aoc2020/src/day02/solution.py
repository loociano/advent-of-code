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
from typing import Callable


def part_one(policy_and_passwords: list) -> int:
  return _countValidPasswords(policy_and_passwords, _isValidPassword)


def part_two(policy_and_passwords: list) -> int:
  return _countValidPasswords(policy_and_passwords, _isValidPassword2)


def _countValidPasswords(policy_and_passwords: list,
    validate: Callable[[str, str], bool]) -> int:
  valid_passwords = 0
  for entry in policy_and_passwords:
    policy, password = _parseEntry(entry)
    if validate(policy, password):
      valid_passwords += 1
  return valid_passwords


def _parseEntry(entry: str) -> (str, str):
  policy, password = entry.split(':')
  return policy.strip(), password.strip()


def _isValidPassword(policy, password) -> bool:
  min, max, letter = _parsePolicy(policy)
  count = 0
  for p in password:
    if p == letter:
      count += 1
    if count > max:
      return False
  return count >= min


def _isValidPassword2(policy, password) -> bool:
  pos1, pos2, letter = _parsePolicy(policy)
  pos1 -= 1  # first position is 1
  pos2 -= 1  # first position is 1
  if password[pos1] != letter and password[pos2] != letter:
    return False
  if password[pos1] == letter and password[pos2] == letter:
    return False
  return password[pos1] == letter or password[pos2] == letter


def _parsePolicy(policy) -> (int, int, str):
  min_max, letter = policy.split(' ')
  min, max = min_max.split('-')
  return int(min), int(max), letter

