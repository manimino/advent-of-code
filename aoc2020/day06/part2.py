def read():
    obj=[]
    with open('input.txt') as fh:
        for line in fh.readlines():
            if not line.strip():
                yield len(obj), ' '.join(obj)
                obj=[]
            else:
                obj.append(line.strip())


def main():
    sumall=0
    for n, obj in read():
        if not obj.strip():
            continue
        yesses = {c: 0 for c in list('qwertyuiopasdfghjklzxcvbnm')}
        for c in obj:
            if c in yesses:
                yesses[c]+=1
        sum=0
        for k,v in yesses.items():
            if v==n:
                sum+=1
        sumall += sum
    print(sumall)


if __name__ == '__main__':
    main()