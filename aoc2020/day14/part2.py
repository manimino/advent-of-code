import re


def read_input():
    # for puzzles where each input line is an object
    with open('input.txt') as fh:
        for line in fh.readlines():
            yield line.strip()


def replace_Xs_and_write(mem,pos_str,val):
    # no Xs in pos_str pls
    i = pos_str.find('X')
    if i==-1:
        mem[to_base10(pos_str)] = val
    else:
        replace_Xs_and_write(mem, pos_str[0:i]+'0'+pos_str[i+1:], val)
        replace_Xs_and_write(mem, pos_str[0:i]+'1'+pos_str[i+1:], val)


def write_to_mem(mem, pos, mask, val):
    pos_str = to_36b(pos)
    new_pos_str=list()
    # determine pos as string with Xs
    for i in range(len(pos_str)):
        if mask[i]=='X':
            new_pos_str.append('X')
        elif mask[i]=='1':
            new_pos_str.append('1')
        elif mask[i]=='0':
            new_pos_str.append(pos_str[i])

    # actually do writing
    replace_Xs_and_write(mem, ''.join(new_pos_str), val)


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
            write_to_mem(mem, pos, mask, val)
        elif obj.startswith("mask"):
            mask = obj.split('=')[-1].strip()

    result = 0
    for k, v in mem.items():
        result += v
    print(result)


if __name__ == '__main__':
    main()