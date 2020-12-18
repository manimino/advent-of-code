import re
def read_input():
    # for puzzles where each input line is an object
    with open('input.txt') as fh:
        for line in fh.readlines():
            yield line.strip()


def apply_mask(mask, val):
    val_str = to_36b(val)
    result=list()
    for i in range(len(val_str)):
        if mask[i]=='X':
            result.append(val_str[i])
        elif mask[i]=='1':
            result.append('1')
        elif mask[i]=='0':
            result.append('0')
    return to_base10(''.join(result))


def to_36b(val):
    # convert int to 36-bit binary number string
    return str(bin(val)[2:]).zfill(36)


def to_base10(val_str):
    return int(val_str, 2)


def main():
    mem = dict()
    mask=""
    for obj in read_input():
        if obj.startswith("mem"):
            r = re.match(r"mem\[(\d+)\] = (\d+)", obj)
            pos = int(r.groups()[0])
            val = int(r.groups()[1])
            mem[pos] = apply_mask(mask, val)
        elif obj.startswith("mask"):
            mask = obj.split('=')[-1].strip()

    result = 0
    for k, v in mem.items():
        result += v
    print(result)


if __name__ == '__main__':
    main()