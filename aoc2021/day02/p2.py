def read_input():
    # for puzzles where each input line is an object
    with open('input.txt') as fh:
        for line in fh.readlines():
            yield line.strip()


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


fwd = 0
depth = 0
aim = 0
i = 0
for obj in read_input():
    d, num = obj.split(' ')
    num = int(num)
    if d == 'forward':
        fwd += num
        depth += aim*num
    if d == 'down':
        aim += num
    if d == 'up':
        aim -= num

print(fwd * depth)