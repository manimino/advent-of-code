def read_input():
    # for puzzles where each input line is an object
    with open('input.txt') as fh:
        for line in fh.readlines():
            line = line.strip().replace('(', '').replace(')','').replace(',', '')
            ing_str, all_str = line.split('contains')
            ings = ing_str.strip().split()
            alls = all_str.strip().split()
            yield ings, alls


def items_in_every_list(ls):
    items = set()
    for l in ls:
        items.update(l)
    result = []
    for i in items:
        in_all = True
        for l in ls:
            if i not in l:
                in_all = False
        if in_all:
            result.append(i)
    return result


def delete_ing(could_be, delete_this):
    for aller in could_be:
        for l in could_be[aller]:
            if delete_this in l:
                l.remove(delete_this)


def find_for_sure(could_be):
    # mutates could_be
    for aller in could_be:
        its_one_of_these = items_in_every_list(could_be[aller])
        if len(its_one_of_these) == 1:
            # found the allergen
            its_this_one = its_one_of_these[0]
            delete_ing(could_be, its_this_one)
            return aller, its_this_one
    return None, None


def main():
    could_be = dict()
    for ings, alls in read_input():
        for all in alls:
            if all in could_be:
                could_be[all].append(ings)
            else:
                could_be[all] = [ings]

    for all in could_be:
        print(all, could_be[all])

    done=False
    matches = {}
    aller_ings = []
    while not done:
        aller, ing = find_for_sure(could_be)
        if aller is None:
            break
        matches[aller] = ing
        aller_ings.append(ing)

    count = 0
    for ings, alls in read_input():
        for i in ings:
            if i not in aller_ings:
                count +=1
    print("\npart 1:")
    print(count)

    sl = []
    for m in sorted(matches.keys()):
        sl.append(matches[m])
    print("\npart 2:")
    print(','.join(sl))



if __name__ == '__main__':
    main()