from run_util import run_puzzle


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x]) 
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)
    

def parse_data(data):
    return [tuple(map(int, line.split(','))) for line in data.strip().splitlines()]


def part_a(data):
    memory = parse_data(data)
    size = 71
    bytes = 1024

    grid = [[0 for _ in range(size)] for _ in range(size)]
    distances = [[-1 for _ in range(size)] for _ in range(size)]

    for i, (x, y) in enumerate(memory):
        if i < bytes:
            grid[x][y] = 1

    queue = [(0, 0)]
    distances[0][0] = 0
    dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    while queue:
        x, y = queue.pop(0)

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < size and 0 <= ny < size and grid[nx][ny] == 0:
                if distances[nx][ny] == -1:
                    queue.append((nx, ny))
                    distances[nx][ny] = distances[x][y] + 1

    return distances[size-1][size-1]


def to_index(x, y, size):
    return x * size + y


def part_b(data):
    memory = parse_data(data)
    size = 71

    def is_path_blocked(mid):
        uf = UnionFind(size * size)
        grid = [[0] * size for _ in range(size)]
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        for i in range(mid + 1):
            x, y = memory[i]
            grid[x][y] = 1

        for x in range(size):
            for y in range(size):
                if grid[x][y] == 0:
                    index = to_index(x, y, size)
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < size and 0 <= ny < size and grid[nx][ny] == 0:
                            uf.union(index, to_index(nx, ny, size))

        return not uf.connected(to_index(0, 0, size), to_index(size - 1, size - 1, size))

    left, right = 0, len(memory) - 1
    result = None

    while left <= right:
        mid = (left + right) // 2
        if is_path_blocked(mid):
            result = mid
            right = mid - 1
        else:
            left = mid + 1

    x, y = memory[result]
    return f"{x},{y}"


def main():
    examples = [
        ("""5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0""", None, None)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()