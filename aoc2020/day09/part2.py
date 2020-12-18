
def read_input():
    # for puzzles where each input line is an object
    with open('input.txt') as fh:
        for line in fh.readlines():
            yield int(line.strip())


def find_range_that_sums_to(num, buf):
    for i in range(len(buf)):
        for j in range(i+1, len(buf)):
            if sum(buf[i:j])>num:
                break
            if sum(buf[i:j])==num:
                print(i, j, buf[i:j])
                print(min(buf[i:j])+max(buf[i:j]))
    print("onoz")


def main():
    buf=[]
    for num in read_input():
        buf.append(num)
        if num==144381670:
            find_range_that_sums_to(num, buf)


if __name__ == '__main__':
    main()