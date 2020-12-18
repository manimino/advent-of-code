input_str = """
cut -135
deal with increment 38
deal into new stack
deal with increment 29
cut 120
deal with increment 30
deal into new stack
cut -7198
deal into new stack
deal with increment 59
cut -8217
deal with increment 75
cut 4868
deal with increment 29
cut 4871
deal with increment 2
deal into new stack
deal with increment 54
cut 777
deal with increment 40
cut -8611
deal with increment 3
cut -5726
deal with increment 57
deal into new stack
deal with increment 41
deal into new stack
cut -5027
deal with increment 12
cut -5883
deal with increment 45
cut 9989
deal with increment 14
cut 6535
deal with increment 18
cut -5544
deal with increment 29
deal into new stack
deal with increment 64
deal into new stack
deal with increment 41
deal into new stack
deal with increment 6
cut 4752
deal with increment 8
deal into new stack
deal with increment 26
cut -6635
deal with increment 10
deal into new stack
cut -3830
deal with increment 48
deal into new stack
deal with increment 39
cut -4768
deal with increment 65
deal into new stack
cut -5417
deal with increment 15
cut -4647
deal into new stack
cut -3596
deal with increment 17
cut -3771
deal with increment 50
cut 1682
deal into new stack
deal with increment 20
deal into new stack
deal with increment 22
deal into new stack
deal with increment 3
cut 8780
deal with increment 52
cut 7478
deal with increment 9
cut -8313
deal into new stack
cut 742
deal with increment 19
cut 9982
deal into new stack
deal with increment 68
cut 9997
deal with increment 23
cut -240
deal with increment 54
cut -7643
deal into new stack
deal with increment 6
cut -3493
deal with increment 74
deal into new stack
deal with increment 75
deal into new stack
deal with increment 40
cut 596
deal with increment 6
cut -4957
deal into new stack"""

inlist = [f.strip() for f in input_str.split('\n') if f.strip()]


def cut(pile, n, dest):
    if n > 0:
        dest[0:-n] = pile[n:]
        dest[-n:] = pile[0:n]
    else:
        dest[0:n] = pile[n:]
        dest[n:] = pile[0:(len(pile)+n)]
        return


def list_eq(l1, l2):
    match = (len(l1) == len(l2)) and all(l1[i] == l2[i] for i in range(len(l1)))
    if not match:
        print("Mismatch:")
        print(l1)
        print(l2)
    return match


def deal_increment(src, n, dest):
    for i in range(len(src)):
        dest[(i*n) % len(src)] = src[i]


def deal(src, dest):
    n = len(src)
    for i in range(n):
        dest[n-i-1] = src[i]


def parse_input_and_do():
    # avoid allocating ram for each transform by just having two lists and switching src and dest each time.
    piles = [list(range(10007)), list(range(10007))]
    for i, item in enumerate(inlist):
        if i%2 == 0:
            src, dest = piles[0], piles[1]
        else:
            src, dest = piles[1], piles[0]

        print(item)
        if i%10 == 0:
            print(100*i/len(inlist), "% complete")
        instr, num = item.split()[-2:]
        if num == 'stack':
            deal(src, dest)
        elif instr == 'increment':
            deal_increment(src, int(num), dest)
        elif instr == 'cut':
            cut(src, int(num), dest)
        else:
            print("wat:", item)
    if len(inlist) % 2 == 1:
        print(src.index(2019))
    else:
        print(dest.index(2019))


### tests

def test_cut():
    src = list(range(4))
    dest = list(range(4))
    cut(src, 2, dest)
    assert list_eq(dest, [2, 3, 0, 1])
    cut(src, -2, dest)
    assert list_eq(dest, [2, 3, 0, 1])


def test_deal_increment():
    src = list(range(4))
    dest = list(range(4))
    deal_increment(src, 3, dest)
    assert list_eq(dest, [0, 3, 2, 1])


def do_tests():
    test_cut()
    test_deal_increment()
    print("tests passed")


if __name__ == '__main__':
    do_tests()
    parse_input_and_do()