
def read_input():
    # for puzzles where each input line is an object
    with open('input.txt') as fh:
        for line in fh.readlines():
            yield int(line.strip())


def is_sum_of_two_in(num, buf):
    for i in range(len(buf)):
        for j in range(i+1,len(buf)):
            if num==buf[i]+buf[j]:
                return True
    return False


def main():
    buf=[0]*25
    bufptr=0
    full=False
    for num in read_input():
        if full:
            if not is_sum_of_two_in(num, buf):
                print(num)
                return
        buf[bufptr]=num
        if bufptr==24:
            full=True
        bufptr=(bufptr+1)%25


if __name__ == '__main__':
    main()