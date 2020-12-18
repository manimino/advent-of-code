def read_input():
    # for puzzles where each input line is an object
    with open('input.txt') as fh:
        for line in fh.readlines():
            yield line


def main():
    objs=[]
    for obj in read_input():
        objs.append(int(obj))
    prev = 0
    one_diffs = 0
    three_diffs = 1  # last adapter -> device
    for obj in sorted(objs):
        if prev is not None:
            print(obj, (obj-prev))
            if obj-prev == 1:
                one_diffs += 1
            elif obj-prev == 3:
                three_diffs += 1
        else:
            if obj==1:
                one_diffs+=1
            elif obj==3:
                three_diffs+=1
        prev=obj
    print(one_diffs, three_diffs, one_diffs*three_diffs)
    # 63 36 2268 too low
    # 63 37 2331 too low

if __name__ == '__main__':
    main()