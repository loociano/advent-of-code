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


def _get_image_pixels(file):
    with open(file) as f:
        return list(map(int, f.read()))


def _get_layer_with_fewest_zeros(freq_list):
    result = -1
    min_zeros = sys.maxsize
    for freq in freq_list:
        if freq[0] < min_zeros:
            min_zeros = freq[0]
            result = freq
    return result


def _compute_freqs(pixels, width, height):
    layer = -1
    freq_list = []
    for i, pixel in enumerate(pixels):
        if i % (width * height) == 0:
            layer += 1
            freq_list.append([0 for i in range(0, 10)])
        freq_list[layer][pixel] += 1
    return freq_list


def _compute_image(pixels, width, height):
    num_layers = int(len(pixels) / (width * height))
    message = []
    for row in range(0, height):
        line_str = []
        for col in range(0, width):
            color = 2  # transparent
            for l in range(0, num_layers):
                color = pixels[(l * width * height) + (width * row) + col]
                if color == 0 or color == 1:  # black or white
                    break
            line_str.append('X' if color == 1 else ' ')
        message.append(''.join(line_str))
    return '\n'.join(message)


def part_one(filename, width, height):
    result_layer = _get_layer_with_fewest_zeros(_compute_freqs(_get_image_pixels(filename), width, height))
    return result_layer[1] * result_layer[2]


def part_two(filename, width, height):
    return _compute_image(_get_image_pixels(filename), width, height)


print(part_one('input', 25, 6))  # 1965
print(part_two('input', 25, 6))  # GZKJY
"""
 XX  XXXX X  X   XX X   X
X  X    X X X     X X   X
X      X  XX      X  X X 
X XX  X   X X     X   X  
X  X X    X X  X  X   X  
 XXX XXXX X  X  XX    X  
"""
