import numpy as np
from collections import defaultdict

def read_input():
    # for puzzles where each input line is an object
    with open('input.txt') as fh:
        for line in fh.readlines():
            if line.strip():
                yield line.strip()


def display(d):
    xs = [k[0] for k in d.keys()]
    ys = [k[1] for k in d.keys()]
    mat = np.empty((max(xs)+1, max(ys)+1), dtype=str)
    for k, v in d.items():
        mat[k[0], k[1]] = v
    for m in range(len(mat)):
        for n in range(len(mat[0])):
            if not mat[m, n]:
                mat[m, n] = '.'
    print(mat.T)


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
        #print(x1, y1, x2, y2)
        if x1 == x2:
            # horiz
            if y1 > y2:
                y1, y2 = y2, y1
            for y in range(y1, y2 + 1):
                d[(x1, y)] += 1
        elif y1 == y2:
            # vert
            if x1 > x2:
                x1, x2 = x2, x1
            for x in range(x1, x2+1):
                d[(x, y1)] += 1
        else:
            # diagonal
            length = abs(x2-x1)+1
            if x2 > x1:
                x_sign = 1
            else:
                x_sign = -1
            if y2 > y1:
                y_sign = 1
            else:
                y_sign = -1

            for inc in range(length):
                d[x1+inc*x_sign, y1+inc*y_sign] += 1
    display(d)
    n = 0
    for k, v in d.items():
        if v >= 2:
            n += 1
        #print(k, v)
    return n

print(main())