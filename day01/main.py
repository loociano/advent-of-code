import math

with open('input') as mass_list:
    total_fuel_req = 0
    for mass in mass_list:
        total_fuel_req += math.floor(int(mass) / 3) - 2
    print(total_fuel_req)