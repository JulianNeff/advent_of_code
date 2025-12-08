from run_util import run_puzzle

def parse_data(data):
    # return as int
    return [(i, list(map(int, line.split(',')))) for i, line in enumerate(data.splitlines())]


def get_distances(nodes):
    distances = []
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            n1 = nodes[i]
            n2 = nodes[j]
            x1, y1, z1 = n1[1]
            x2, y2, z2 = n2[1]
            dist = (x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2
            distances.append((dist, i, j))
    distances.sort()
    return distances

def part_a(data):
    nodes = parse_data(data)
    distances = get_distances(nodes)

    connections = 10 if len(nodes) == 20 else 1000
    team = [i for i in range(len(nodes))]

    for connection in range(connections):
        dist, i, j = distances[connection]
        lower = min(team[i], team[j])
        higher = max(team[i], team[j])

        for k in range(len(team)):
            if team[k] == higher:
                team[k] = lower


    team_count = {}
    for member in team:
        if member not in team_count:
            team_count[member] = 0
        team_count[member] += 1

    largest_3_teams = sorted(team_count.values(), reverse=True)[:3]

    return largest_3_teams[0] * largest_3_teams[1] * largest_3_teams[2]


def part_b(data):
    nodes = parse_data(data)
    distances = get_distances(nodes)
    team = [i for i in range(len(nodes))]

    for connection in range(len(distances)):
        dist, i, j = distances[connection]
        lower = min(team[i], team[j])
        higher = max(team[i], team[j])


        for k in range(len(team)):
            if team[k] == higher:
                team[k] = lower

        if all(x == 0 for x in team):
            return nodes[i][1][0] * nodes[j][1][0]


def main():
    examples = [
        ("""162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689""", 40, 25272)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()