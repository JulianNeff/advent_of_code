from run_util import run_puzzle


def parse_input(input_string: str) -> (list, dict):
    sections = input_string.split('\n\n')
    seeds = list(map(int, sections[0].split()[1:]))

    maps = []
    for mapping_section in sections[1:]:
        lines = mapping_section.splitlines()
        maps.append([tuple(map(int, line.split())) for line in lines[1:]])

    return seeds, maps


def part_a(data: str) -> int:
    seeds, maps = parse_input(data)

    locations = []
    for val in seeds:
        for mapping in maps:
            for dest, src, size in mapping:
                if src <= val < src + size:
                    val = dest + val - src
                    break
        
        locations.append(val)

    return min(locations)


def part_b(data: str) -> int:
    seeds, maps = parse_input(data)
    locations = []

    for start, val_range in zip(seeds[::2], seeds[1::2]):
        val_ranges = [range(start, start + val_range)]

        for mapping in maps:
            new_ranges = []
            for r in val_ranges:
                new_vals = []

                while len(r) > 0:
                    used = False
                    new_r = len(r)
                    for dst, src, size in mapping:
                        if src <= r[0] < src+size:
                            used = True
                            new_len = min(size - r[0] + src, len(r))
                            new_vals.append(range(dst + r[0] - src, dst + r[0] - src + new_len))
                            r = r[new_len:]
                            break
                        elif src < r[0]:
                            new_r = min(new_r,  r[0] - src)

                    if not used:
                        new_vals.append(r[:new_r])
                        r = r[new_r:]
                new_ranges.extend(new_vals)

            val_ranges = new_ranges
        locations += val_ranges

    return min(r.start for r in locations)


def main():
    examples = [
        ("""seeds: 79 14 55 13

    seed-to-soil map:
    50 98 2
    52 50 48

    soil-to-fertilizer map:
    0 15 37
    37 52 2
    39 0 15

    fertilizer-to-water map:
    49 53 8
    0 11 42
    42 0 7
    57 7 4

    water-to-light map:
    88 18 7
    18 25 70

    light-to-temperature map:
    45 77 23
    81 45 19
    68 64 13

    temperature-to-humidity map:
    0 69 1
    1 0 69

    humidity-to-location map:
    60 56 37
    56 93 4""", 35, 46),
    ]

    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()