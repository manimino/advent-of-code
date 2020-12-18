import numpy as np


def read_input():
    # for puzzles where each input line is an object
    with open('input.txt') as fh:
        for line in fh.readlines():
            ln = []
            for c in line.strip():
                if c == '#':
                    ln.append(1)
                else:
                    ln.append(0)
            yield ln


def count_adj(grid, x, y, z):
    xl, yl, zl = grid.shape
    neighbors = []
    for xn in range(-1, 2):
        if x + xn < 0 or x + xn >= xl:
            continue
        for yn in range(-1, 2):
            if y + yn < 0 or y + yn >= yl:
                continue
            for zn in range(-1, 2):
                if z + zn < 0 or z + zn >= zl:
                    continue
                if xn==0 and yn==0 and zn==0:  #skip self
                    continue
                neighbors.append((x + xn, y + yn, z + zn))
    count = 0
    for n in neighbors:
        if grid[n] == 1:
            count += 1
    return count


def iter(grid1):
    xl, yl, zl = grid1.shape
    grid2 = np.zeros((xl, yl, zl))
    for x in range(xl):
        for y in range(yl):
            for z in range(zl):
                active_adj = count_adj(grid1, x, y, z)
                if grid1[x,y,z]==1:
                    if active_adj==2 or active_adj==3:
                        grid2[x,y,z]=1
                    else:
                        grid2[x, y, z] = 0
                else:
                    if active_adj == 3:
                        grid2[x,y,z]=1
                    else:
                        grid2[x,y,z] = 0

    return grid2


def print_grid(grid):
    xl, yl, zl = grid.shape
    for z in range(zl):
        print("z=", z)
        print(grid[:,:,z].T)


def count_active(grid):
    count = 0
    xl, yl, zl = grid.shape
    for x in range(xl):
        for y in range(yl):
            for z in range(zl):
                if grid[x,y,z]==1:
                    count += 1
    return count


def main():
    # big array
    sz = 40
    grid = np.zeros((sz,sz,sz))
    mid = int(sz/2)
    ox, oy, oz = mid, mid, mid
    yi=0
    for line in read_input():
        grid[ox:ox+len(line), oy+yi, oz] = line
        yi+=1
    print_grid(grid)

    for i in range(6):
        grid = iter(grid)

    print(count_active(grid))

if __name__ == '__main__':
    main()