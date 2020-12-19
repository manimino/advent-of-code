import re


def read_input():
    # for puzzles where each input line is an object
    def _parse_nums(rule_text):
        return tuple(int(i) for i in rule_text.strip().split())

    with open('input.txt') as fh:
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
                        # there's a max of 1 "|" per rule in the input
                        first_rule, second_rule = rule_body.split("|")
                        rules[rule_num] = [_parse_nums(first_rule), _parse_nums(second_rule)]
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

"""
^a
  (
    (
      (aa|bb)|(ab|ba)
    )|
    (
      (ab|ba)|(aa|bb)
    )
  )
b$
"""


if __name__ == '__main__':
    main()