import math


def find_fuel_required(mass):
    return math.floor(mass / 3) - 2

if __name__ == "__main__":
    summ = 0
    with open('input.txt', 'r') as f:
        for mass in f.readlines():
            mass = int(mass)
            summ += find_fuel_required(mass)
            print(f'Required fuel: {find_fuel_required(mass)}  |  Total fuel: {summ}')

    print(f'The total fuel requiredis {summ}')