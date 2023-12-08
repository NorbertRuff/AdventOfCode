from utils import read_file

"""
- Five of a kind, where all five cards have the same label: AAAAA
- Four of a kind, where four cards have the same label and one card has a different label: AA8AA
- Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
- Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
- Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
- One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
- High card card, where all cards' labels are distinct: 23456
"""

cards_list = {'High card': [], 'One pair': [], 'Two pair': [], 'Three of a kind': [], 'Full house': [],
              'Four of a kind': [], 'Five of a kind': []}


def check_card(cards):
    original_cards = len(cards)
    num_cards = len(set(cards))
    if num_cards == original_cards:
        cards_list['High card'].append(cards)
    elif num_cards == 1:
        cards_list['Five of a kind'].append(cards)
    elif num_cards == 2:
        for card in cards:
            if cards.count(card) == 3:
                cards_list['Full house'].append(cards)
                break
            if cards.count(card) == 4:
                cards_list['Four of a kind'].append(cards)
                break

    elif num_cards == 3:
        added = False
        for card in cards:
            if cards.count(card) == 3:
                cards_list['Three of a kind'].append(cards)
                added = True
                break
        if not added:
            cards_list['Two pair'].append(cards)

    else:
        cards_list['One pair'].append(cards)


def part1_resolver(raw_data):
    bid = {}
    cards = []
    for line in raw_data:
        line = line.split()
        cards.append(line[0])
        bid[line[0]] = int(line[1])

    for card in cards:
        check_card(card)

    curr = 1
    result = 0

    ranks = {'A': 13, 'K': 12, 'Q': 11, 'J': 10, 'T': 9, '9': 8, '8': 7, '7': 6, '6': 5, '5': 4, '4': 3, '3': 2, '2': 1}

    for house in cards_list.keys():
        cards_list[house].sort(
            key=lambda x: (ranks[x[0]], ranks[x[1]], ranks[x[2]], ranks[x[3]], ranks[x[4]]))
        for idx, card in enumerate(cards_list[house]):
            result += bid[card] * (idx + curr)

        curr += len(cards_list[house])

    return result


def part2_resolver(cards):
    pass
    # joker = cards.count('J')
    # if joker == 0:
    #     key = check_card(cards)
    # house = {card: cards.count(card) for card in cards if card != 'J'}
    # card_list = [card for card in house.keys()]
    # card_list.sort(key=lambda x: house[x], reverse=True)
    # if not card_list:
    #     key = '5 kind'
    # else:
    #     new_cards = cards.replace('J', card_list[0])
    #     key = check_card(new_cards)
    # cards_list[key].append(cards)
    # return key


if __name__ == '__main__':
    raw_data = read_file('./input.txt').splitlines()
    first_part_result = part1_resolver(raw_data)
    print('first_part_result', first_part_result)
    second_part_result = part2_resolver(raw_data)
    print('second_part_result', second_part_result)
