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


def fft(digits: list, target_phases: int) -> list:
    output = digits.copy()
    base_pat = [0, 1, 0, -1]
    for phase in range(0, target_phases):
        print('phase: {}'.format(phase))
        phase_output = []
        for i in range(0, len(output)):
            base_index = 0
            reps = i + 1
            digit_calc = 0
            count_reps = 1
            for j, digit in enumerate(output):
                if count_reps == reps:
                    count_reps = 0
                    if base_index == len(base_pat) - 1:
                        base_index = 0
                    else:
                        base_index += 1
                digit_calc += digit * base_pat[base_index]
                count_reps += 1
            phase_output.append(digit_calc % 10 if digit_calc >= 0 else abs(digit_calc % -10))
        output = phase_output
    return output


def part_one(filename: str, target_phases: int) -> str:
    output = fft(read_file(filename), target_phases)
    return ''.join([str(d) for d in output[:8]])

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
