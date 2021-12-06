
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


    for d in range(100):
        print(d, len(fish))
        for fi in range(len(fish)):
            if fish[fi] == 0:
                fish.append(8)
                fish[fi] = 6
            else:
                fish[fi] -= 1
    return fish


fish = main()
print(len(fish))
