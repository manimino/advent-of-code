import copy
import time


def read_input():
    # for puzzles where each input line is an object
    with open('input.txt') as fh:
        i=0
        for line in fh.readlines():
            if i==0:
                cups = [int(t) for t in list(line.strip())]
            if i==1:
                n_moves = int(line)
            i += 1
        return cups, n_moves


def move(cups, cur_pos):
    n_cups = len(cups)
    new_cups = [None] * n_cups

    # pick next 3 cups
    next_cups = []
    for i in range(3):
        next_pos = (cur_pos + i + 1) % n_cups
        next_cups.append(cups[next_pos])

    # determine tgt_cup
    t = -1
    cur_cup = cups[cur_pos]
    while True:
        tgt_cup = cur_cup + t
        if tgt_cup < 1:
            tgt_cup += n_cups
        if tgt_cup not in next_cups and tgt_cup in cups:
            tgt_cup_idx = cups.index(tgt_cup)
            break
        t -= 1

    # target cup is in same place as it was
    new_cups[tgt_cup_idx] = tgt_cup

    # put next_cups in after the target
    for n in range(3):
        idx = (tgt_cup_idx + n + 1) % len(new_cups)
        new_cups[idx] = next_cups[n]

    # fill in remaining cups
    for i in range(tgt_cup_idx, tgt_cup_idx + len(cups)):
        from_idx = i % len(cups)
        if cups[from_idx] in new_cups:
            continue
        for j in range(from_idx, from_idx + len(cups)):
            to_idx = j % len(cups)
            if new_cups[to_idx] is None:
                new_cups[to_idx] = cups[from_idx]
                break
    new_pos = (new_cups.index(cur_cup) + 1) % len(new_cups)
    return new_cups, new_pos


def to_str(cups, cur_pos, move_num):
    s = []
    zero_idx = (cur_pos - move_num - 1) % len(cups)
    for c in range(zero_idx, zero_idx+len(cups)):
        if c == cur_pos:
            s.append('(' + str(cups[c % len(cups)]) + ')')
        else:
            s.append(str(cups[c % len(cups)]))
    return ''.join(s)


def main():
    cups, n_moves = read_input()
    print(to_str(cups, 0, 0))

    cur_pos = 0
    for move_num in range(n_moves):
        cups, cur_pos = move(cups, cur_pos)
        print(cups)
        #print(to_str(cups, cur_pos, move_num))

    s = to_str(cups, cur_pos, move_num)
    s = s.replace('(','').replace(')','')
    idx = s.index('1')
    result = s[idx+1:] + s[:idx]
    print('answer', result)

if __name__ == '__main__':
    main()