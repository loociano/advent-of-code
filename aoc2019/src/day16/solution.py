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
from aoc2019.src.common.file_utils import read_integers


def fft(digits: list, target_phases: int) -> list:
    output = digits.copy()
    base_pat = [0, 1, 0, -1]
    for phase in range(0, target_phases):
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


# Calculates FFT for the second half of the input list [n/2, n].
# For a digit at position i, its new value is calculated as (A[i] + A[i+1] + ... + A[n]) % 10
def fft_second_half(digits: list, target_phases: int) -> list:
    output = digits.copy()
    half_len = len(digits) // 2
    for phase in range(0, target_phases):
        phase_output = [0] * len(digits)
        right_array_sum = sum(output[half_len:])
        for i in range(half_len, len(output)):
            if i != 0:
                right_array_sum -= output[i - 1]
            phase_output[i] = right_array_sum % 10
        output = phase_output
    return output


def part_one(filename: str, target_phases: int) -> str:
    output = fft(read_integers(filename), target_phases)
    return ''.join(map(str, output[:8]))


def part_two(filename: str, target_phases: int) -> str:
    input_num = read_integers(filename) * 10000
    offset = int(''.join(map(str, input_num[:7])))
    output = fft_second_half(input_num, target_phases)
    return ''.join(map(str, output[offset:offset + 8]))
