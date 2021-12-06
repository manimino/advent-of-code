from collections import Counter


def read_input():
    # for puzzles where each input line is an object
    with open('input.txt') as fh:
        for line in fh.readlines():
            if line.strip():
                yield line.strip()

def main():
    fish = []
    for line in read_input():
        fish = [int(a) for a in line.split(',')]

    fish_before = Counter(fish)
    days = 256

    for d in range(days):
        fish_after = {}
        for f in sorted(fish_before.keys()):
            if f == 0:
                fish_after[6] = fish_after.get(6, 0) + fish_before[f]
                fish_after[8] = fish_after.get(8, 0) + fish_before[f]
            else:
                fish_after[f - 1] = fish_after.get(f - 1, 0) + fish_before[f]
        fish_before = fish_after

    print("total", sum(fish_after.values()))


main()
