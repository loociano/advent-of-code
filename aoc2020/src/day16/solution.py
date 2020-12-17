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
  nearby_tickets, your_ticket, rules = parse_notes(notes)
  return _calculate_ticket_scanning_error_rate(nearby_tickets, rules)


def part_two(notes: List[str]) -> int:
  """
  Args
    notes: contains rules, your ticket and nearby tickets.
  Returns
    Product of values for the 6 departure fields.
  """
  nearby_tickets, your_ticket, rules = parse_notes(notes)
  valid_tickets = _exclude_invalid_tickets(nearby_tickets, rules)
  ordered_fields = find_field_order(valid_tickets, rules)
  return _multiply_departure_fields(your_ticket, ordered_fields)


def find_field_order(tickets: List[List[int]],
                     rules: Dict[str, Tuple[int, int, int, int]]) -> List[str]:
  """
  Args:
    tickets: each ticket represented by list of integers.
    rules: field names with two valid ranges.
  Returns:
    Ordered fields.
  """
  available_rules = rules.copy()
  num_fields = len(rules.keys())
  ordered_fields = [''] * num_fields

  pos = 0
  while len(available_rules):
    if ordered_fields[pos] == '':
      values = [ticket[pos] for ticket in tickets]
      valid_fields = _find_valid_fields(values, available_rules)
      if len(valid_fields) == 1:
        field = valid_fields[0]
        ordered_fields[pos] = field
        del available_rules[field]
    pos += 1
    if pos >= num_fields:
      pos = 0
  return ordered_fields


def parse_notes(notes: List[str]) \
    -> Tuple[List[List[int]], List[int], Dict[str, Tuple[int, int, int, int]]]:
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
          your_ticket = [int(value) for value in line.split(',')]
      else:
        if 'nearby tickets:' not in line:
          nearby_tickets.append([int(value) for value in line.split(',')])
  return nearby_tickets, your_ticket, rules


def _multiply_departure_fields(ticket: List[int], fields: List[str]) -> int:
  """
  Args:
    ticket: list of integers.
    fields: ordered fields.
  Returns:
    Product of values whose fields start with 'departure'.
  """
  result = 1
  for i, field in enumerate(fields):
    if 'departure' in field:
      result *= ticket[i]
  return result


def _calculate_ticket_scanning_error_rate(
    tickets: List[List[int]], rules: Dict[str, Tuple[int, int, int, int]]) -> int:
  """
  Args:
    tickets: represented by a list of integers.
    rules: field names with two valid ranges.
  Returns:
    Sum of all the invalid values amongst all tickets.
  """
  invalid_values = 0
  for ticket in tickets:
    invalid_values += sum(_get_invalid_values(ticket, rules))
  return invalid_values


def _exclude_invalid_tickets(
    tickets: List[List[int]], rules: Dict[str, Tuple[int, int, int, int]]) \
    -> List[List[int]]:
  """
  Args:
    tickets: each ticket represented by a list of integers.
    rules: field names with two valid ranges.
  Returns:
    Valid tickets.
  """
  valid_tickets = []
  for ticket in tickets:
    if not len(_get_invalid_values(ticket, rules)):
      valid_tickets.append(ticket)
  return valid_tickets


def _find_valid_fields(values: List[int],
                       rules: Dict[str, Tuple[int, int, int, int]]) \
    -> List[str]:
  """
  Args:
    values: list if integer values.
    rules: field names with two valid ranges
  Returns
    Field(s) that satisfy all values.
  """
  valid_fields = []  # Could be more than one?
  for field, rule in rules.items():
    if _are_valid(values, rule):
      valid_fields.append(field)
  return valid_fields


def _are_valid(values: List[int], rule: Tuple[int, int, int, int]) -> bool:
  """
  Args:
    values: list of integer valeus.
    rule: field name with two valid ranges
  Returns:
    True if all values satisfy the rule.
  """
  for value in values:
    if not _is_valid(value, rule):
      return False
  return True

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