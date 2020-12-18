import copy


def read_input():
    # for puzzles where each input line is an object
    with open('input.txt') as fh:
        for line in fh.readlines():
            yield line.strip()


def get_n_adj(o,p,lines):
    n_adj=0

    # --- check up ---
    i=o
    j=p
    while i>0:
        if lines[i-1][j] == 'L':
            break
        if lines[i-1][j] == '#':
            n_adj += 1
            break
        i-=1

    i=o
    j=p
    while i > 0 and j>0:
        if lines[i-1][j-1] == 'L':
            break
        if lines[i-1][j-1] == '#':
            n_adj+=1
            break
        i-=1
        j-=1

    i=o
    j=p
    while i > 0 and j < len(lines[i-1])-1:
        if lines[i-1][j+1] == 'L':
            break
        if lines[i-1][j+1] == '#':
            n_adj+=1
            break
        i-=1
        j+=1

    # --- check down ---
    i=o
    j=p
    while i<len(lines)-1:
        if lines[i+1][j] == 'L':
            break
        if lines[i+1][j] == '#':
            n_adj += 1
            break
        i+=1

    i=o
    j=p
    while i < len(lines) - 1 and j>0:
        if lines[i+1][j-1] == 'L':
            break
        if lines[i+1][j-1] == '#':
            n_adj+=1
            break
        i+=1
        j-=1

    i=o
    j=p
    while i < len(lines) - 1 and j < len(lines[i+1])-1:
        if lines[i+1][j+1] == 'L':
            break
        if lines[i+1][j+1] == '#':
            n_adj+=1
            break
        j+=1
        i+=1

    #check left
    i=o
    j=p
    while j>0:
        if lines[i][j-1] == 'L':
            break
        if lines[i][j-1] == '#':
            n_adj+=1
            break
        j-=1

    #check right
    i=o
    j=p
    while j<len(lines[i])-1:
        if lines[i][j+1] == 'L':
            break
        if lines[i][j+1] == '#':
            n_adj+=1
            break
        j+=1
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
                if n_adj>=5:
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

    kk=0
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
        kk+=1


if __name__ == '__main__':
    main()