from functools import reduce
from math import gcd


def read_input():
    # for puzzles where each input line is an object

    with open('input.txt') as fh:
        arr_time = int(fh.readline().strip())
        bus_ids=[]
        for c in fh.readline().strip().split(','):
            if c!='x':
                bus_ids.append(int(c))
            else:
                bus_ids.append(0)
        return arr_time, bus_ids


def test_sat(bus_ids, t):
    for i in range(len(bus_ids)):
        if bus_ids[i]!=0:
            if (t+i)%bus_ids[i]==0:
                print("Yep..",(t),"%", bus_ids[i],"=",(t)%bus_ids[i])
            else:
                print("Nope.",(t),"%", bus_ids[i],"=",(t)%bus_ids[i], "not", 0)


def lcm(numbers):
    return reduce((lambda x, y: int(x * y / gcd(x, y))), numbers)


def solve(bus_ids):
    # comes up with A valid solution

    t=bus_ids[0]
    print("found: {}%{}==0".format(t, bus_ids[0]))
    for i in range(1,len(bus_ids)):
        t+=1
        if bus_ids[i]==0:
            continue

        prev_mods=[z for z in bus_ids[0:i] if z!=0]
        inc=lcm(prev_mods)
        while (t % bus_ids[i]) != 0:
            t += inc
        print("found: {}%{}==0".format(t, bus_ids[i]))

    return t+1-len(bus_ids)


def main():
    _, bus_ids = read_input()
    t = solve(bus_ids)

    test_sat(bus_ids, t)
    print("answer",t)


if __name__ == '__main__':
    main()