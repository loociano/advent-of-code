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
from aoc2019.src.common.file_utils import read_intcode
from aoc2019.src.common.net_intcode import NetIntcode


def pending_messages(network) -> bool:
    for n in network:
        if n.message_queue:
            return True
    return False


def part_one(filename: str, num_computers: int, target_address: int) -> int:
    network = []
    program = read_intcode(filename)
    for address in range(num_computers):
        network.append(NetIntcode(program, address, target_address, network))
    while True:
        for computer in network:
            y = computer.run_until_io()
            if y is not None:
                return y
