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
from aoc2019.src.common.intcode import Intcode


class NetIntcode:

    def __init__(self, program: list, address: int, target_address: int, network: list):
        self.message_queue = []
        self.vm = Intcode(program)
        self.vm.input_val = address
        self.target_address = target_address
        self.network = network
        self.vm.run_until_input_or_done()
        self.vm.input_val = -1

    def run_until_io(self) -> int or None:
        if not self.message_queue:
            self.vm.input_val = -1
        else:
            self.vm.input_val = self.message_queue[0][0]  # provide X from next packet
        output = self.vm.run_until_io_or_done()
        if self.vm.stopped_on_input:
            if self.message_queue:
                x, y = self.message_queue.pop(0)
                self.vm.input_val = y
                self.vm.run_until_input_or_done()
        else:
            if output is None:
                return
            dest_address = output
            x = self.vm.run_until_io_or_done()
            y = self.vm.run_until_io_or_done()
            if dest_address == self.target_address:
                return y
            self.network[dest_address].message_queue.append((x, y))
