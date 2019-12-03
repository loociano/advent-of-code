def _get_mass_list(filename):
    with open(filename) as file:
        return list(map(int, file))


def _calculate_fuel(mass):
    return mass // 3 - 2


def part_one(filename):
    total_fuel_req = 0
    for mass in _get_mass_list(filename):
        total_fuel_req += _calculate_fuel(mass)
    return total_fuel_req


def part_two(filename):
    total_fuel = 0
    for module_mass in _get_mass_list(filename):
        module_fuel = _calculate_fuel(module_mass)
        while module_fuel > 0:
            total_fuel += module_fuel
            module_fuel = _calculate_fuel(module_fuel)
    return total_fuel


if __name__ == '__main__':
    print(part_one('input'))  # 3246455
    print(part_two('input'))  # 4866824
