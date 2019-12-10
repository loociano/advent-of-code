import math


def get_map(file):
    map = []
    with open(file) as f:
        for line in f.readlines():
            map_line = []
            for x in line.rstrip():
                map_line.append(x)
            map.append(map_line)
    return map


def find_asteroid(map, width, height, x, y, dx, dy):
    pos_x = x + dx
    pos_y = y + dy
    while width > pos_x >= 0 and height > pos_y >= 0:
        if map[pos_y][pos_x] == '#':
            return True
        pos_x += dx
        pos_y += dy
    return False


def normalize(x, y):
    gcd = math.gcd(x, y)
    return '{} {}'.format(x // gcd, y // gcd)


def calc_directions(width, height):
    dirs = set()
    for w in range(-width + 1, width):
        for h in range(-height, height):
            if not(w == 0 and h == 0):
              dirs.add(normalize(w, h))
    return dirs


def part_one():
    max_asteroids = 0
    map = get_map('input')
    width = len(map[0])
    height = len(map)
    dirs = calc_directions(width, height)
    for y in range(0, height):
        for x in range(0, width):
            if map[y][x] == '#':
                count_asteroids = 0
                for dir in dirs:
                    dx, dy = dir.split(' ')
                    if find_asteroid(map, width, height, x, y, int(dx), int(dy)):
                        count_asteroids += 1
                max_asteroids = max(max_asteroids, count_asteroids)
    return max_asteroids


print(part_one())
