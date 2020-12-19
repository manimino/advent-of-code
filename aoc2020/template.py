def read_input():
    # for puzzles where each input line is an object
    with open('input.txt') as fh:
        for line in fh.readlines():
            yield line


def read_input_objs():
    # for puzzles with newline-separated objects as input
    with open('input.txt') as fh:
        obj = []
        for line in fh.readlines():
            if not line.strip():
                yield ' '.join(obj).strip()
                obj = []
            else:
                obj.append(line.strip())
        if obj:
            yield obj


def main():
    for obj in read_input():
        pass


if __name__ == '__main__':
    main()