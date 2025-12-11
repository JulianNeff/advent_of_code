from run_util import run_puzzle
from typing import Dict, List

def parse_data(data):
    return {n: nb.split() for n, nb in (line.split(": ") for line in data.splitlines())}


def count_paths(graph: Dict[str, List[str]], start: str, end: str) -> int:
    memo = {}

    def dfs(node: str) -> int:
        if node == end:
            return 1

        if node in memo:
            return memo[node]

        memo[node] = sum(dfs(neighbor) for neighbor in graph.get(node, []))

        return memo[node]

    return dfs(start)


def part_a(data: str) -> int:
    graph = parse_data(data)
    return count_paths(graph, 'you', 'out')


def part_b(data: str) -> int:
    graph = parse_data(data)

    paths_fft_to_dac = count_paths(graph, 'fft', 'dac')

    if paths_fft_to_dac > 0:
        return (
            count_paths(graph, 'svr', 'fft') *
            paths_fft_to_dac *
            count_paths(graph, 'dac', 'out')
        )
    else:
        return (
            count_paths(graph, 'svr', 'dac') *
            count_paths(graph, 'dac', 'fft') *
            count_paths(graph, 'fft', 'out')
        )


def main():
    examples = [
        ("""aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out""", 5, None),
        ("""svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out
""", None, 2)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()
