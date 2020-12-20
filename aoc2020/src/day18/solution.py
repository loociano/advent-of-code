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
    Sum of result(s) of the math expression(s).
  """
  return sum(_evaluate(_tokenize_expression(expression), 0)[0]
             for expression in expressions)


def part_two(expressions: List[str]) -> int:
  return sum(_advanced_evaluate(_tokenize_expression(expression))
             for expression in expressions)


def _tokenize_expression(expression: str) -> List[str]:
  tokens = []
  for token in expression.split(' '):
    if '(' in token or ')' in token:
      tokens += list(token)
    else:
      tokens.append(token)
  return tokens


def _advanced_evaluate(tokens: List[str]) -> int:
  while '(' in tokens:
    next_closing = _find_closing_pos(tokens.index('('), tokens)
    result = _advanced_evaluate(tokens[tokens.index('(') + 1:next_closing])
    tokens = tokens[:tokens.index('(')] + [result] + tokens[next_closing + 1:]

  while len(tokens) > 1:
    if '+' in tokens:
      next_plus = tokens.index('+')
      result = _op(int(tokens[next_plus - 1]), '+', int(tokens[next_plus + 1]))
      tokens = tokens[:next_plus - 1] + [result] + tokens[next_plus + 2:]
    elif '*' in tokens:
      next_prod = tokens.index('*')
      result = _op(int(tokens[next_prod - 1]), '*', int(tokens[next_prod + 1]))
      tokens = tokens[:next_prod - 1] + [result] + tokens[next_prod + 2:]
  return tokens[0]


def _find_closing_pos(open_pos: int, tokens: List[str]) -> int:
  stack = []
  i = open_pos
  while i < len(tokens):
    if tokens[i] == '(':
      stack.append(i)
    elif tokens[i] == ')':
      stack.pop()
      if len(stack) == 0:
        return i
    i += 1

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