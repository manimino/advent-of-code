
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
    return rows[0]*8+seats[0]


def main():
    # get_row_and_seat('FBFBBFFRLR')
    sids = []
    for rid in read():
        sids.append(get_row_and_seat(rid))
    s_sids = list(sorted(sids))
    for i in range(len(s_sids)-1):
        #print("     ",s_sids[i])
        if s_sids[i+1] == s_sids[i] + 2:
            print(s_sids[i]+1)

if __name__ == '__main__':
    main()