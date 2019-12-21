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
import sys


def get_wires(filename: str) -> (list, list):
    with open(filename) as file:
        return list(file.readline().rstrip().split(',')), list(file.readline().rstrip().split(','))


def paint_path(area_dict: dict, delay_dict: dict, wire_data: list, id: int, with_delay: bool) -> int:
    min_dist = sys.maxsize
    x, y = 0, 0
    step = 0
    for i in range(len(wire_data)):
        next = wire_data[i]
        dir, steps = next[0:1], int(next[1:])
        for j in range(steps):
            if dir == 'R':
                x += 1
            elif dir == 'L':
                x -= 1
            elif dir == 'U':
                y += 1
            else:
                y -= 1
            step += 1
            key = "{} {}".format(x, y)
            if area_dict.get(key) is None or area_dict.get(key) == id:
                area_dict[key] = id
                delay_dict[key] = step
            else:
                min_dist = min(min_dist, delay_dict.get(key) + step if with_delay else abs(x) + abs(y))
    return min_dist


def part_one(filename: str) -> int:
    wire1, wire2 = get_wires(filename)
    area_dict = {}
    delay_dict = {}
    paint_path(area_dict, delay_dict, wire1, 1, False)
    return paint_path(area_dict, delay_dict, wire2, 2, False)


def part_two(filename: str) -> int:
    wire1, wire2 = get_wires(filename)
    area_dict = {}
    delay_dict = {}
    paint_path(area_dict, delay_dict, wire1, 1, True)
    return paint_path(area_dict, delay_dict, wire2, 2, True)

