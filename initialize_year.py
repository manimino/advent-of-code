import os

boilerplate = """
def read_input():
    # for puzzles where each input line is an object
    # with open('input.txt') as fh:  
    with open('test_input.txt') as fh:  
        for line in fh.readlines():
            if line.strip():
                yield line.strip()


def read_input_objs():
    # for puzzles with newline-separated objects as input
    # with open('input.txt') as fh:  
    with open('test_input.txt') as fh:  
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
    for line in read_input():
        pass

    for line in read_input_objs():
        pass

main()
"""

for i in range(1, 26):
    s = 'day' + str(i).zfill(2)
    d = os.getcwd() + os.sep + s
    if os.path.isdir(d):
        print("hey, this year's already initialized")
        break
    else:
        os.makedirs(d)
    for fi in ['input.txt', 'test_input.txt', 'part1.py', 'part2.py']:
        fn = d + os.sep + fi
        print(fn)
        with open(fn, 'w') as fh:
            if fi.startswith('part'):
                fh.write(boilerplate)
            else:
                fh.write('')
