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


def _get_wires(filename):
    with open(filename) as file:
        return list(file.readline().rstrip().split(',')), list(file.readline().rstrip().split(','))


def _paint_path(area_dict, delay_dict, wire_data, id, with_delay):
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


def part_one():
    wire1, wire2 = _get_wires('input')
    area_dict = {}
    delay_dict = {}
    _paint_path(area_dict, delay_dict, wire1, 1, False)
    return _paint_path(area_dict, delay_dict, wire2, 2, False)


def part_two():
    wire1, wire2 = _get_wires('input')
    area_dict = {}
    delay_dict = {}
    _paint_path(area_dict, delay_dict, wire1, 1, True)
    return _paint_path(area_dict, delay_dict, wire2, 2, True)


print(part_one())  # 1626
print(part_two())  # 27330
