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
from aoc2019.src.common.intcode import Intcode, read_intcode


def get_num_blocks(program: Sequence[int]) -> int:
  block_tile_count = 0
  vm = Intcode(program)
  while True:
    x = vm.run()
    if x is None:
      break
    vm.run()  # ignore y value
    tile_id = vm.run()
    block_tile_count += tile_id == 2
  return block_tile_count


def part_one(program: str) -> int:
  return get_num_blocks(read_intcode(program))


def move_joystick(vm: Intcode, paddle_x: int, ball_x: int):
  vm.set_input(-1 if paddle_x > ball_x else 1 if paddle_x < ball_x else 0)


def beat_game(vm: Intcode) -> int:
  score = 0
  paddle_x = 0
  while True:
    x = vm.run()
    if x is None:
      break
    y = vm.run()
    data = vm.run()
    if x == -1 and y == 0:
      score = data
    else:
      if data == 3:  # paddle
        paddle_x = x
      if data == 4:  # ball
        move_joystick(vm, paddle_x, x)
  return score


def part_two(program: str) -> int:
  program = list(read_intcode(program))
  program[0] = 2  # play game
  return beat_game(Intcode(tuple(program)))
