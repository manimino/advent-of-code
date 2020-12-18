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
    #end_pos=2020
    end_pos=30000000

    last_pos_of = dict()
    max_pos=0
    data = [2, 15, 0, 9, 1, 20]
    for i, num in enumerate(data[:-1]):
        last_pos_of[num] = i
        max_pos += 1

    t0 = time.time()

    prev_num = data[-1]
    for i in range(max_pos, end_pos+1):
        if i%1000000==0:
            print(round(i/end_pos*100, 2), "% done at", round(time.time()-t0), "seconds")
        #print("looking up", prev_num)
        num = 0
        if prev_num in last_pos_of:
            num = i-last_pos_of[prev_num]
            #print("last pos of ", prev_num, "updated to", i)
        else:
            pass #print("last pos of ", prev_num, "is", i)
        last_pos_of[prev_num] = i
        prev_num = num
        if i==end_pos-2:
            print(">>> result:", prev_num)

    #for k, v in last_pos_of.items():
    #    print("last pos of", k, "is", v)

if __name__ == '__main__':
    main()