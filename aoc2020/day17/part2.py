import numpy as np
import time

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


def count_adj(grid, x, y, z, w):
    xl, yl, zl, wl = grid.shape
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
                for wn in range(-1, 2):
                    if w + wn < 0 or w + wn >= wl:
                        continue
                    if xn==0 and yn==0 and zn==0 and wn==0:  #skip self
                        continue
                    neighbors.append((x + xn, y + yn, z + zn, w+wn))
    count = 0
    for n in neighbors:
        if grid[n] == 1:
            count += 1
    return count


def iter(grid1):
    xl, yl, zl, wl = grid1.shape
    grid2 = np.zeros((xl, yl, zl, wl))
    for x in range(xl):
        for y in range(yl):
            for z in range(zl):
                for w in range(zl):
                    active_adj = count_adj(grid1, x, y, z, w)
                    if grid1[x,y,z,w]==1:
                        if active_adj==2 or active_adj==3:
                            grid2[x,y,z,w]=1
                        else:
                            grid2[x, y, z, w] = 0
                    else:
                        if active_adj == 3:
                            grid2[x,y,z, w]=1
                        else:
                            grid2[x,y,z, w] = 0

    return grid2


def count_active(grid):
    count = 0
    xl, yl, zl, wl = grid.shape
    for x in range(xl):
        for y in range(yl):
            for z in range(zl):
                for w in range(wl):
                    if grid[x,y,z,w]==1:
                        count += 1
    return count


def main():
    # big array
    sz = 30
    grid = np.zeros((sz,sz,sz,sz))
    mid = int(sz/2)
    ox, oy, oz, ow = mid, mid, mid, mid
    yi=0
    for line in read_input():
        grid[ox:ox+len(line), oy+yi, oz, ow] = line
        yi+=1

    t0 = time.time()
    for i in range(6):
        print("t:", round(time.time()-t0, 2))
        print("iter:", i)
        grid = iter(grid)

    print(count_active(grid))

if __name__ == '__main__':
    main()