from day22.inputs import inlist
from day22.cutit import inv_cut_all, cut_all
from day22.dealit import inv_deal_all, deal_all
from day22.dealincr import inv_deal_increment_all, deal_increment_all
from day22.util import list_eq

"""
OK, we have all the inverse functions.
Let's see if we can invert day 1's result (4086 -> 2019.)
"""


def do_day1():
    # avoid allocating ram for each transform by just having two lists and switching src and dest each time.
    piles = [list(range(10007)), list(range(10007))]
    for i, item in enumerate(inlist):
        if i % 2 == 0:
            src, dest = piles[0], piles[1]
        else:
            src, dest = piles[1], piles[0]

        print(item)
        if i % 10 == 0:
            print(100*i/len(inlist), "% complete")
        instr, num = item.split()[-2:]
        if num == 'stack':
            deal_all(src, dest)
        elif instr == 'increment':
            deal_increment_all(src, int(num), dest)
        elif instr == 'cut':
            cut_all(src, int(num), dest)
        else:
            print("wat:", item)
    if len(inlist) % 2 == 1:
        return src
    else:
        return dest


def do_day1_inverse(day1_end_state):
    # avoid allocating ram for each transform by just having two lists and switching src and dest each time.
    piles = [day1_end_state, list(range(10007))]
    for i, item in enumerate(reversed(inlist)):
        if i % 2 == 0:
            src, dest = piles[0], piles[1]
        else:
            src, dest = piles[1], piles[0]

        print(item)
        if i % 10 == 0:
            print(100*i/len(inlist), "% complete")
        instr, num = item.split()[-2:]
        if num == 'stack':
            inv_deal_all(src, dest)
        elif instr == 'increment':
            inv_deal_increment_all(src, int(num), dest)
        elif instr == 'cut':
            inv_cut_all(src, int(num), dest)
        else:
            print("wat:", item)
    if len(inlist) % 2 == 1:
        return src
    else:
        return dest


if __name__ == '__main__':
    day1_result = do_day1()
    inverted = do_day1_inverse(day1_result)  # should be a sorted list
    print(inverted)
    assert list_eq(inverted, list(range(len(inverted))))
