from run_util import run_puzzle

def parse_data(data):
    file_map, disk_map = {}, {}
    current_position, id = 0, 0
    is_file = True

    for char in data:
        segment_length = int(char)

        if is_file:
            file_map[id] = (current_position, segment_length)
            for offset in range(segment_length):
                disk_map[current_position + offset] = id
            id += 1

        is_file = not is_file
        current_position += segment_length

    return file_map, disk_map, id


def part_a(data):
    _, disk_map, _ = parse_data(data)
    start, end = 0, max(disk_map.keys())
    
    while start < end:
        if end in disk_map:
            id = disk_map[end]
            del disk_map[end]
            while start in disk_map:
                start += 1
            disk_map[start] = id
        end -= 1

    return sum(position * id for position, id in disk_map.items())


def part_b(data):
    file_map, disk_map, file_count = parse_data(data)

    for id in range(file_count - 1, -1, -1):
        target_position = 0
        while target_position < file_map[id][0]:
            file_length = file_map[id][1]
            if all(target_position + offset not in disk_map for offset in range(file_length)):
                for offset in range(file_length):
                    del disk_map[file_map[id][0] + offset]
                    disk_map[target_position + offset] = id
                break
            target_position += 1

    return sum(position * id for position, id in disk_map.items())


def main():
    examples = [
        ("""2333133121414131402""", 1928, 2858)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()