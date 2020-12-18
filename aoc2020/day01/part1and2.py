
ls = []
with open('input.txt') as fh:
    for line in fh.readlines():
        if not line.strip():
            continue
        ls.append(int(line))

for i in range(len(ls)):
    for j in range(i+1, len(ls)):
        if ls[i] + ls[j] == 2020:
            print("part1:")
            print(ls[i], ls[j])
            print(ls[i] * ls[j])
        for k in range(j + 1, len(ls)):
            if ls[i]+ls[j]+ls[k]==2020:
                print("\npart2:")
                print(ls[i], ls[j], ls[k])
                print(ls[i]*ls[j]*ls[k])
