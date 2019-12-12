import math


class Universe:

    def __init__(self):
        self.moons = []
        self.states = set()

    @staticmethod
    def _lcm(a, b):
        return abs(a*b) // math.gcd(a, b)

    def _hash_state(self, axis: int):
        moon_states = []
        for moon in self.moons:
            moon_states.append('{} {}'.format(moon.pos[axis], moon.vel[axis]))
        return '\n'.join(moon_states)

    def add_moon(self, moon):
        self.moons.append(moon)

    def apply_gravity(self):
        for i in range(0, len(self.moons) - 1):
            for j in range(i + 1, len(self.moons)):
                for axis in range(0, 3):
                    pos_i = self.moons[i].pos[axis]
                    pos_j = self.moons[j].pos[axis]
                    if pos_i > pos_j:
                        self.moons[i].update_vel(axis, -1)
                        self.moons[j].update_vel(axis, 1)
                    elif pos_i < pos_j:
                        self.moons[i].update_vel(axis, 1)
                        self.moons[j].update_vel(axis, -1)

    def apply_gravity_axis(self, axis: int):
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

    def apply_velocity(self):
        for moon in self.moons:
            for axis in range(0, 3):
                moon.pos[axis] += moon.vel[axis]

    def apply_velocity_axis(self, axis: int):
        for moon in self.moons:
            moon.pos[axis] += moon.vel[axis]

    def simulate(self, steps: int):
        for step in range(0, steps):
            self.apply_gravity()
            self.apply_velocity()

    def simulate_axis(self, axis: int):
        states = set()
        hash_state = self._hash_state(axis)
        count = 0
        while hash_state not in states:
            states.add(hash_state)
            self.apply_gravity_axis(axis)
            self.apply_velocity_axis(axis)
            count += 1
            hash_state = self._hash_state(axis)
        return count

    def calc_steps(self):
        length_x = self.simulate_axis(0)
        length_y = self.simulate_axis(1)
        length_z = self.simulate_axis(2)
        return self._lcm(self._lcm(length_x, length_y), length_z)

    def calc_total_energy(self) -> int:
        total_energy = 0
        for moon in self.moons:
            pot_energy = 0
            kin_energy = 0
            for axis in range(0, 3):
                pot_energy += abs(moon.pos[axis])
                kin_energy += abs(moon.vel[axis])
            total_energy += pot_energy * kin_energy
        return total_energy


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
    return universe.calc_steps()


print(part_one('input', 1000))  # 6735
print(part_two('input'))  # 326489627728984
