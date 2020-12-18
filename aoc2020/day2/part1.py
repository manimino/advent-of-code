def read_each():
    with open('input.txt') as fh:
        for line in fh.readlines():
            policy, pwd = line.split(':')
            yield policy.strip(), pwd.strip()


def validate(policy, pwd):
    rng, req_char = policy.split()
    lmin, lmax = rng.split('-')
    req_count = 0
    for c in pwd:
        if c == req_char:
            req_count += 1
    if req_count >= int(lmin) and req_count <= int(lmax):
        return True
    return False


def main():
    valid = 0
    for policy, pwd in read_each():
        if validate(policy, pwd):
            valid += 1
    print(valid)


if __name__ == '__main__':
    main()