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
from typing import List, Dict, Tuple


def part_one(notes: List[str]) -> int:
  """
  Args
    notes: contains rules, your ticket and nearby tickets.
  Returns
    Ticket scanning error rate.
  """
  nearby_tickets, your_ticket, rules = _parse_notes(notes)
  return _calculate_ticket_scanning_error_rate(nearby_tickets, rules)


def _parse_notes(notes: List[str]) \
    -> Tuple[List[str], str, Dict[str, Tuple[int, int, int, int]]]:
  """
  Args:
    notes: contains rules, your ticket and nearby tickets.
  Returns:
    nearby tickets, your ticket and rules
  """
  rules = {}
  your_ticket = None
  nearby_tickets = []
  rules_completed = False
  ticket_completed = False
  for line in notes:
    if not line:
      if not rules_completed:
        rules_completed = True
      else:
        ticket_completed = True
    else:
      if not rules_completed:
        # rules
        field, ranges = line.split(':')
        range1, range2 = ranges.split(' or ')
        range1_bottom, range1_top = range1.split('-')
        range2_bottom, range2_top = range2.split('-')
        rules[str(field)] = (int(range1_bottom), int(range1_top),
                             int(range2_bottom), int(range2_top))
      elif not ticket_completed:
        if 'your ticket:' not in line:
          your_ticket = line
      else:
        if 'nearby tickets:' not in line:
          nearby_tickets.append(line)
  return nearby_tickets, your_ticket, rules


def _calculate_ticket_scanning_error_rate(
    tickets: List[str], rules: Dict[str, Tuple[int, int, int, int]]) -> int:
  """
  Args:
    tickets: represented by a list of integers
    rules: field names with two valid ranges
  Returns:
    Sum of all the invalid values amongst all tickets.
  """
  invalid_values = 0
  for ticket in tickets:
    invalid_values += sum(_get_invalid_values(
        [int(i) for i in ticket.split(',')], rules))
  return invalid_values


def _get_invalid_values(
    values: List[int],
    rules: Dict[str, Tuple[int, int, int, int]]) -> List[int]:
  """
  Args:
    values: list of integers
    rules: field names with two valid ranges
  Returns:
    Values that do not satisfy any rule, if any. May be more than one.
  """
  # Unsure whether a ticket may contain more than one invalid value.
  invalid_values = []
  for value in values:
    valid = False
    for field, rule in rules.items():
      if _is_valid(value, rule):
        valid = True
        break
    if not valid:
      invalid_values.append(value)
  return invalid_values


def _is_valid(value: int, rule: Tuple[int, int, int, int]) -> bool:
  """
  Args:
    value: value to validate against rule
    rule: four integers representing two inclusive ranges
  Returns:
    True if number is included in one of the ranges.
  """
  return (rule[0] <= value <= rule[1]) or (rule[2] <= value <= rule[3])