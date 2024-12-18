from run_util import run_puzzle

def parse_data(data):
    return [list(line) for line in data.splitlines()]


def part_a(data):
    data = parse_data(data)
    rows, cols = len(data), len(data[0])
    visited = [[0] * cols for _ in range(rows)]

    score = 0
    for i, line in enumerate(data):
        for j, char in enumerate(line):
            if visited[i][j]:
                continue

            area = 0
            perimeter = 0
            queue = [(i, j)]

            while queue:
                x, y = queue.pop()

                if visited[x][y]:
                    continue
                visited[x][y] = 1
                area += 1

                p = 4
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols:
                        if data[nx][ny] == char:
                            p -= 1
                            if not visited[nx][ny]:
                                queue.append((nx, ny))
                perimeter += p

            score += perimeter * area

    return score


def part_b(data):
    data = parse_data(data)
    rows, cols = len(data), len(data[0])
    visited = [[0] * cols for _ in range(rows)]

    score = 0
    for i in range(rows):
        for j in range(cols):
            if visited[i][j]:
                continue

            area = 0
            perimeter = 0
            char = data[i][j]
            queue = [(i, j)]

            while queue:
                x, y = queue.pop()

                if visited[x][y]:
                    continue
                visited[x][y] = 1
                area += 1

                up = x > 0 and data[x - 1][y] == char
                down = x < rows - 1 and data[x + 1][y] == char
                left = y > 0 and data[x][y - 1] == char
                right = y < cols - 1 and data[x][y + 1] == char

                if up and not visited[x - 1][y]:
                    queue.append((x - 1, y))
                if down and not visited[x + 1][y]:
                    queue.append((x + 1, y))
                if left and not visited[x][y - 1]:
                    queue.append((x, y - 1))
                if right and not visited[x][y + 1]:
                    queue.append((x, y + 1))

                # Check if (x, y) is an inwards corner
                if up and left and data[x - 1][y - 1] != char:
                    perimeter += 1
                if up and right and data[x - 1][y + 1] != char:
                    perimeter += 1
                if down and left and data[x + 1][y - 1] != char:
                    perimeter += 1
                if down and right and data[x + 1][y + 1] != char:
                    perimeter += 1

                # Skip if (x, y) is part of a line
                if (up and down) or (left and right):
                    continue
                
                neighbors = up + down + left + right
                if neighbors == 2:
                    perimeter += 1
                if neighbors == 1:
                    perimeter += 2
                if neighbors == 0:
                    perimeter += 4
            
            score += perimeter * area
    return score



def main():
    examples = [
        ("""RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE""", 1930, 1206)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()