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
import math


def load_reactions(filename: str):
    table = {}
    with open(filename) as f:
        for line in f.readlines():
            inputs, output = line.rstrip().split('=>')
            chemicals = inputs.rstrip().split(',')
            output_q, output_val = output.lstrip().split(' ')
            for i, val in enumerate(chemicals):
                a, b = val.lstrip().rstrip().split(' ')
                chemicals[i] = [int(a), b]
            chemicals.insert(0, int(output_q))
            table[output_val] = chemicals
    return table


def part_one(filename: str):
    ore_count = 0
    table = load_reactions(filename)
    bases = {}
    remainders = {}
    stack = [[1, 'FUEL']]
    while len(stack) > 0:
        out_num, name = stack.pop()
        print('{} {}'.format(out_num, name))
        deps = table.get(name)
        if len(deps) == 2:  # element maps directly to ORE
            if bases.get(name) is None:
                bases[name] = out_num
            else:
                bases[name] += out_num
        elif len(deps) > 2:
            minimum = deps[0]
            if out_num == minimum:
                multiplier = 1
            elif out_num < minimum:
                multiplier = 1  # math.ceil(minimum / out_num)
                remainders[name] = minimum - out_num
            else:
                multiplier = math.ceil(out_num / minimum)
                remainders[name] = out_num - minimum
            for i in range(1, len(deps)):
                stack.append([deps[i][0] * multiplier, deps[i][1]])

    for key, val in bases.items():
        deps = table.get(key)
        minimum = deps[0]
        ores = deps[1][0]
        ore_count += ores * math.ceil(val / minimum)
    return ore_count


print(part_one('input'))
