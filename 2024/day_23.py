from run_util import run_puzzle
import networkx as nx


def parse_data(data):
    return [tuple(line.split('-')) for line in data.strip().split('\n')]


def part_a(data):
    graph = nx.Graph(parse_data(data))
    triangles = [clique for clique in nx.enumerate_all_cliques(graph) if len(clique) == 3]
    return sum(1 for triangle in triangles if any(node.startswith('t') for node in triangle))


def part_b(data):
    graph = nx.Graph(parse_data(data))
    largest_clique = max(nx.find_cliques(graph), key=len)
    return ','.join(sorted(largest_clique))


def main():
    examples = [
        ("""kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn""", 7, "co,de,ka,ta")
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()