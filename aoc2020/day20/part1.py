import copy
import math

INPUT = 'test_input.txt'

COUNTER = 0
EDGE_NUMS = {}

SIDES = ['up', 'down', 'left', 'right']


def read_input_objs():
    # for puzzles with newline-separated objects as input
    with open(INPUT) as fh:
        obj = []
        num = None
        for line in fh.readlines():
            if not line.strip():
                yield num, obj
                obj = []
            else:
                if line.startswith('Tile'):
                    # first line is Tile: num
                    num_str = line.strip().split(' ')[1]
                    num = num_str.replace(':', '')
                else:
                    obj.append(line.strip())
        if obj:
            yield num, obj


def val(edge_list):
    global EDGE_NUMS
    global COUNTER
    edge = ''.join(edge_list)
    if EDGE_NUMS.get(edge, -1) == -1:
        # new edge
        EDGE_NUMS[edge] = COUNTER
        COUNTER += 1
        return EDGE_NUMS[edge]
    else:
        return EDGE_NUMS[edge]


def edge_values(tile, f, r):
    # get nums for up, down, left, and right edges of a tile
    edges = dict()

    mut_tile = copy.deepcopy(tile)
    if f == 1:
        for i in range(len(mut_tile)):
            mut_tile[i] = ''.join(list(reversed(mut_tile[i])))
        tile = mut_tile

    U = tile[0]
    D = tile[-1]
    L = ''.join([t[0] for t in tile])
    R = ''.join([t[-1] for t in tile])

    if r == 0:
        edges['up']    = U
        edges['right'] = R
        edges['down']  = D
        edges['left']  = L
    elif r == 1:
        edges['up'] = ''.join(list(reversed(L)))
        edges['right'] = U
        edges['down'] = ''.join(list(reversed(R)))
        edges['left'] = D
    elif r == 2:
        edges['up']    = ''.join(list(reversed(D)))
        edges['right'] = ''.join(list(reversed(L)))
        edges['down']  = ''.join(list(reversed(U)))
        edges['left']  = ''.join(list(reversed(R)))
    elif r == 3:
        edges['up'] = R
        edges['right'] = ''.join(list(reversed(D)))
        edges['down'] = L
        edges['left'] = ''.join(list(reversed(U)))

    for x in range(len(tile)):
        print(tile[x])
    print('flip', f, 'rot', r)
    print('up  :', edges['up'])
    print('down:', edges['down'])
    print('left:', edges['left'])
    print('right', edges['right'])
    print('--------')
    for e in edges:
        edges[e] = val(edges[e])
    return edges


def check_matches(matches):
    #check some version of 1951 is above some version of 2729
    def _check(tile1, tile2, direction):
        sat = False
        for e in matches:
            if e.startswith(tile1):
                for f in matches[e][direction]:
                    if f.startswith(tile2):
                        sat = True
        if sat:
            print("verified match:", tile1, tile2, direction)
        assert sat
    _check('2729', '1951', 'up')
    _check('2971', '2729', 'up')
    _check('1427', '2729', 'left')
    #_check('1427', '2311', 'up')


def get_matches(tile_edges, q_tile, q_side, q_tile_num):
    if q_side == 'left':
        m_side = 'right'
    elif q_side == 'right':
        m_side = 'left'
    elif q_side == 'up':
        m_side = 'down'
    elif q_side == 'down':
        m_side = 'up'
    else:
        print('weird side')
    m_tiles = []
    for tile_num in tile_edges:
        if q_tile_num == tile_num:
            continue  # don't match self
        if tile_edges[tile_num][m_side] == q_tile[q_side]:
            m_tiles.append(tile_num)
    return m_tiles


def remove_bad_tiles(matches):
    """
    matches items look like:
    ['2797_13']['up'] = ['1753_10', '1753_12', '1753_13', '2797_11']
    """
    def _is_bad(tm):
        # Are 3 or 4 sides empty?
        count = 0
        for side in SIDES:
            if tm[side]:
                count += 1
        if count < 2:
            return True
        # if only 2 sides, they need to be 'corner' not across from each other
        if count == 2:
            if tm['up'] and tm['down']:
                return True
            if tm['left'] and tm['right']:
                return True
        return False


    removed_any = True
    while removed_any:
        removed_any = False
        for tile_num in list(matches.keys()):
            if _is_bad(matches[tile_num]):
                # tile_num is a bad tile -- delete from everywhere
                removed_any = True
                for tn in matches:
                    for s in SIDES:
                        if tile_num in matches[tn][s]:
                            matches[tn][s].remove(tile_num)
                matches.pop(tile_num)


class Grid():
    def __init__(self, sz, tms):
        self.grid = [[-1]*sz for _ in range(sz)]
        self.sz = sz
        self.avail_tiles = copy.deepcopy(tms)

    def pop_copies(self, tile_num):
        for t in list(self.avail_tiles.keys()):
            if t.split('_')[0] == tile_num.split('_')[0]:
                self.avail_tiles.pop(t)

    def can_place(self, tile_num, row, col):
        tile = self.avail_tiles[tile_num]
        if col > 0:
            # check if can match left
            if self.grid[row][col-1] not in tile['left']:
                return False
        if row > 0:
            # check if matches upward
            if self.grid[row-1][col] not in tile['up']:
                return False
        return True

    def place(self, tile_num, row, col):
        self.grid[row][col] = tile_num
        self.pop_copies(tile_num)

    def solve(self):
        for r in range(self.sz):
            for c in range(self.sz):
                #for y in range(self.sz):
                #    print(self.grid[y])
                #print("")
                if self.grid[r][c] != -1:
                    # already assigned
                    continue
                can_place_any = False
                for t in self.avail_tiles:
                    if self.can_place(t, r, c):
                        can_place_any = True
                        self.place(t, r, c)
                        break
                if not can_place_any:
                    return False
        return True


def solve():
    tile_edges = {}
    anchor_tile = True

    n_tiles = 0
    for _, _ in read_input_objs():
        n_tiles += 1
    grid_size = int(math.sqrt(n_tiles))

    for num, tile in read_input_objs():
        print('\n======\n', num)
        if anchor_tile:
            # The complete puzzle could be arbitrarily rotated / flipped
            # Make one tile an "anchor" tile to force a single orientation for the answer
            tile_edges[num + '_f0r0'] = edge_values(tile, 0, 0)
            anchor_tile = False
        else:
            for f in [0, 1]:
                for r in range(4):
                    tile_edges[num + '_f' + str(f) + 'r' + str(r)] = edge_values(tile, f, r)

    for t in tile_edges:
        if t.endswith('f0r0'):
            print(t, tile_edges[t])

    matches = dict()
    for tile_num in tile_edges:
        matches[tile_num] = dict()
        for side in SIDES:
            matches[tile_num][side] = get_matches(tile_edges, tile_edges[tile_num], side, tile_num)

    if INPUT == 'test_input.txt':
        check_matches(matches)

    remove_bad_tiles(matches)

    if INPUT == 'test_input.txt':
        check_matches(matches)


    """
    for tnum in matches:
        if tnum.startswith('2729'):
            print(tnum, matches[tnum]['down'])
            """
    """
    corner_tiles = []
    for tn in sorted(matches.keys()):
        n_sides = 0
        for s in SIDES:
            if matches[tn][s]:
                n_sides += 1
            print(tn, s, matches[tn][s])
        if n_sides == 2:
            corner_tiles.append(tn.split('_')[0])

    print(len(set(corner_tiles)))
    print(set(corner_tiles))
    """
    n_sols = 0
    for tnum in matches:
        g = Grid(grid_size, matches)
        g.place(tnum, 0, 0)
        if g.solve():
            n_sols += 1
            print("SOLUTION:")
            for row in g.grid:
                print(row)
            return g.grid
    if n_sols == 0:
        print("NO SOLUTIONS")


def main():
    grid = solve()
    prod = 1
    for w in [grid[0][0], grid[0][-1], grid[-1][-1], grid[-1][0]]:
        prod *= int(w.split('_')[0])
    print(prod)


if __name__ == '__main__':
    main()