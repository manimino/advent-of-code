import time

import numpy as np


def last_spoken(n, arr, k, seen_set):
    if n in seen_set:
        for i in range(k-1,-1,-1):
            if arr[i]==n:
                return k-i
    else:
        return None


def main():
    end_pos=2020
    end_pos=30000000
    print("allocating")
    arr = np.zeros(end_pos+10)
    print("done allocating")
    arr[0:6] = [2, 15, 0, 9, 1, 20]
    i=0
    k=i+5
    seen_set = set(arr[:k])
    t0 = time.time()
    while i < end_pos+1:
        if i%(int(end_pos/300))==10:
            print(round(i/end_pos * 100, 2), "% done in", round(time.time()-t0, 6), "seconds")
        num = last_spoken(arr[k], arr, k, seen_set)
        seen_set.add(arr[k])
        i += 1
        k=i+5
        if num is None:
            arr[k] = (0)
        else:
            arr[k] = (num)
    print(int(arr[end_pos-1]))


if __name__ == '__main__':
    main()