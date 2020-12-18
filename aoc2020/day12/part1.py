def read_input():
    # for puzzles where each input line is an object
    with open('input.txt') as fh:
        for line in fh.readlines():
            yield line

def turn(facing, direction, deg):
    new_facing=[0,0]
    for i in range(int(deg/90)):
        if abs(facing[0])==1:
            new_facing[0]=0
            if direction=='R':
                new_facing[1]=facing[0]*1
            elif direction=='L':
                new_facing[1]=facing[0]*-1
        elif abs(facing[1])==1:
            new_facing[1]=0
            if direction=='R':
                new_facing[0]=facing[1]*-1
            if direction=='L':
                new_facing[0]=facing[1]*1
        facing[0] = new_facing[0]
        facing[1] = new_facing[1]
    return facing


def facing_chr(facing):
    if facing==[0,1]:
        return '>'
    if facing==[1,0]:
        return '^'
    if facing==[0,-1]:
        return '<'
    if facing==[-1,0]:
        return 'v'


def test_turn():
    for direction in ['L','R']:
        for f0 in [-1,0,1]:
            for f1 in [-1,0,1]:
                if abs(f0)+abs(f1)!=1:
                    continue
                print(facing_chr([f0,f1]),
                      direction,
                      facing_chr(turn([f0,f1], direction, deg)))


def add(pos, d, mag):
    print("moving",d,"*",mag)
    pos[0] += d[0]*mag
    pos[1] += d[1]*mag


def main():
    pos=[0,0]
    facing=[0,1]

    for obj in read_input():
        print("--------\npos:",pos,"facing:",facing_chr(facing))
        print(obj)
        d_char = obj[0]
        mag = int(obj[1:])

        # handle turns
        if d_char in ['L', 'R']:
            print(facing_chr(facing), "+", obj)
            facing=turn(facing, d_char, mag)
            print(facing_chr(facing))
            continue

        # move in direction
        d=[0,0]
        if d_char=='E':
            d=[0,1]
        elif d_char == 'W':
            d = [0, -1]
        elif d_char=='N':
            d = [1, 0]
        elif d_char=='S':
            d = [-1, 0]
        elif d_char=='F':
            d = facing
        add(pos, d, mag)
    print("end pos:", pos, "manhattan:", abs(pos[0])+abs(pos[1]))


if __name__ == '__main__':
    main()
    # 800 too low