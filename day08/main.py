import sys


def get_image_pixels(file):
    with open(file) as f:
        return list(map(int, f.read()))


def get_layer_fewest_zeros(freq_list):
    result = -1
    min_zeros = sys.maxsize
    for freq in freq_list:
        if freq[0] < min_zeros:
            min_zeros = freq[0]
            result = freq
    return result


def part_one(width, height):
    pixels = get_image_pixels('input')
    layer = -1
    freq_list = []
    for i, pixel in enumerate(pixels):
        if i % (width * height) == 0:
            layer += 1
            freq_list.append([0 for i in range(0, 10)])
        freq_list[layer][pixel] += 1

    result_layer = get_layer_fewest_zeros(freq_list)
    return result_layer[1] * result_layer[2]


print(part_one(25, 6))

