
BYRS = []
IYRS = []
EYRS = []
HGTS = []
ECLS = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def generate_valids():
    for i in range(1920, 2002+1):
        BYRS.append(str(i))
    for i in range(2010, 2020+1):
        IYRS.append(str(i))
    for i in range(2020, 2030+1):
        EYRS.append(str(i))

    # HGT can be cm or in
    for i in range(150, 193+1):
        HGTS.append('{}cm'.format(i))
    for i in range(59,76+1):
        HGTS.append('{}in'.format(i))


def read_passports():
    with open('input.txt') as fh:
        lines = fh.readlines()

    pp_chunks = []
    chunk = ""
    for li in range(len(lines)):
        if lines[li].strip():
            chunk += lines[li].strip() + " "
        else:
            pp_chunks.append(chunk)
            chunk = ""
            # I added 2 newlines at the end of the input so this will catch the last one. HAX.

    print(len(pp_chunks), pp_chunks)

    # each chunk is a one-line string containing all fields
    passports = []
    for chunk in pp_chunks:
        p = dict()
        try:
            for tok in chunk.strip().split(' '):
                if not tok.strip():
                    # could have multiple spaces, no biggie
                    continue
                k, v = tok.split(':')  # might error if bad token
                p[k] = v
        except Exception:
            # invalid - skip.
            print("skipping chunk:", chunk)
            continue
        passports.append(p)
    print(len(passports,), passports)
    return passports


def check_required_fields_present(p):
    # cid not actually required
    min_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    for field in min_fields:
        if field not in p:
            print("p missing", field, len(p), ":", p)
            return False
    return True


def valid_pid(pid):
    try:
        for i in range(9):
            int(pid[i])
        assert len(pid) == 9
    except Exception:
        return False
    return True


def valid_hcl(hcl):
    valid_chars = [str(i) for i in range(10)] + ['a', 'b', 'c', 'd', 'e', 'f']
    try:
        assert len(hcl) == 7
        assert hcl[0] == '#'
        for i in range(1,7):
            assert hcl[i] in valid_chars
    except Exception:
        return False
    return True


def check_required_fields_valid(p):
    if not p['byr'] in BYRS:
        return False
    if not p['iyr'] in IYRS:
        return False
    if not p['eyr'] in EYRS:
        return False
    if not p['hgt'] in HGTS:
        return False
    if not p['ecl'] in ECLS:
        return False
    if not valid_pid(p['pid']):
        return False
    if not valid_hcl(p['hcl']):
        return False
    return True


def main():
    pps = read_passports()
    valid_pps = []
    for p in pps:
        if not check_required_fields_present(p):
            continue
        if not check_required_fields_valid(p):
            continue
        valid_pps.append(p)
    print(len(valid_pps))


if __name__ == '__main__':
    # 226 - max
    generate_valids()
    main()