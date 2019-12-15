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
from common.intcode import Intcode
from common.utils import read_program


def get_new_pos(curr_pos: tuple, move: int) -> tuple:
    moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    delta = moves[move - 1]
    return curr_pos[0] + delta[0], curr_pos[1] + delta[1]


def get_possible_moves(visited: set, walls: set, curr_pos: tuple) -> list:
    moves = []
    for move in range(1, 5):
        new_pos = get_new_pos(curr_pos, move)
        if new_pos not in walls and new_pos not in visited:
            moves.append(move)
    return moves


def get_opposite_move(move: int) -> int:
    return 1 if move == 2 else 2 if move == 1 else 3 if move == 4 else 4


def do_move(vm: Intcode, move: int) -> int:
    vm.set_input(move)
    return vm.run()


def find_distance_to_oxygen(vm: Intcode) -> int:
    walls = set()
    visited = set()
    curr_pos = (0, 0)
    visited.add(curr_pos)
    move_stack = []
    while True:
        open_paths = get_possible_moves(visited, walls, curr_pos)
        if len(open_paths) > 0:
            move = open_paths.pop(0)
            result = do_move(vm, move)
            new_pos = get_new_pos(curr_pos, move)
            if result == 0:
                walls.add(new_pos)
            elif result == 1:
                curr_pos = new_pos
                move_stack.append(move)
                visited.add(new_pos)
            elif result == 2:
                move_stack.append(move)
                break  # found oxygen
        else:
            opposite_move = get_opposite_move(move_stack.pop())
            do_move(vm, opposite_move)  # ignore output
            curr_pos = get_new_pos(curr_pos, opposite_move)
    return len(move_stack)


def part_one(filename: str):
    vm = Intcode(read_program(filename))
    return find_distance_to_oxygen(vm)


print(part_one('input'))
