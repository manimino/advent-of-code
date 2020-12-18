
"""
any 3-skip breaks the problem into 2 subproblems (before and after the 3-skip)
so like:
[1,2,5,6,7]
becomes
(0->1, 1->2), (0->2) 2 ways
(2->5) 1 way
(5->6, 6->7), (5->7) 2 ways
(6->9) 1 way

all together, 2*1*2*1=4 possible paths
yeah we can just split and count probably
"""


def read_input():
    # for puzzles where each input line is an object
    with open('input.txt') as fh:
        objs=[]
        for line in fh.readlines():
            objs.append(int(line.strip()))
    objs.append(0)
    objs.append(max(objs)+3)
    return list(sorted(objs))


def count_paths(objs, path_so_far=None):
    paths=0
    i=0
    if path_so_far is None:
        path_so_far = []

    path_so_far.append(objs[i])
    if i == len(objs)-1:
        # we're asking "how many ways can we get to this point"
        print(path_so_far)
        return 1
    if i+1 < len(objs) and objs[i+1] <= objs[i]+3:
        # can we move to the next number?
        paths += count_paths(objs[i+1:], path_so_far)
    if i+2 < len(objs) and objs[i+2] <= objs[i]+3:
        # can we move to the +2?
        paths += count_paths(objs[i+2:], path_so_far)
    if i+3 < len(objs) and objs[i+3] <= objs[i]+3:
        # can we move to the +3?
        paths += count_paths(objs[i+3:], path_so_far)
    return paths


def main():
    paths=1
    begin=0
    objs=read_input()
    for i in range(len(objs)):
        if i>1 and (objs[i]-objs[i-1])==3:
            paths *= count_paths(objs[begin:i])
            begin=i
    print("total paths", paths)


if __name__ == '__main__':
    main()