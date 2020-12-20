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
from typing import List, Tuple


def part_one(expressions: List[str]) -> int:
  """
  Returns:
    Result of the math expression.
  """
  return sum(_evaluate(_tokenize_expression(expression), 0)[0]
             for expression in expressions)


def _tokenize_expression(expression: str) -> List[str]:
  tokens = []
  for token in expression.split(' '):
    if '(' in token or ')' in token:
      tokens += list(token)
    else:
      tokens.append(token)
  return tokens


def _evaluate(tokens: List[str], pos: int) -> Tuple:
  """
  Returns:
    Result of the expression and next position to evaluate.
  """
  acc = 0
  op = None
  while pos < len(tokens):
    token = tokens[pos]
    if token == ')':
      break
    if token == '+' or token == '*':
      op = token
      pos += 1
    elif token == '(':
      subresult, new_pos = _evaluate(tokens, pos + 1)
      acc = _op(acc, op, subresult)
      pos = new_pos + 1
    else: # number
      acc = _op(acc, op, int(token))
      pos += 1
  return acc, pos


def _op(left_operand: int, op: str, right_operand: int) -> int:
  if op is None:
    return int(right_operand)
  if op == '+':
    return left_operand + int(right_operand)
  if op == '*':
    return left_operand * int(right_operand)
  raise Exception('Unknown operator.')