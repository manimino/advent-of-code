def read_input():
    # for puzzles where each input line is an object
    in_rules=True
    in_mine=False
    in_nearby=False
    rules=[]
    nearby=[]
    with open('input.txt') as fh:

        for line in fh.readlines():
            if not line.strip():
                continue

            if line.startswith('your'):
                in_mine = True
                in_rules = False
                in_nearby=False
                continue

            if line.startswith('nearby'):
                in_nearby=True
                in_rules=False
                in_mine=False
                continue

            if in_nearby:
                nl = [int(x) for x in line.strip().split(',')]
                print("nearby", nl)
                nearby.append(nl)

            if in_rules:
                nums_part = line.split(':')[-1]
                ranges = [x.strip() for x in nums_part.strip().split('or')]
                rl = []
                for r in ranges:
                    rmin=int(r.split('-')[0])
                    rmax=int(r.split('-')[1])
                    rl.append([rmin,rmax])
                print("ranges",rl)
                rules.append(rl)
    return rules, nearby


def main():
    rules, nearby = read_input()
    total = 0
    for n in nearby:
        for num in n:
            good_num = False
            for rule in rules:
                if good_num:
                    continue
                for range in rule:
                    if good_num:
                        continue
                    if num >= range[0] and num <= range[1]:
                        # it's good
                        print("valid:", num, range[0], range[1])
                        good_num = True
            if not good_num:
                total += num
    print(total)
    # not 71



if __name__ == '__main__':
    main()