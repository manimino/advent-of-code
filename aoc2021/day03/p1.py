import numpy as np

def read_input():
    # for puzzles where each input line is an object
    with open('input.txt') as fh:
        for line in fh.readlines():
            if line.strip():
                yield line.strip()

def main():
    ok = [list(r) for r in read_input()]
    arr = np.array(ok, dtype='int')
    print(arr.shape)
    gamma = ''
    eps = ''
    for i in range(arr.shape[1]):
        if arr[:,i].sum() > 500:
            gamma += '0'
            eps += '1'
        else:
            gamma += '1'
            eps += '0p2'
    print(int(gamma, 2) * int(eps, 2))

main()