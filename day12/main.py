import math


class Universe:

    NUM_AXIS = 3

    def __init__(self):
        self.moons = []
        self.states = set()

    @staticmethod
    def _lcm(a, b) -> int:
        return abs(a * b) // math.gcd(a, b)

    def simulate(self, steps: int) -> None:
        for step in range(0, steps):
            self._apply_gravity()
            self._apply_velocity()

    def calc_universe_cycle_len(self) -> int:
        length_x = self._simulate_axis(0)
        length_y = self._simulate_axis(1)
        length_z = self._simulate_axis(2)
        return self._lcm(self._lcm(length_x, length_y), length_z)

    def calc_total_energy(self) -> int:
        total_energy = 0
        for moon in self.moons:
            pot_energy = 0
            kin_energy = 0
            for axis in range(0, self.NUM_AXIS):
                pot_energy += abs(moon.pos[axis])
                kin_energy += abs(moon.vel[axis])
            total_energy += pot_energy * kin_energy
        return total_energy

    def _hash_state(self, axis: int) -> str:
        moon_states = []
        for moon in self.moons:
            moon_states.append('{} {}'.format(moon.pos[axis], moon.vel[axis]))
        return '\n'.join(moon_states)

    def add_moon(self, moon) -> None:
        self.moons.append(moon)

    def _apply_gravity(self) -> None:
        for axis in range(0, self.NUM_AXIS):
            self._apply_gravity_axis(axis)

    def _apply_gravity_axis(self, axis: int) -> None:
        for i in range(0, len(self.moons) - 1):
            for j in range(i + 1, len(self.moons)):
                pos_i = self.moons[i].pos[axis]
                pos_j = self.moons[j].pos[axis]
                if pos_i > pos_j:
                    self.moons[i].update_vel(axis, -1)
                    self.moons[j].update_vel(axis, 1)
                elif pos_i < pos_j:
                    self.moons[i].update_vel(axis, 1)
                    self.moons[j].update_vel(axis, -1)

    def _apply_velocity(self) -> None:
        for axis in range(0, self.NUM_AXIS):
            self._apply_velocity_axis(axis)

    def _apply_velocity_axis(self, axis: int) -> None:
        for moon in self.moons:
            moon.pos[axis] += moon.vel[axis]

    def _simulate_axis(self, axis: int) -> int:
        states = set()
        hash_state = self._hash_state(axis)
        steps = 0
        while hash_state not in states:
            states.add(hash_state)
            self._apply_gravity_axis(axis)
            self._apply_velocity_axis(axis)
            hash_state = self._hash_state(axis)
            steps += 1
        return steps


class Moon:

    def __init__(self, pos):
        self.pos = pos
        self.vel = [0, 0, 0]

    def update_vel(self, axis, delta):
        self.vel[axis] += delta


def _load_moons_from_file(filename: str) -> Universe:
    universe = Universe()
    with open(filename) as f:
        for line in f.readlines():
            coords = list(map(lambda x: int(x.split('=')[1]),
                              line.rstrip().lstrip('<').rstrip('>').split(',')))
            universe.add_moon(Moon(coords))
    return universe


def part_one(filename: str, steps: int):
    universe = _load_moons_from_file(filename)
    universe.simulate(steps)
    return universe.calc_total_energy()


def part_two(filename: str):
    universe = _load_moons_from_file(filename)
    return universe.calc_universe_cycle_len()


print(part_one('input', 1000))  # 6735
print(part_two('input'))  # 326489627728984
