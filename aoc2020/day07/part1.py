def read_input():
    # for puzzles where each input line is an object
    with open('input.txt') as fh:
        for line in fh.readlines():
            yield line.strip()


def read_input_objs():
    # for puzzles with newline-separated objects as input
    with open('input.txt') as fh:
        obj = []
        for line in fh.readlines():
            if not line.strip():
                yield ' '.join(obj).strip()
                obj = []
            else:
                obj.append(line.strip())
        if obj:
            yield obj


contains = dict()
contained_by = dict()

"""
Example:
contains = {
  outer_color: [{inner_1: 3, inner_2: 4}] 
}

contained_by = {
  inner_1: [{outer_color: 3}],
  inner_2: [{outer_color: 4}]
}
"""


def add_rule(outer_color, inner_color, inner_num):
    if outer_color not in contains:
        contains[outer_color] = []
    contains[outer_color].append({inner_color: inner_num})
    if inner_color not in contained_by:
        contained_by[inner_color] = []
    contained_by[inner_color].append({outer_color: inner_num})


def build_dicts():
    for obj in read_input():
        outer, inner = obj.split(' bags contain ')
        outer = outer.strip()
        inner_list = inner.strip().replace('.', '').split(',')
        for inn in inner_list:
            inn = inn.replace('bags', '').replace('bag', '').strip()
            if inn.startswith('no other'):
                continue
            num = int(inn.split()[0])
            color = ' '.join(inn.split()[1:])
            add_rule(outer, color, num)


def find_containers_for(color):
    # recurses
    outers = []
    if color not in contained_by:
        return outers
    for csd in contained_by[color]:
        cs = list(csd.keys())[0]
        outers.append(cs)
        outers.extend(find_containers_for(cs))
    return outers


def main():
    build_dicts()
    outers = find_containers_for('shiny gold')
    for i in range(len(outers)):
        print(outers[i])
    print("answer:", len(set(outers)))


if __name__ == '__main__':
    main()