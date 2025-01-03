# Copyright 2021 Google LLC
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


class LanternFish:
  """Represents a lanternfish."""
  _NEWBORN_TIMER = 8
  _SPAWN_TIMER = 6

  timer: int

  def __init__(self, timer: int = _NEWBORN_TIMER) -> None:
    self.timer = timer

  def run(self) -> bool:
    """Runs timer on lanternfish.

    Returns:
        True if the lanternfish spawns a new one, False otherwise.
    """
    if self.timer == 0:
      self.timer = self._SPAWN_TIMER
      return True
    self.timer -= 1
    return False


def part_one(lanternfish_ages: str, days: int) -> int:
  """AOC 2021 Day 6 Part 1.

  Args:
      lanternfish_ages: Comma-separated string of lanternfish ages.
      days: Number of elapsed days to calculate population of lanternfish.
  Returns:
      Number of lanternfish after elapsed days.
  """
  initial_state = tuple(map(int, lanternfish_ages[0].split(',')))
  population = [LanternFish(timer=timer) for timer in initial_state]
  today = 0
  while today < days:
    spawn_count = 0
    for fish in population:
      spawn_count += fish.run()
    population += [LanternFish() for _ in range(0, spawn_count)]
    today += 1
  return len(population)


def part_two(lanternfish_ages: str, days: int) -> int:
  """AOC 2021 Day 6 Part 2.

  Args:
      lanternfish_ages: Comma-separated string of lanternfish ages.
      days: Number of elapsed days to calculate population of lanternfish.
  Returns:
      Number of lanternfish after elapsed days.
  """
  population = list(map(int, lanternfish_ages[0].split(',')))
  # Object-oriented and array approach does not scale.
  # Inspired approach from redditor /u/mariothedogMC:
  # Maintain a map of fish timers and frequencies:
  fish_timer_frequencies = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
  }
  for fish in population:
    fish_timer_frequencies[fish] += 1
  for _ in range(days):
    new_fish_count = fish_timer_frequencies[0]
    for timer, freq in fish_timer_frequencies.copy().items():
      # Reset frequency.
      fish_timer_frequencies[timer] = 0
      if timer > 0:
        # Make tick. Shift frequencies to lower timer.
        fish_timer_frequencies[timer - 1] = freq
    # Spawn new fish.
    fish_timer_frequencies[8] += new_fish_count
    # Mother timers return to 6!
    fish_timer_frequencies[6] += new_fish_count
  return sum(fish_timer_frequencies.values())  # New population.
