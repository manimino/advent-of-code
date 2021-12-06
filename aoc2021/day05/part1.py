from collections import defaultdict

def read_input():
    # for puzzles where each input line is an object
    with open('input.txt') as fh:
        for line in fh.readlines():
            if line.strip():
                yield line.strip()


def main():
    d = defaultdict(lambda: 0)
    for line in read_input():
        l, r = line.split(' -> ')
        l1, l2 = l.split(',')
        r1, r2 = r.split(',')
        x1 = int(l1)
        y1 = int(l2)
        x2 = int(r1)
        y2 = int(r2)
        if x1 > x2:
            x1, x2 = x2, x1
        if y1 > y2:
            y1, y2 = y2, y1
        #print(x1, y1, x2, y2)
        if x1 != x2 and y1 != y2:
            continue
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                d[(x,y)] += 1
    n = 0
    for k, v in d.items():
        if v >= 2:
            n += 1
        print(k, v)
    return n

print(main())