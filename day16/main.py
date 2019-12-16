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


def read_file(file: str) -> list:
    with open(file) as f:
        return list(map(int, [x for x in f.read()]))


def generate_pattern(order: int, length: int) -> list:
    base_pat = [0, 1, 0, -1]
    pattern = []
    base_index = 0
    while len(pattern) <= length:
        reps = order + 1
        while reps > 0 and len(pattern) <= length:
            pattern.append(base_pat[base_index])
            reps -= 1
        if base_index >= len(base_pat) - 1:
            base_index = 0
        else:
            base_index += 1
    pattern.pop(0)
    return pattern


def generate_patterns(length: int) -> list:
    return [generate_pattern(i, length) for i in range(0, length)]


def part_one(filename: str, target_phases: int) -> str:
    digits = read_file(filename)
    patterns = generate_patterns(len(digits))

    for phase in range(0, target_phases):
        output_digits = []
        for i in range(0, len(digits)):
            digit_calc = 0
            for j, digit in enumerate(digits):
                digit_calc += digit * patterns[i][j]
            output_digits.append(digit_calc % 10 if digit_calc >= 0 else abs(digit_calc % -10))
        digits = output_digits
    return ''.join([str(d) for d in digits[:8]])


print(part_one('input', 100))  # 70856418
