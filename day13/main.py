from common.intcode import Intcode


def _get_program(file):
    with open(file) as f:
        return list(map(int, f.read().split(',')))


def part_one(filename: str):
    block_tile_count = 0
    vm = Intcode(_get_program(filename))
    while True:
        x = vm.run()
        if x is None:
            break
        y = vm.run()
        tile_id = vm.run()
        block_tile_count += 1 if tile_id == 2 else 0
    return block_tile_count


print(part_one('input'))
