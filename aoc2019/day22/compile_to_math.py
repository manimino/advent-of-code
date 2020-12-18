"""
cut: b += -c
dealinc: a = ai
deal: a = -a; b = -b
"""


def apply_cut(a, b, c):
    return a, b-c


def apply_deal(a, b):
    return -a, -1-b


def apply_dealinc(a, b, i):
    return a*i, b*i


def main():
    a = 1
    b = 0



if __name__ == '__main__':
    main()