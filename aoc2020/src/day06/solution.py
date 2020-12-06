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


def part_one(group_answers: List[str]) -> int:
  """
  Args:
    group_answers: answers to 26 yes-or-no questions that were answered yes,
    separated by group (empty line).

  Returns:
    Sum of the number of questions that every group answered 'yes'.
  """
  return _sum_yes_questions(group_answers)


def part_two(group_answers: List[str]) -> int:
  """
  Args:
    group_answers: answers to 26 yes-or-no questions that were answered yes,
    separated by group (empty line)

  Returns:
    Sum of the number of questions that everyone in the group answered 'yes'.
  """
  return _sum_yes_questions(group_answers, everyone_in_group_answered_yes=True)


def _sum_yes_questions(group_answers: List[str],
                       everyone_in_group_answered_yes=False) -> int:
  """
   Args:
    group_answers: answers to 26 yes-or-no questions that were answered yes,
    separated by group (empty line).
    everyone_in_group_answered_yes: true to count answer if everyone in the
    group answered yes; false if at least one member of the group answered yes.

    Returns:
      Sum of the number of questions that were answered 'yes'.
    """
  total_sum = 0
  group_size = 0
  positive_answers = [0] * 26
  for line in group_answers:
    if not line:
      total_sum += sum(
          1 for a in positive_answers
          if (a == group_size if everyone_in_group_answered_yes else a > 0))
      group_size = 0  # Reset
      positive_answers = [0] * 26  # Reset
    else:
      group_size += 1
      for question in line:
        positive_answers[ord(question) - ord('a')] += 1
  # Last group
  total_sum += sum(
      1 for a in positive_answers
      if (a == group_size if everyone_in_group_answered_yes else a > 0))
  return total_sum