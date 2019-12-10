import math


def _get_map(file):
    map = []
    with open(file) as f:
        for line in f.readlines():
            map_line = []
            for x in line.rstrip():
                map_line.append(x)
            map.append(map_line)
    return map


def _find_asteroid_pos(map, width, height, x, y, dx, dy):
    pos_x = x + dx
    pos_y = y + dy
    while width > pos_x >= 0 and height > pos_y >= 0:
        if map[pos_y][pos_x] == '#':
            return [pos_x, pos_y]
        pos_x += dx
        pos_y += dy
    return None


def _normalize(x, y):
    gcd = math.gcd(x, y)
    return tuple([x // gcd, y // gcd])


def _cmp_vector_angle(vector_a):
    ah = math.sqrt(vector_a[0] * vector_a[0] + vector_a[1] * vector_a[1])
    return math.asin(vector_a[1] / ah)


def _get_quadrant_dirs(range_x, range_y, is_angle_negative):
    dirs = set()
    for w in range_x:
        for h in range_y:
            if w == 0 and h == 0:
                continue
            dirs.add(_normalize(w, h))
    return sorted(dirs, key=_cmp_vector_angle, reverse=is_angle_negative)


def _calc_directions(width, height):
    sorted_dirs = []
    # Clockwise order: quadrant 1, 4, 3 and 2
    range_x = [range(0, width), range(0, width), range(-width, 0), range(-width, 0)]
    range_y = [range(-height, 0), range(0, height), range(0, height), range(-height, 0)]
    negative_angle = [False, False, True, True]
    for q in range(0, 4):
        sorted_dirs.extend(_get_quadrant_dirs(range_x[q], range_y[q], negative_angle[q]))
    return sorted_dirs


def _get_monitoring_station_position(filename):
    best_position = None
    max_asteroids = 0
    map = _get_map(filename)
    width = len(map[0])
    height = len(map)
    directions = _calc_directions(width, height)
    for y in range(0, height):
        for x in range(0, width):
            if map[y][x] == '#':
                count_asteroids = 0
                for vector in directions:
                    pos = _find_asteroid_pos(map, width, height, x, y, vector[0], vector[1])
                    if pos is not None:
                        count_asteroids += 1
                if count_asteroids > max_asteroids:
                    max_asteroids = count_asteroids
                    best_position = [x, y]
    return max_asteroids, best_position


def part_one(filename):
    return _get_monitoring_station_position(filename)[0]


def part_two(filename, vaporized_num):
    map = _get_map('input')
    width, height = len(map[0]), len(map)
    directions = _calc_directions(width, height)
    max_asteroids, station_pos = _get_monitoring_station_position(filename)
    vaporized_count = 0
    while vaporized_count < vaporized_num:
        for vector in directions:
            asteroid_pos = _find_asteroid_pos(map, width, height, station_pos[0], station_pos[1], vector[0], vector[1])
            if asteroid_pos is not None:
                map[asteroid_pos[1]][asteroid_pos[0]] = '.'  # vaporized
                vaporized_count += 1
                if vaporized_count == vaporized_num:
                    return asteroid_pos[0] * 100 + asteroid_pos[1]


print(part_one('input'))  # 276
print(part_two('input', 200))  # 1321
