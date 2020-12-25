import copy
"""
we can map to a 2D grid like so:

   b       c
a a b     c      (even line
 a a b a c a a   (odd line)
a a a b c a a    (even line)
 1 2 3 b
      c b
     c   b

just need to render as a brick-pattern
each tile has x, y, linenum
if linenum is even, going sw is (x-1, y+1) and se is (x, y+1)
if linenum is odd, going sw is (x, y+1) and se is (x+1, y+1)

the center tile is on line 0 (even).
"""

def get_coords(move, is_odd_line):
    if move == 'e':
        return 1, 0
    elif move == 'w':
        return -1, 0
    else:
        if is_odd_line == 1:
            if move == 'sw':
                return 0, 1
            elif move == 'se':
                return 1, 1
            elif move == 'nw':
                return 0, -1
            elif move == 'ne':
                return 1, -1
        else:
            # even line
            # if linenum is even, going sw is (x-1, y+1) and se is (x, y+1)
            if move == 'sw':
                return -1, 1
            elif move == 'se':
                return 0, 1
            elif move == 'nw':
                return -1, -1
            elif move == 'ne':
                return 0, -1
    print('uhoh')


def read_input():
    # for puzzles where each input line is an object
    with open('input.txt') as fh:
        for line in fh.readlines():
            line = line.strip()
            i = 0
            moves = []
            while i < len(line):
                if line[i] in ['e', 'w']:
                    moves.append(line[i])
                    i+=1
                elif line[i] in ['n', 's']:
                    moves.append(line[i:i+2])
                    i+=2
            yield moves


def get_neighbors(pos):
    # get neighbor pos list
    neighbors = [(pos[0]-1, pos[1]),
                 (pos[0]+1, pos[1])]
    if pos[1] % 2 == 1:
        # odd row -- neighbors are x+0 and x+1
        neighbors.extend([
            (pos[0]+1, pos[1]+1),
            (pos[0], pos[1]+1),
            (pos[0]+1, pos[1]-1),
            (pos[0], pos[1]-1),
        ])
    else:
        # even row -- neighbors are x+0 and x-1
        neighbors.extend([
            (pos[0]-1, pos[1]+1),
            (pos[0], pos[1]+1),
            (pos[0]-1, pos[1]-1),
            (pos[0], pos[1]-1),
        ])
    return neighbors


def count_black_white_neighbors(tiles, pos):
    n_black = 0
    n_white = 0
    for n in get_neighbors(pos):
        if n not in tiles:
            n_white += 1
        elif not tiles[n]:
            n_black += 1
        else:
            n_white += 1
    return n_black, n_white


def create_tiles():
    tiles = {(0, 0): True}
    for obj in read_input():
        pos = [0,0]
        for move in obj:
            dx, dy = get_coords(move, pos[1] % 2)
            pos[0] += dx
            pos[1] += dy
            if tuple(pos) not in tiles:
                tiles[tuple(pos)] = True
        # flip target
        tiles[tuple(pos)] = not tiles[tuple(pos)]
    print('orig black tiles:', count_black_tiles(tiles))
    return tiles


def count_black_tiles(tiles):
    n_black = 0
    for pos in tiles:
        if not tiles[pos]:
            n_black += 1
    return n_black


def main():
    tiles = create_tiles()
    n_days = 100
    for d in range(n_days):
        print(d, len(tiles), count_black_tiles(tiles))
        new_tiles = dict()

        tiles_to_process = set()
        for t in tiles:
            for n in get_neighbors(t):
                tiles_to_process.add(n)
            tiles_to_process.add(t)  # probably does nothing but hey

        for t in tiles_to_process:
            n_b, n_w = count_black_white_neighbors(tiles, t)
            if t in tiles and not tiles[t]:
                # it's black
                if n_b == 0 or n_b > 2:
                    new_tiles[t] = True
                else:
                    new_tiles[t] = False
            else:
                # it's white
                if n_b == 2:
                    new_tiles[t] = False
                else:
                    new_tiles[t] = True
        tiles = new_tiles

    print('part2 black tiles:', count_black_tiles(tiles))


if __name__ == '__main__':
    main()