def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a, m):
    """
    (a*?)%m==1
    """
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def read_input():
    # for puzzles where each input line is an object

    with open('input.txt') as fh:
        arr_time = int(fh.readline().strip())
        bus_ids = [int(x) for x in fh.readline().strip().split(',') if x!='x']
        return arr_time, bus_ids


def main():
    arr_time, bus_ids = read_input()
    print(arr_time, bus_ids)
    earliest_times={}
    for bid in bus_ids:
        for i in range(0,bid):  # times to try
            t=arr_time+i
            if t%bid==0:
                earliest_times[bid]=t
                break

    tmin=9999999999
    best_id=0
    for k,v in earliest_times.items():
        if v < tmin:
            best_id=k
            tmin=v
    print(best_id, tmin, best_id*(tmin-arr_time))



if __name__ == '__main__':
    main()