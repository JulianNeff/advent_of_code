from run_util import run_puzzle


def part_a(data):
    red = 12
    green = 13
    blue = 14

    sum = 0
    lines = data.split('\n')
    for line in lines:
        possible = True
        id = int((line.split(':')[0])[5:])
        
        content = line.split(':')[1]
        games = content.split(';')
        for game in games:
            if possible is not True:
                break

            colors = game.split(',')
            for color in colors:
                amount = int(color.split(' ')[1])
                if color.endswith('red') and amount > red:
                    possible = False
                    break
                elif color.endswith('green') and amount > green:
                    possible = False
                    break
                elif color.endswith('blue') and amount > blue:
                    possible = False
                    break
        
        if possible:
            sum += id

    return sum


def part_b(data):
    sum = 0
    lines = data.split('\n')

    for line in lines:
        min_red = 0
        min_green = 0
        min_blue = 0

        content = line.split(':')[1]
        games = content.split(';')
        for game in games:
            colors = game.split(',')
            for color in colors:
                amount = int(color.split(' ')[1])
                if color.endswith('red') and amount > min_red:
                    min_red = amount
                elif color.endswith('green') and amount > min_green:
                    min_green = amount
                elif color.endswith('blue') and amount > min_blue:
                    min_blue = amount

        sum += min_red * min_green * min_blue

    return sum


def main():
    examples = [
        ("""Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green""", 8, None),
    ("""Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
    Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
    Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
    Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green""", None, 2286)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()