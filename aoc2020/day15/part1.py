

def last_spoken(n, arr):
    if n in arr:
        rev_arr = list(reversed(arr))
        res = rev_arr.index(n) + 1
        return res
    else:
        print(0)
        return None


def main():
    arr=[2, 15, 0, 9, 1, 20]
    i=0
    while i < 2021:
        num = last_spoken(arr[-1], arr[:-1])
        if num is None:
            arr.append(0)
        else:
            arr.append(num)
        i += 1
    print(arr)
    print(arr[2019])


if __name__ == '__main__':
    main()