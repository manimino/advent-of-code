

def read_input():
    # for puzzles where each input line is an object
    with open('input.txt') as fh:
        for line in fh.readlines():
            yield line.strip().split()


def run(ptr, cmds, accum):
    cmd = cmds[ptr][0]
    arg = cmds[ptr][1]
    if cmd=='jmp':
        return ptr+arg, accum
    elif cmd=='nop':
        return ptr+1, accum
    elif cmd=='acc':
        return ptr+1, accum+arg


def main():
    cmds = []
    visited_lines = set()
    for cmd, arg in read_input():
        cmds.append((cmd, int(arg)))
    ptr=0
    accum=0
    visited_lines.add(ptr)
    while True:
        ptr, accum = run(ptr, cmds, accum)
        if ptr in visited_lines:
            break
        visited_lines.add(ptr)
    print(accum)


if __name__ == '__main__':
    main()