import copy
import sys
import threading

from collections import defaultdict


def read_input():
    # for puzzles where each input line is an object
    with open('input.txt') as fh:
        decks = [[], []]
        cur_player = 0
        for line in fh.readlines():
            if not line.strip():
                cur_player = 1
                continue
            if line.startswith('P'):
                continue
            decks[cur_player].append(int(line.strip()))
        return decks[0], decks[1]


def winner(deck):
    result = 0
    print("end result", deck)
    for i in range(len(deck)):
        result += deck[i]*(len(deck)-i)
    print(result)


ROUND = [1]*1000000
NEXT_GAME_NUM = 2
GAME_STACK = [1]


def round(p1, p2, states):
    global ROUND, GAME_STACK, NEXT_GAME_NUM
    print("\n--- Round {}".format(ROUND[GAME_STACK[-1]]), "(Game {}) ---".format(GAME_STACK[-1]))
    ROUND[GAME_STACK[-1]] += 1
    print(p1, p2)

    # check for repeat
    state = ','.join([str(x) for x in p1]) + '|' + ','.join([str(x) for x in p2])
    if state in states[GAME_STACK[-1]]:
        print("INSTANT WIN!", state)
        return p1, p2, 1
    else:
        states[GAME_STACK[-1]].add(state)

    if not len(p1):
        return p1, p2, 2
    if not len(p2):
        return p1, p2, 1
    a = p1.pop(0)
    b = p2.pop(0)
    if len(p1) >= a and len(p2) >= b:
        # recurse
        print('playing subgame')
        GAME_STACK.append(NEXT_GAME_NUM)
        NEXT_GAME_NUM += 1
        _, _, subgame_result = round(copy.copy(p1[0:a]), copy.copy(p2[0:b]), states)
        GAME_STACK.pop(-1)
        if subgame_result == 1:
            print("  subgame result", 1, "p1 gets", a, b)
            p1.append(a)
            p1.append(b)
            return round(p1, p2, states)
        elif subgame_result == 2:
            print("  subgame result:", 2, "p2 gets:", b, a)
            p2.append(b)
            p2.append(a)
            return round(p1, p2, states)
    else:
        # can't recurse - round goes to higher valued card
        if a > b:
            p1.append(a)
            p1.append(b)
        elif b > a:
            p2.append(b)
            p2.append(a)
        return round(p1, p2, states)


def main():
    p1, p2 = read_input()
    n_cards = len(p1) + len(p2)

    states = defaultdict(lambda: set())
    p1, p2, game_win = round(copy.copy(p1), copy.copy(p2), states)

    win_deck = p1
    if game_win == 2:
        win_deck = p2

    # sanity checks
    assert len(win_deck) == n_cards
    for i in range(n_cards):
        assert i+1 in win_deck

    winner(win_deck)


if __name__ == '__main__':
    sys.setrecursionlimit(100000)
    threading.stack_size(200000000)
    thread = threading.Thread(target=main)
    thread.start()
    # 34886 too low
    # 34886 still too low FUCK
    # 30274 too low