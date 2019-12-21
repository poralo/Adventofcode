# 387638-919123

def check_for_adj_digit(number):
    n = list(str(number))
    for digit1, digit2 in zip(n[:-1], n[1:]):
        if digit1 == digit2:
            return True
    
    return False

def check_for_decrease(number):
    n = list(str(number))
    last_digit = int(n[-1])
    for digit in reversed(n):
        digit = int(digit)
        if digit > last_digit:
            return False
        last_digit = digit
    
    return True

if __name__ == "__main__":
    passwords = []
    for i in range(387638, 919123 + 1):
        if check_for_adj_digit(i) and check_for_decrease(i):
            passwords.append(i)

    print(f'There is {len(passwords)} different passwords which meet the criteria.')