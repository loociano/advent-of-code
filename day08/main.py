import sys


def _get_image_pixels(file):
    with open(file) as f:
        return list(map(int, f.read()))


def _get_layer_with_fewest_zeros(freq_list):
    result = -1
    min_zeros = sys.maxsize
    for freq in freq_list:
        if freq[0] < min_zeros:
            min_zeros = freq[0]
            result = freq
    return result


def part_one(width, height):
    pixels = _get_image_pixels('input')
    layer = -1
    freq_list = []
    for i, pixel in enumerate(pixels):
        if i % (width * height) == 0:
            layer += 1
            freq_list.append([0 for i in range(0, 10)])
        freq_list[layer][pixel] += 1

    result_layer = _get_layer_with_fewest_zeros(freq_list)
    return result_layer[1] * result_layer[2]


def part_two(width, height):
    pixels = _get_image_pixels('input')
    num_layers = int(len(pixels) / (width * height))
    message = []
    for row in range(0, height):
        line_str = []
        for col in range(0, width):
            color = 2  # transparent
            for l in range(0, num_layers):
                color = pixels[(l * width * height) + (width * row) + col]
                if color == 0 or color == 1:  # black or white
                    break
            line_str.append('X' if color == 1 else ' ')
        message.append(''.join(line_str))
    return '\n'.join(message)


print(part_one(25, 6))
print(part_two(25, 6))
