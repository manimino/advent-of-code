

def read_input():
    # for puzzles where each input line is an object
    with open('input.txt') as fh:
        i=0
        for line in fh.readlines():
            if i==0:
                cups = [int(t) for t in list(line.strip())]
            if i==1:
                n_moves = int(line)
            i += 1
        return cups, n_moves


class CNode():
    # node in a circular linked list of cups
    # does the C stand for Circle? or Cup? It is a mystery for you to ponder.
    def __init__(self, num):
        self.num = num
        self.next = None


def move(label_nodes, label):
    node = label_nodes[label]

    # remove next 3 cups
    next_3_labels = [node.next.num, node.next.next.num, node.next.next.next.num]
    node.next = node.next.next.next.next

    # find target cup
    tgt_label = node.num - 1
    if tgt_label == 0:
        tgt_label = len(label_nodes)
    while True:
        if tgt_label in next_3_labels:
            tgt_label = tgt_label - 1 % len(label_nodes)
            if tgt_label == 0:
                tgt_label = len(label_nodes)
        else:
            break

    # move next_3 cups after target
    node_that_was_after_target = label_nodes[tgt_label].next
    label_nodes[tgt_label].next = label_nodes[next_3_labels[0]]
    label_nodes[next_3_labels[2]].next = node_that_was_after_target

    return node.next.num


def print_basic(label_nodes, start_pos):
    s = []
    label = start_pos
    while True:
        s.append(str(label_nodes[label].num))
        label = label_nodes[label].next.num
        if label == start_pos:
            break
    print(''.join(s))


def main():
    cups, n_moves = read_input()

    part2 = True
    if part2:
        cups = cups + list(range(10, 1000000+1))
        n_moves = 10000000

    label_nodes = dict()
    for c in range(len(cups)):
        label_nodes[cups[c]] = CNode(cups[c])
    for c in range(len(cups)):
        d = (c + 1) % len(cups)
        label_nodes[cups[c]].next = label_nodes[cups[d]]

    pos = cups[0]
    for m in range(n_moves):
        if m % 100000 == 0:
            print(round(m/n_moves*100, 2), '% done')
        pos = move(label_nodes, pos)

    if not part2:
        print_basic(label_nodes, cups[0])

    if part2:
        print('next 2 cups:',label_nodes[1].next.num, label_nodes[1].next.next.num)
        print('answer',label_nodes[1].next.num * label_nodes[1].next.next.num)

if __name__ == '__main__':
    main()
