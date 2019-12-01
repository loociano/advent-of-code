import math


def calculate_fuel(mass):
    return math.floor(int(mass) / 3) - 2


with open('input') as mass_list:
    total_fuel = 0
    for module_mass in mass_list:
        module_fuel = calculate_fuel(module_mass)
        while module_fuel > 0:
            total_fuel += module_fuel
            module_fuel = calculate_fuel(module_fuel)
    print(int(total_fuel))
