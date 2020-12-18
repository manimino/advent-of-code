from day22.util import list_eq


def cut_one(src_pos, c, stack_size):
    """
    :param src_pos: a position in the source stack
    :param c: cut point (can be negative)
    :param stack_size: total
    :return: a position in the destination stack
    """
    """
    # fix negative
    if c < 0:
        c = stack_size + c

    # let "s" represent the card at src_pos
    if c > src_pos:
        # cut point is below s
        # |s|c| -> ||s||
        # c = 4
        # s + (stack_size-c) = s+(5-4) = s is now at position 2
        # s moves deeper into the deck by (stack_size-c) cards
        return src_pos + (stack_size - c)
    else:
        # cut point is above s
        # |c|s| -> |s|||
        # s rises c positions higher in the deck
        return src_pos - c
    """
    return (src_pos - c) % stack_size


def inv_cut_one(src_pos=None, c=None, stack_size=None):
    # if you just did a "cut 4", you could "cut -4" to get your original stack back.
    return cut_one(src_pos, -c, stack_size)


def inv_cut_all(src, c, dest):
    for si in range(len(src)):
        di = inv_cut_one(si, c, len(src))
        dest[di] = src[si]


def cut_all(src, c, dest):
    """
    :param src: stack
    :param c: cut point
    :param dest: preallocated empty stack of length src, to be filled by this function
    """
    for si in range(len(src)):
        di = cut_one(si, c, len(src))
        dest[di] = src[si]


def cut_all_day1(pile, n, dest):
    if n > 0:
        dest[0:-n] = pile[n:]
        dest[-n:] = pile[0:n]
    else:
        dest[0:n] = pile[n:]
        dest[n:] = pile[0:(len(pile)+n)]
        return


def test_cut():
    src = list(range(4))
    dest = list(range(4))
    cut_all(src, 2, dest)
    assert list_eq(dest, [2, 3, 0, 1])
    cut_all(src, -2, dest)
    assert list_eq(dest, [2, 3, 0, 1])
    cut_all(src, 0, dest)
    assert list_eq(dest, [0, 1, 2, 3])


def test_cut_vs_other():
    src = list(range(5))
    dest = list(range(5))
    dest2 = list(range(5))
    for c in [-4, 0, 4, 5, -5]:
        print(c)
        cut_all(src, c, dest)
        cut_all_day1(src, c, dest2)
        assert list_eq(dest, dest2)


if __name__ == "__main__":
    test_cut()
    test_cut_vs_other()