from day22.util import list_eq, modInverse


def deal_increment_day1(src, n, dest):
    for i in range(len(src)):
        dest[(i*n) % len(src)] = src[i]


def deal_increment_one(si, n, deck_size):
    return (si*n) % deck_size


def deal_increment_all(src, n, dest):
    for si in range(len(src)):
        di = deal_increment_one(si, n, len(src))
        dest[di] = src[si]


def inv_deal_increment_one(si=None, n=None, deck_size=None):
    """
    In general, we can't invert modulo because it's ambiguous.
    5 % 3 is the same as 8 % 3, so inv(2, 3) could give 2, 5, 8...
    Here, though, we have the guarantee of uniqueness because as the problem says:
    "Of course, this technique is carefully designed so it will never put two cards in
    the same position or leave a position empty."
    Meaning that the deck size and divisor are relatively prime. This makes it invertible.
    """
    """
    # correct, but really expensive:
    for i in range(deck_size):
        if (i*n) % deck_size == si:
            return i
    """
    # thanks to https://www.youtube.com/watch?v=4-HSjLXrfPs for (re)teaching me linear congruence solving
    invmod = modInverse(n, deck_size)  # lru_cached
    return (invmod * si) % deck_size


def inv_deal_increment_all(src, n, dest):
    for si in range(len(src)):
        dest[inv_deal_increment_one(si, n, len(src))] = src[si]


def test_inv_deal_increment_one():
    assert inv_deal_increment_one(0, 1, 1) == 0

    # stack size 5, modulo 3.
    # Forwards,
    # [0,1,2,3,4] becomes
    # [0,.,.,.,.]
    # [0,.,.,1,.]
    # [0,2,.,1,.]
    # [0,2,.,1,3]
    # [0,2,4,1,3]
    assert inv_deal_increment_one(0, 3, 5) == 0  # card at pos 0 stays at 0
    assert inv_deal_increment_one(3, 3, 5) == 1  # card at pos 3 moves back to pos 1
    assert inv_deal_increment_one(1, 3, 5) == 2  # card at pos 1 moves back to pos 2
    assert inv_deal_increment_one(4, 3, 5) == 3  # card at pos 4 moves back to pos 3
    assert inv_deal_increment_one(2, 3, 5) == 4  # card at pos 2 moves back to pos 4


def test_inv_deal_increment_all():
    sz = 7
    div = 3
    src = [i for i in range(sz)]
    dest1 = list(range(sz))
    dest2 = list(range(sz))
    deal_increment_all(src, div, dest1)
    inv_deal_increment_all(dest1, div, dest2)
    print(dest1)
    assert list_eq(dest2, src)


def test_deal_increment():
    src = list(range(4))
    dest = list(range(4))
    deal_increment_all(src, 3, dest)
    assert list_eq(dest, [0, 3, 2, 1])


def test_deal_incr_all_vs_day1():
    src = list(range(11))
    dest1 = list(range(11))
    dest2 = list(range(11))
    for n in [1, 3, 5, 7]:
        deal_increment_all(src, n, dest1)
        deal_increment_day1(src, n, dest2)
        assert list_eq(dest1, dest2)


if __name__ == '__main__':
    test_deal_increment()
    test_deal_incr_all_vs_day1()
    test_inv_deal_increment_one()
    test_inv_deal_increment_all()
