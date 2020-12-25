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



def main():
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
        print(pos, tiles[tuple(pos)])


    n_black = 0
    for pos in tiles:
        if not tiles[pos]:
            n_black += 1
    print(n_black)

if __name__ == '__main__':
    main()