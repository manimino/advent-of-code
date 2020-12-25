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


def main():
    p1, p2 = read_input()
    while len(p1) and len(p2):
        a = p1.pop(0)
        b = p2.pop(0)
        if a > b:
            p1.append(a)
            p1.append(b)
        elif b > a:
            p2.append(b)
            p2.append(a)
    winner = p1
    if not len(winner):
        winner = p2
    print(winner)
    result = 0
    for i in range(len(winner)):
        result += winner[i]*(len(winner)-i)

    print(result)

if __name__ == '__main__':
    main()