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


def _get_program(file):
    with open(file) as f:
        return list(map(int, f.read().split(',')))


def part_one(filename: str):
    block_tile_count = 0
    vm = Intcode(_get_program(filename))
    while True:
        x = vm.run()
        if x is None:
            break
        y = vm.run()
        tile_id = vm.run()
        block_tile_count += 1 if tile_id == 2 else 0
    return block_tile_count


print(part_one('input'))
