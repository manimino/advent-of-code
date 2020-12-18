import copy


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
    orig_cmds = []
    for cmd, arg in read_input():
        orig_cmds.append([cmd, int(arg)])
    target=len(orig_cmds)-1
    for i in range(len(orig_cmds)):
        # setup
        cmds = copy.deepcopy(orig_cmds)
        if cmds[i][0] == 'nop':
            cmds[i][0] = 'jmp'
        elif cmds[i][0] == 'jmp':
            cmds[i][0] = 'nop'

        # see if the new instruction set works
        visited_lines = set()
        ptr = 0
        accum = 0
        visited_lines.add(ptr)
        while True:
            ptr, accum = run(ptr, cmds, accum)
            if ptr in visited_lines:
                # not the right answer
                print("     not", i)
                break
            visited_lines.add(ptr)
            if ptr==target:
                print("FOUND IT", i, "answer", accum)
                break


if __name__ == '__main__':
    main()