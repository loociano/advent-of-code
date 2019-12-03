import sys


def _get_wires(filename):
    with open(filename) as file:
        return list(file.readline().rstrip().split(',')), list(file.readline().rstrip().split(','))


def _paint_path(area_dict, delay_dict, wire, mark, with_delay):
    min_dist = sys.maxsize
    x = 0
    y = 0
    delay = 0
    for i in range(len(wire)):
        next = wire[i]
        dir = next[0:1]
        steps = int(next[1:])
        for j in range(steps):
            if dir == 'R':
                x += 1
            elif dir == 'L':
                x -= 1
            elif dir == 'U':
                y += 1
            else:
                y -= 1
            delay += 1
            key = "{} {}".format(x, y)
            if area_dict.get(key) is None or area_dict[key] == mark:
                area_dict[key] = mark
                delay_dict[key] = delay
            else:
                if with_delay:
                    dist = delay_dict.get(key) + delay
                else:
                    dist = abs(x) + abs(y)
                if dist < min_dist:
                    min_dist = dist
    return min_dist


def part_one():
    wire1, wire2 = _get_wires('input')
    area_dict = {}
    delay_dict = {}
    _paint_path(area_dict, delay_dict, wire1, 1, False)
    return _paint_path(area_dict, delay_dict, wire2, 2, False)


def part_two():
    wire1, wire2 = _get_wires('input')
    area = {}
    delay = {}
    _paint_path(area, delay, wire1, 1, True)
    return _paint_path(area, delay, wire2, 2, True)


print(part_one())
print(part_two())
