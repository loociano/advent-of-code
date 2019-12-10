import math
from functools import cmp_to_key


def get_map(file):
    map = []
    with open(file) as f:
        for line in f.readlines():
            map_line = []
            for x in line.rstrip():
                map_line.append(x)
            map.append(map_line)
    return map


def find_asteroid_pos(map, width, height, x, y, dx, dy):
    pos_x = x + dx
    pos_y = y + dy
    while width > pos_x >= 0 and height > pos_y >= 0:
        if map[pos_y][pos_x] == '#':
            return [pos_x, pos_y]
        pos_x += dx
        pos_y += dy
    return None


def normalize(x, y):
    gcd = math.gcd(x, y)
    return tuple([x // gcd, y // gcd])


def cmp_vector_angle(a, b):
    ah = math.sqrt(a[0] * a[0] + a[1] * a[1])
    bh = math.sqrt(b[0] * b[0] + b[1] * b[1])
    return 1 if math.asin(a[1] / ah) > math.asin(b[1] / bh) else -1


def get_first_quadrant(width, height):
    dirs = set()
    for w in range(1, width):
        for h in range(-height + 1, 0):
            dirs.add(normalize(w, h))
    return sorted(dirs, key=cmp_to_key(cmp_vector_angle))


def get_second_quadrant(width, height):
    dirs = set()
    for w in range(-width + 1, 0):
        for h in range(-height + 1, 0):
            dirs.add(normalize(w, h))
    return sorted(dirs, key=cmp_to_key(cmp_vector_angle), reverse=True)


def get_third_quadrant(width, height):
    dirs = set()
    for w in range(-width + 1, 0):
        for h in range(1, height):
            dirs.add(normalize(w, h))
    return sorted(dirs, key=cmp_to_key(cmp_vector_angle), reverse=True)


def get_fourth_quadrant(width, height):
    dirs = set()
    for w in range(1, width):
        for h in range(1, height):
            dirs.add(normalize(w, h))
    return sorted(dirs, key=cmp_to_key(cmp_vector_angle))


def calc_directions(width, height):
    sorted_dirs = []
    sorted_dirs.append(normalize(0, -height))  # Top
    sorted_dirs.extend(get_first_quadrant(width, height))
    sorted_dirs.append(normalize(width - 1, 0))  # Right
    sorted_dirs.extend(get_fourth_quadrant(width, height))
    sorted_dirs.append(normalize(0, height))  # Bottom
    sorted_dirs.extend(get_third_quadrant(width, height))
    sorted_dirs.append(normalize(-width, 0))  # Left
    sorted_dirs.extend(get_second_quadrant(width, height))
    return sorted_dirs


def get_monitoring_station_position(filename):
    best_position = None
    max_asteroids = 0
    map = get_map('input')
    width = len(map[0])
    height = len(map)
    directions = calc_directions(width, height)
    for y in range(0, height):
        for x in range(0, width):
            if map[y][x] == '#':
                count_asteroids = 0
                for vector in directions:
                    pos = find_asteroid_pos(map, width, height, x, y, vector[0], vector[1])
                    if pos is not None:
                        count_asteroids += 1
                if count_asteroids > max_asteroids:
                    max_asteroids = count_asteroids
                    best_position = [x, y]
    return max_asteroids, best_position


def part_one(filename):
    return get_monitoring_station_position(filename)[0]


def part_two(filename, vaporized_num):
    map = get_map('input')
    width, height = len(map[0]), len(map)
    directions = calc_directions(width, height)
    max_asteroids, station_pos = get_monitoring_station_position(filename)
    vaporized_count = 0
    while vaporized_count < vaporized_num:
        for vector in directions:
            asteroid_pos = find_asteroid_pos(map, width, height, station_pos[0], station_pos[1], vector[0], vector[1])
            if asteroid_pos is not None:
                map[asteroid_pos[1]][asteroid_pos[0]] = '.'  # vaporized
                vaporized_count += 1
                if vaporized_count == vaporized_num:
                    return asteroid_pos[0] * 100 + asteroid_pos[1]


print(part_one('input'))  # 276
print(part_two('input', 200))  # 1321
