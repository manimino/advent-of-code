
def read():
    for dx in [1, 3, 5, 7]:
        x = 0
        tree = 0
        with open('input.txt') as fh:
            first_line = True
            for line in fh.readlines():
                if first_line:
                    first_line = False
                    continue
                x = (x + dx) % len(line.strip())

                if line[x] == '#':
                    tree += 1
        print(dx, tree)


def read_dy2():
    for dx in [1]:
        x = 0
        tree = 0
        with open('input.txt') as fh:
            first_line = True
            i = 0
            for line in fh.readlines():
                if first_line:
                    first_line = False
                    continue
                i += 1
                x = (x + dx) % len(line.strip())
                if i % 2 == 1:
                    # "going down 2"
                    continue

                if line[x] == '#':
                    tree += 1
        print("for dy=2")
        print(dx, tree)


if __name__ == '__main__':
    read()
    read_dy2()
    print(62*184*80*74*36)