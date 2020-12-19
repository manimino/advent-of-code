import re


def read_input():
    # for puzzles where each input line is an object
    def _parse_nums(rule_text):
        return tuple(int(i) for i in rule_text.strip().split())

    with open('part2_input.txt') as fh:
        rules = {}
        texts = []
        for line in fh.readlines():
            if ':' in line.strip():
                rule_num, rule_body = line.strip().split(': ')
                rule_num = int(rule_num)
                if '\"' in rule_body:
                    rules[rule_num] = rule_body.replace("\"", "")
                else:
                    if "|" in rule_body:
                        options = rule_body.split("|")
                        rules[rule_num] = [_parse_nums(r) for r in options]
                    else:
                        rules[rule_num] = _parse_nums(rule_body)
            elif line.strip():
                # it's a message
                texts.append(line.strip())
        return rules, texts


def do_subs(rules, thing):
    if type(thing) == str:
        return thing
    elif type(thing) == int:
        return do_subs(rules, rules[thing])
    elif type(thing) == list:
        return [do_subs(rules, x) for x in thing]
    elif type(thing) == tuple:
        return tuple(do_subs(rules, x) for x in thing)


def make_regex(compiled_rules):
    if type(compiled_rules) is list:
        return '(' + '|'.join([make_regex(x) for x in compiled_rules]) + ')'
    elif type(compiled_rules) is tuple:
        return ''.join([make_regex(x) for x in compiled_rules])
    elif type(compiled_rules) is str:
        return compiled_rules


def main():
    rules, texts = read_input()
    print('rules:', rules)
    compiled_rules = do_subs(rules, 0)
    print('compiled rules:', compiled_rules)
    regex = make_regex(compiled_rules)
    regex = '^{}$'.format(regex)  # exact match
    print("regex:", regex)
    print(texts)
    print("matches:")
    ms = []
    for text in texts:
        if re.match(regex, text) is not None:
            ms.append(text)
    print("answer:", len(ms))


def fix_input_11():
    s = []
    for i in range(2, 15):
        s.append('|')
        s.extend(['42'] * i)
        s.extend(['31'] * i)
        print(s)
    print(' '.join(s))


def fix_input_8():
    s = []
    for i in range(2, 15):
        s.append('|')
        s.extend(['42'] * i)
        print(s)
    print(' '.join(s))


if __name__ == '__main__':
    main()