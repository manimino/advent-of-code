import copy


def read_input():
    # for puzzles where each input line is an object
    in_rules=True
    in_mine=False
    in_nearby=False
    rules=[]
    nearby=[]
    mine = []
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
                #print("nearby", nl)
                nearby.append(nl)

            if in_rules:
                nums_part = line.split(':')[-1]
                ranges = [x.strip() for x in nums_part.strip().split('or')]
                rl = []
                for r in ranges:
                    rmin=int(r.split('-')[0])
                    rmax=int(r.split('-')[1])
                    rl.append([rmin,rmax])
                #print("ranges",rl)
                rules.append(rl)

            if in_mine:
                mine = [int(x) for x in line.strip().split(',')]

    return rules, nearby, mine


def filter_tickets(rules, nearby):
    total = 0
    good_nearby = []
    for n in nearby:
        all_good = True
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
                        #print("valid:", num, range[0], range[1])
                        good_num = True
            if not good_num:
                total += num
                all_good = False
        if all_good:
            good_nearby.append(n)
    return good_nearby


def passes_rule(num, rule):
    good_num = False
    for range in rule:
        if num >= range[0] and num <= range[1]:
            # it's good
            good_num = True
            break
    return good_num


def can_be_field(rules, nearby):
    possible_fields = dict()
    # for each column, check which rules work for it
    for c in range(len(nearby[0])):
        possible_fields[c] = list()

        for i, r in enumerate(rules):
            all_pass_rule = True
            for ticket in nearby:
                if not passes_rule(ticket[c], r):
                    all_pass_rule = False
            if all_pass_rule:
                possible_fields[c].append(i)


    return possible_fields


def csolve(possible_fields):
    skip_keys = []
    while len(skip_keys) < len(possible_fields):
        to_remove = None
        for k, v in possible_fields.items():
            if k in skip_keys:
                continue
            if len(possible_fields[k]) == 1:
                to_remove = possible_fields[k][0]
                skip_keys.append(k)
                break
        if to_remove is not None:
            for k, v in possible_fields.items():
                if k in skip_keys:
                    continue
                if to_remove in v:
                    v.remove(to_remove)

    return possible_fields
    # not 393120


def main():
    rules, nearby, mine = read_input()
    nearby = filter_tickets(rules, nearby)
    possible_fields = can_be_field(rules, nearby)
    possible_fields = csolve(possible_fields)

    for k, v in possible_fields.items():
        print(k, ":", possible_fields[k])
    prod=1

    print('----')
    for k, v in possible_fields.items():
        if possible_fields[k][0] < 6:
            print(k, ":", possible_fields[k])
            idx = k
            prod *= mine[idx]
    print(prod)

    # not 18204492965401

if __name__ == '__main__':
    main()

"""
0 [18]
1 [13]
2 [8]
3 [3]
4 [5]
5 [14]
"""