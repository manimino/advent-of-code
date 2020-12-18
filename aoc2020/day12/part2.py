def read_input():
    # for puzzles where each input line is an object
    with open('input.txt') as fh:
        for line in fh.readlines():
            yield line


def turn(wp, direction, deg):
    new_wp=[0,0]
    for i in range(int(deg/90)):
        # find new Y
        if wp[0]>0:
            if direction=='R':
                new_wp[1]=-wp[0]
            elif direction=='L':
                new_wp[1]=wp[0]
        else:
            if direction=='R':
                new_wp[1]=-wp[0]
            elif direction=='L':
                new_wp[1]=wp[0]

        # find new X
        if wp[1]>0:
            if direction=='R':
                new_wp[0]=wp[1]
            if direction=='L':
                new_wp[0]=-wp[1]
        else:
            if direction=='R':
                new_wp[0]=wp[1]
            if direction=='L':
                new_wp[0]=-wp[1]

        wp[0] = new_wp[0]
        wp[1] = new_wp[1]
    return wp

"""
print("turn([10,1],'R',90)",turn([10,1],'R',90))
print("turn([10,1],'L',90)",turn([10,1],'L',90))
print("turn([-10,1],'R',90)",turn([-10,1],'R',90))
print("turn([10,-1],'L',90)",turn([10,-1],'L',90))
print("turn([-10,-1],'L',90)",turn([-10,-1],'L',90))
print("turn([-10,-1],'R',90)",turn([-10,-1],'R',90))
"""


def forward(pos, wp, times):
    print("moving",wp,"*",times)
    pos[0] += wp[0]*times
    pos[1] += wp[1]*times


def main():
    pos=[0,0]
    wp=[10,1]

    for obj in read_input():
        print("--------\npos:",pos,"wp:",wp)
        print("cmd:", obj)
        d_char = obj[0]
        num = int(obj[1:])

        if d_char == 'F':
            forward(pos, wp, num)
            continue

        # handle turns
        if d_char in ['L', 'R']:
            wp=turn(wp, d_char, num)
            continue

        # move waypoint
        d=[0,0]
        if d_char=='E':
            d = [num, 0]
        elif d_char == 'W':
            d = [-num, 0]
        elif d_char=='N':
            d=[0,num]
        elif d_char=='S':
            d = [0, -num]
        wp[0]+=d[0]
        wp[1]+=d[1]
    print("end pos:", pos, "manhattan:", abs(pos[0])+abs(pos[1]))


if __name__ == '__main__':
    main()