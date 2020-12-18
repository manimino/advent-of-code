
def read():
    with open('input.txt') as fh:
        for line in fh.readlines():
            yield line


def get_row_and_seat(id):
    rows = list(range(128))
    seats = list(range(8))
    for i in range(7):
        if id[i] == 'B':
            rows = rows[int(len(rows)/2):]
        else:
            rows = rows[:int(len(rows)/2)]
    for i in range(7,10):
        if id[i] == 'R':
            seats = seats[int(len(seats)/2):]
        else:
            seats = seats[:int(len(seats)/2)]
    return rows[0], seats[0]


def main():
    # get_row_and_seat('FBFBBFFRLR')
    biggest = 0
    for rid in read():
        r, s = get_row_and_seat(rid)
        sid = r*8+s
        if sid > biggest:
            biggest = sid
    print(biggest)

if __name__ == '__main__':
    main()