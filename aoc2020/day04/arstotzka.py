

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


def main():
    pps = read_passports()
    valid_pps = []
    for p in pps:
        if not check_required_fields_present(p):
            continue
        valid_pps.append(p)
    print(len(valid_pps))


if __name__ == '__main__':
    # 225 - too low
    # 235 - too high, so the idea's roughly right.
    main()