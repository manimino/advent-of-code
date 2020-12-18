def read_each():
    with open('input.txt') as fh:
        for line in fh.readlines():
            policy, pwd = line.split(':')
            yield policy.strip(), pwd.strip()


def validate(policy, pwd):
    rng, req_char = policy.split()
    pos1, pos2 = rng.split('-')
    pos1 = int(pos1)-1
    pos2 = int(pos2)-1
    matches = 0
    if pos1 <= len(pwd) and pwd[pos1] == req_char:
        matches += 1
    if pos2 <= len(pwd) and pwd[pos2] == req_char:
        matches += 1
    if matches == 1:
        return True
    return False


def main():
    valid = 0
    for policy, pwd in read_each():
        if validate(policy, pwd):
            valid += 1
    print(valid)


if __name__ == '__main__':
    # 850 too high
    main()