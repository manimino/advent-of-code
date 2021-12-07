
def read_input():
    # for puzzles where each input line is an object
    with open('input.txt') as fh:
        for line in fh.readlines():
            if line.strip():
                yield line.strip()


def main():
    for line in read_input():
        crabs = [int(x) for x in line.split(',')]

    min_pos = min(crabs)
    max_pos = max(crabs)
    best = float('inf')
    for p in range(min_pos, max_pos+1):
        print(p)
        tot = 0
        for c in crabs:
            tot += abs(c - p)
        if tot < best:
            best = tot
    return best

print(main())