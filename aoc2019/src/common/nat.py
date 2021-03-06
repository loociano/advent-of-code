# Copyright 2020 Google LLC
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


class NAT:
    def __init__(self, network):
        self.network = network
        self.packet = None
        self.last_y_delivered = None

    def is_network_idle(self):
        for computer in self.network:
            if not computer.idle:
                return False
        return True

    def has_packet(self):
        return self.packet is not None

    def is_repeated_y(self):
        return self.packet[1] == self.last_y_delivered

    def send_packet(self):
        self.last_y_delivered = self.packet[1]
        self.network[0].packet_queue.append(self.packet)
        self.packet = None
