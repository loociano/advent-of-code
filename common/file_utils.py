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
import os


def read_intcode(file) -> list:
    with open(file) as f:
        return list(map(int, f.read().split(',')))


def read_map(file) -> list:
    with open(file) as f:
        return [list(line.rstrip('\n')) for line in f.readlines()]


def read_lines(file) -> list:
    with open(file) as f:
        return [line.rstrip() for line in f.readlines()]


def read_integers(file: str) -> list:
    with open(file) as f:
        return list(map(int, [x for x in f.read()]))


def read_as_ints(file: str) -> list:
    with open(file) as f:
        return list(map(int, [x for x in f.readlines()]))


def get_path(dir_name: str, filename: str) -> str:
    return os.path.join(os.path.dirname(dir_name), filename)
