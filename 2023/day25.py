from run_util import run_puzzle

import networkx as nx
import matplotlib.pyplot as plt

def create_graph(data):
    graph = nx.Graph()
    lines = data.splitlines()
    for line in lines:
        src, tar = line.split(':')
        tar = tar[1:].split(' ')
        for t in tar:
            graph.add_edge(src, t)
            graph.add_edge(t, src)
    return graph

def part_a(data):
    graph = create_graph(data)

    nx.draw(graph, with_labels=True)
    plt.show()

    graph.remove_edge('zhg', 'fmr')
    graph.remove_edge('rgv', 'jct')
    graph.remove_edge('krf', 'crg')

    result = 1
    for g in nx.connected_components(graph):
        result *= len(g)
    return result


def part_b(data):
    return 0


def main():
    examples = [
        ("""jqt: rhn xhk nvd
rsh: frs pzl lsr
xhk: hfx
cmg: qnr nvd lhk bvb
rhn: xhk bvb hfx
bvb: xhk hfx
pzl: lsr hfx nvd
qnr: nvd
ntq: jqt hfx bvb xhk
nvd: lhk
lsr: lhk
rzs: qnr cmg lsr rsh
frs: qnr lhk lsr""", None, None)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()