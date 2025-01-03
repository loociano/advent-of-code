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
import re
from copy import deepcopy

from typing import List, Tuple, Dict


def part_one(rules_and_messages: List[str]) -> int:
  """
  Returns:
    Number of messages that completely match rule 0
  """
  rules, messages = _parse(rules_and_messages)
  rule = _flatten_rules(rules)
  return sum(_matches_rule(message, rule) for message in messages)


def part_two(rules_and_messages: List[str]) -> int:
  """
  Returns:
    Number of messages that completely match rule 0 with added loops in rules
    8 and 11.
  """
  rules, messages = _parse(rules_and_messages)
  num_loops = 1
  num_matching_messages = None
  # Increase the number of loops until no message matches anymore.
  while True:
    rules[8] = _compute_rule_8(num_loops)
    rules[11] = _compute_rule_11(num_loops)
    rule = _flatten_rules(rules)
    new_num_matching_messages = \
      sum(_matches_rule(message, rule) for message in messages)
    if new_num_matching_messages == num_matching_messages:
      # Last matching number was the maximum.
      return num_matching_messages
    else:
      num_matching_messages = new_num_matching_messages
    num_loops += 1


def _compute_rule_8(num_loops: int) -> str:
  """
  Computes rule 8 with n number of loops:
    n=0: 42
    n=1: 42 | 42 42
    n=2: 42 | 42 42 | 42 42 42
  Args:
    num_loops: number of loops
  Returns
    Computed rule 8.
  """
  new_rule = ['42']
  for num_loop in range(num_loops):
    new_rule.append(' |')
    for i in range(num_loop + 2):
      new_rule.append(' 42')
  return ''.join(new_rule)


def _compute_rule_11(num_loops: int) -> str:
  """
    Computes rule 11 with n number of loops:
      n=0: 42 31
      n=1: 42 | 42 42 31 31
      n=2: 42 | 42 42 31 31 | 42 42 42 31 31 31
    Args:
      num_loops: number of loops
    Returns
      Computed rule 11.
    """
  new_rule = ['42 31']
  for num_loop in range(num_loops):
    new_rule.append(' |')
    for i in range(num_loop + 2):
      new_rule.append(' 42')
    for i in range(num_loop + 2):
      new_rule.append(' 31')
  return ''.join(new_rule)


def _flatten_rules(original_rules: Dict[int, str]) -> str:
  rules = deepcopy(original_rules)
  num_rules = len(rules)
  resolved = {}
  while len(resolved) < num_rules:
    for rule_num, rule in rules.items():
      if resolved.get(rule_num):
        continue
      if not bool(re.search(r'\d', rule)):
        resolved[rule_num] = rule.replace(' ', '')
      rules[rule_num] = _replace_with_resolved(rules[rule_num], resolved)
  return resolved[0]


def _replace_with_resolved(rule: str, resolved: Dict[int, str]) -> str:
  new_rule = []
  for subrule in rule.split(' '):
    if subrule == '|' or subrule == 'a' or subrule == 'b' or '(' in subrule:
      new_rule.append(subrule)
      continue
    resolved_rule = resolved.get(int(subrule))
    if resolved_rule is not None:
      if resolved_rule == 'a' or resolved_rule == 'b':
        new_rule.append(resolved_rule)
      else:
        new_rule.append('({})'.format(resolved.get(int(subrule))))
    else:
      new_rule.append(subrule)
  return ' '.join(new_rule)


def _matches_rule(message: str, rule: str) -> bool:
  return re.compile('^{}$'.format(rule)).match(message) is not None


def _parse(rules_and_messages: List[str]) -> Tuple[Dict[int, str], List[str]]:
  finished_rules = False
  rules = {}
  messages = []
  for line in rules_and_messages:
    if not line:
      finished_rules = True
    elif finished_rules: # messages
      messages.append(line)
    else: # rules
      rule_num, rule = line.split(': ')
      rules[int(rule_num)] = rule.replace('"', '')  # remove quotes for "a" and "b"
  return rules, messages
