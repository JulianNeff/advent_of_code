from run_util import run_puzzle
from collections import Counter

map_normal = {"2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6, "8": 7, "9": 8, "T": 9, "J": 10, "Q": 11, "K": 12, "A": 13}
map_j = {"J": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "Q": 11, "K": 12, "A": 13}

class Hand:
    def __init__(self, cards: str, bid: int, part_b):
        assert len(cards) == 5
        self.cards = cards
        self.bid = bid
        self.score = get_type(cards, part_b) * 14 ** 5 + get_score(cards, part_b)


def get_score(cards: str, part_b: bool) -> int:
    card_map = map_j if part_b else map_normal
    return sum(card_map[card] * 14 ** (4 - i) for i, card in enumerate(cards))


def get_type(cards: str, part_b: bool) -> int:
    values = list(Counter(cards).values())

    if part_b and "J" in cards:
        count = cards.count("J")
        values = list(Counter(cards.replace("J", "")).values())
        
        if count >= 4 or (4 in values and count == 1) or (3 in values and count == 2) or (2 in values and count == 3): # Five of a kind
            return 6
        if 4 in values or (3 in values and count == 1) or (2 in values and count == 2) or count == 3: # Four of a kind
            return 5
        if (3 in values and 2 in values) or (values.count(2) == 2 and count == 1): # Full House
            return 4
        if 3 in values or (2 in values and count == 1) or count == 2: # Three of a kind
            return 3
        if values.count(2) == 2 or (2 in values and count == 1): # Two Pair
            return 2
        if 2 in values or count == 1: # One Pair
            return 1

    else:
        if 5 in values: # Five of a kind
            return 6
        if 4 in values: # Four of a kind
            return 5
        if 3 in values and 2 in values: # Full House
            return 4
        if 3 in values: # Three of a kind
            return 3
        if values.count(2) == 2: # Two Pair
            return 2
        if 2 in values: # One Pair
            return 1
    
    return 0


def parse_input(data: str) -> list[tuple[str, int]]:
    return [(line.split()[0], int(line.split()[1])) for line in data.splitlines()]
    

def part_a(data):
    lines = parse_input(data)
    hands = [Hand(hand, bid, False) for hand, bid in lines]
    hands.sort(key=lambda x: x.score)
    return sum(hand.bid * (i + 1) for i, hand in enumerate(hands))


def part_b(data):
    lines = parse_input(data)
    hands = [Hand(hand, bid, True) for hand, bid in lines]
    hands.sort(key=lambda x: x.score)
    return sum(hand.bid * (i + 1) for i, hand in enumerate(hands))


def main():
    examples = [
        ("""32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483""", 6440, 5905)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()