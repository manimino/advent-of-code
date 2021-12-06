import numpy as np

def read_input():
    # for puzzles where each input line is an object
    with open('input.txt') as fh:
        for line in fh.readlines():
            if line.strip():
                yield line.strip()


def keep_most_common(mat, pos):
    arr = np.array(mat, dtype='int')
    if sum(arr[:, pos]) >= arr.shape[0]/2:
        most_common = '1'
    else:
        most_common = '0'

    ret = []
    for row in mat:
        if row[pos] == most_common:
            ret.append(row)
    return ret

def keep_least_common(mat, pos):
    if len(mat) == 1:
        return mat
    arr = np.array(mat, dtype='int')
    if sum(arr[:, pos]) >= arr.shape[0]/2:
        least_common = '0'
    else:
        least_common = '1'

    ret = []
    for row in mat:
        if row[pos] == least_common:
            ret.append(row)
    return ret

print('first thing')
mat = []
for line in read_input():
    mat.append(list(line))

for pos in range(len(mat[0])):
    mat = keep_most_common(mat, pos)
    print(mat)
print(mat)
a = int(''.join(mat[0]), 2)


print('second thing')
mat = []
for line in read_input():
    mat.append(list(line))

for pos in range(len(mat[0])):
    mat = keep_least_common(mat, pos)
    print(mat)
print(mat)
b = int(''.join(mat[0]), 2)

print(a, b)
print(a*b)