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
from math import ceil


def load_reactions(filename: str) -> dict:
    formulas = {}
    with open(filename) as f:
        for line in f.readlines():
            inputs, output = line.rstrip().split('=>')
            chemicals = inputs.rstrip().split(',')
            chem_amount, chem_name = output.lstrip().split(' ')
            for i, val in enumerate(chemicals):
                a, b = val.lstrip().rstrip().split(' ')
                chemicals[i] = [int(a), b]
            chemicals.insert(0, int(chem_amount))
            formulas[chem_name] = chemicals
    return formulas


def count_ores_recursive(totals: dict, formulas: dict, chem_name: str, amount: int):
    # Base case
    if chem_name == 'ORE':
        return amount

    deps = formulas[chem_name]
    output_amount = deps[0]
    amount -= totals[chem_name]
    multiplier = ceil(amount / output_amount)
    totals[chem_name] = multiplier * output_amount - amount
    ore_count = 0
    for i in range(1, len(deps)):
        chem_amount = multiplier * deps[i][0]
        chem_name = deps[i][1]
        ore_count += count_ores_recursive(totals, formulas, chem_name, chem_amount)
    return ore_count


def part_one(filename: str):
    formulas = load_reactions(filename)
    totals = {}
    for key in formulas.keys():
        totals[key] = 0
    return count_ores_recursive(totals, formulas, 'FUEL', 1)


print(part_one('input'))
