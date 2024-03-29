# Copyright 2022 Google LLC
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

# Number of different characters that indicate the position of a marker.
_MARKER_SIZE = 4


def find_marker_position(buffer: str, marker_size: int = _MARKER_SIZE) -> int:
  seen = [False] * 26  # Input only contains a-z.
  for pos in range(len(buffer)):
    if pos >= marker_size - 1:
      for window_pos in range(pos - marker_size + 1, pos + 1):
        seen[ord(buffer[window_pos]) - ord('a')] = True
      if seen.count(True) == marker_size:
        return pos + 1
      else:
        seen = [False] * 26  # Reset.
  raise ValueError('Could not find marker position.')
