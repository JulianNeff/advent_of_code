from run_util import run_puzzle
from collections import deque
from typing import List

class AhoCorasick:
    def __init__(self, patterns: List[str] = None):
        self.trie = [{}]
        self.fail = [0]
        self.outputs = [set()]

        if patterns:
            for pattern in patterns:
                self.add(pattern)
            self.build()

    def add(self, pattern: str):
        node = 0
        for char in pattern:
            if char not in self.trie[node]:
                self.trie.append({})
                self.fail.append(0)
                self.outputs.append(set())
                self.trie[node][char] = len(self.trie) - 1
            node = self.trie[node][char]
        self.outputs[node].add(len(pattern))

    def build(self):
        queue = deque(self.trie[0].values())

        while queue:
            node = queue.popleft()
            for char, next_node in self.trie[node].items():
                queue.append(next_node)
                fail = self.fail[node]
                while fail and char not in self.trie[fail]:
                    fail = self.fail[fail]
                self.fail[next_node] = self.trie[fail].get(char, 0)
                self.outputs[next_node] |= self.outputs[self.fail[next_node]]

    def find(self, text: str):
        matches = [set() for _ in text]
        node = 0

        for i, char in enumerate(text):
            while node and char not in self.trie[node]:
                node = self.fail[node]
            node = self.trie[node].get(char, 0)
            matches[i] = self.outputs[node]

        return matches

def count_ways(automaton: AhoCorasick, designs: List[str]):
    results = []

    for design in designs:
        matches = automaton.find(design)
        n = len(design)
        ways = [1] + [0] * n

        for i in range(n):
            for length in matches[i]:
                prev = i + 1 - length
                if prev >= 0:
                    ways[i + 1] += ways[prev]

        results.append(ways[n])

    return results

def parse_data(data: str):
    lines = [line for line in data.splitlines() if line.strip()]
    patterns = lines[0].split(", ")
    designs = lines[1:]
    return AhoCorasick(patterns), designs


def part_a(data: str):
    aho_corasick, designs = parse_data(data)
    return sum(w > 0 for w in count_ways(aho_corasick, designs))


def part_b(data: str):
    aho_corasick, designs = parse_data(data)
    return sum(count_ways(aho_corasick, designs))


def main():
    examples = [
        ("""r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb""", 6, 16)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()