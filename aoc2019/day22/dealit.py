
def deal_day1(src, dest):
    n = len(src)
    for i in range(n):
        dest[n-i-1] = src[i]


def deal_one(src_pos, stack_size):
    return stack_size-src_pos-1


def inv_deal_one(src_pos=None, deck_size=None):
    # well, that's easy to invert...
    return deck_size-src_pos-1


def inv_deal_all(src, dest):
    deal_all(src, dest)  # EZ


def deal_all(src, dest):
    stack_size = len(src)
    for src_pos in range(len(src)):
        dest[deal_one(src_pos, stack_size)] = src[src_pos]
