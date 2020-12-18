def read_input():
    # for puzzles where each input line is an object
    with open('input.txt') as fh:
        for line in fh.readlines():
            toks = []
            for tok in line.strip().split(" "):
                if len(tok) == 1:
                    toks.append(tok)
                else:
                    # make each '(' or ')' its own token
                    toks.extend(list(tok))
            yield toks


def evaluate(tok_list):
    """
    computes result of a parentheses-free expression
    example input: ['1','+','3','*','4']
    output: '16'
    """
    num_or_op='num'
    result = None
    cur_op = None
    for tok in tok_list:
        # toggle between expecting a num or an op
        if num_or_op=='num':
            num_or_op = 'op'
            if result is None:
                result = int(tok)
            elif cur_op == '+':
                result += int(tok)
            elif cur_op == '*':
                result *= int(tok)
        else:
            num_or_op='num'
            cur_op = tok

    print("got", result, "from tok_list:", tok_list)
    return str(result)


def handle_parens(toks):
    """
    :param toks: a list of tokens, e.g. ['1', '+', '((2', '*', '3)', '*', '5)]
    :return: answer
    """
    expr = []
    i=0
    while i < len(toks):
        tok = toks[i]
        if tok == ')':
            return evaluate(expr), i
        elif tok == '(':
            result, skip_i = handle_parens(toks[i+1:])
            expr.append(result)
            i+=skip_i+1  # skip forward to where that one finished
        else:
            expr.append(tok)
        i+=1
    print("final expr", expr)
    return evaluate(expr)


def main():
    total=0
    for line_toks in read_input():
        print(line_toks)
        result = handle_parens(line_toks)
        print("got:", result, "from:", line_toks)
        total += int(result)
    print(total)


if __name__ == '__main__':
    main()