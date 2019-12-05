def has_repeated_adjacent(num):
    number_str = str(num)
    last_digit = number_str[0]
    for digit in number_str[1:]:
        if digit == last_digit:
            return True
        else:
            last_digit = digit
    return False


def has_a_double_adjacent(num):
    number_str = str(num)
    last_digit = number_str[0]
    group_len = 1
    for digit in number_str[1:]:
        if digit == last_digit:
            group_len += 1
        else:
            if group_len == 2:
                return True
            last_digit = digit
            group_len = 1
    return group_len == 2


def is_non_decreasing(num):
    number_str = str(num)
    last_digit = number_str[0]
    for digit in number_str[1:]:
        if digit < last_digit:
            return False
        last_digit = digit
    return True


def part_one(start, end):
    return len([num for num in range(start, end + 1) if
                has_repeated_adjacent(num) and is_non_decreasing(num)])


def part_two(start, end):
    return len([num for num in range(start, end + 1) if
                has_a_double_adjacent(num) and is_non_decreasing(num)])


print(part_one(256310, 732736))  # 979
print(part_two(256310, 732736))  # 635
