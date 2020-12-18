import copy


def read_input():
    # for puzzles where each input line is an object
    with open('input.txt') as fh:
        for line in fh.readlines():
            yield line.strip()


def get_n_adj(i,j,lines):
    n_adj=0
    if i>0:
        # check up
        if lines[i-1][j] == '#':
            n_adj += 1
        if j>0:
            if lines[i-1][j-1] == '#':
                n_adj+=1
        if j < len(lines[i-1])-1:
            if lines[i-1][j+1] == '#':
                n_adj+=1
    if i<len(lines)-1:
        # check down
        if lines[i+1][j] == '#':
            n_adj += 1
        if j>0:
            if lines[i+1][j-1] == '#':
                n_adj+=1
        if j < len(lines[i+1])-1:
            if lines[i+1][j+1] == '#':
                n_adj+=1
    #check left
    if j>0:
        if lines[i][j-1] == '#':
            n_adj+=1
    #check right
    if j<len(lines[i])-1:
        if lines[i][j+1] == '#':
            n_adj+=1
    return n_adj


def pp(lines):
    for line in lines:
        print(''.join(line))
    print('')


def iter(lines):
    flip=[copy.deepcopy(line) for line in lines]
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            flip[i][j] = lines[i][j]
            n_adj = get_n_adj(i,j,lines)
            if lines[i][j]=='L':
                if n_adj==0:
                    flip[i][j]='#'
            if lines[i][j]=='#':
                if n_adj>=4:
                    flip[i][j]='L'
    pp(flip)
    return flip


def eq(lines, flip):
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] != flip[i][j]:
                return False
    return True


def main():
    lines=[]
    for line in read_input():
        lines.append(list(line))

    while True:
        flip=iter(lines)
        if eq(lines, flip):
            count=0
            for i in range(len(lines)):
                for j in range(len(lines[i])):
                    if lines[i][j]=='#':
                        count+=1
            print(count)
            break
        lines=flip


if __name__ == '__main__':
    main()