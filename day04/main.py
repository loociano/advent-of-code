def has_repeated_adjacent(number):
    number_str = str(number)
    digit = number_str[0]
    for i in range(1, 6):
        if number_str[i] == digit:
            return True
        else:
            digit = number_str[i]
    return False


def has_a_double_adjacent(number):
    number_str = str(number)
    digit = number_str[0]
    count = 1
    for i in range(1, 6):
        if number_str[i] == digit:
            count += 1
        else:
            if count == 2:
                return True
            digit = number_str[i]
            count = 1
    return count == 2


def is_non_decreasing(number):
    number_str = str(number)
    digit = number_str[0]
    for i in range(1, 6):
        if number_str[i] < digit:
            return False
        digit = number_str[i]
    return True


def part_one(start, end):
    count = 0
    for num in range(start, end + 1):
        if has_repeated_adjacent(num) and is_non_decreasing(num):
            count += 1
    return count


def part_two(start, end):
    count = 0
    for num in range(start, end + 1):
        if has_a_double_adjacent(num) and is_non_decreasing(num):
            count += 1
    return count


print(part_one(256310, 732736))
print(part_two(256310, 732736))
