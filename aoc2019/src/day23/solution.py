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
from aoc2019.src.common.nat import NAT
from aoc2019.src.common.net_intcode import NetIntcode


def init_network(program: list, num_computers: int, nat_address: int) -> list:
    network = []
    for address in range(num_computers):
        network.append(NetIntcode(program, address, nat_address, network))
    return network


def part_one(filename: str, num_computers: int, target_address: int) -> int:
    network = init_network(read_intcode(filename), num_computers, target_address)
    while True:
        for computer in network:
            packet = computer.run_until_io()
            if packet is not None and packet[0] == target_address:
                return packet[2]  # Y value


def part_two(filename: str, num_computers: int, nat_address: int) -> int:
    network = init_network(read_intcode(filename), num_computers, nat_address)
    nat = NAT(network)
    while True:
        for computer in network:
            packet = computer.run_until_io()
            if packet is not None and packet[0] == nat_address:
                nat.packet = (packet[1], packet[2])
        if nat.is_network_idle():
            if nat.is_repeated_y():
                return nat.lastY
            nat.send_packet()
