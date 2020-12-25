
def transform_subj_number(sn, loop_size):
    v = 1
    for i in range(loop_size):
        v = (v*sn) % 20201227
    return v


def get_loop_size(pubkey):
    i = 0
    sn = 7
    v = 1
    while True:
        v = (v * sn) % 20201227
        i += 1
        if v == pubkey:
            return i


def main():
    card_pubkey = 9093927
    door_pubkey = 11001876

    #card_pubkey = 5764801
    #door_pubkey = 17807724

    card_loop_size = get_loop_size(card_pubkey)
    door_loop_size = get_loop_size(door_pubkey)

    print(card_loop_size, door_loop_size)

    key = transform_subj_number(door_pubkey, card_loop_size)
    other_key = transform_subj_number(card_pubkey, door_loop_size)
    print(key, other_key)

if __name__ == '__main__':
    main()