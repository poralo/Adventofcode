import math


def find_fuel_required(mass):
    return math.floor(mass / 3) - 2

def total_fuel_required(modules_file):
    fuel_needed_by_modules = []
    with open(modules_file, 'r') as f:
        for mass in f.readlines():
            mass = int(mass)
            
            fuel_needed = find_fuel_required(mass)
            fuel_required = find_fuel_required(fuel_needed)
            while fuel_required > 0:
                fuel_needed += fuel_required
                fuel_required = find_fuel_required(fuel_required)
            
            fuel_needed_by_modules.append(fuel_needed)

    return sum(fuel_needed_by_modules)


if __name__ == "__main__":
    print(f'The total fuel required is {total_fuel_required("test.txt")}')