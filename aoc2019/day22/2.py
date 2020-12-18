import time
from functools import partial

"""
OK, this clearly needs a different plan.
The deck is too big for RAM, and the number of functions to apply is too big for time.

Here's a plan:
1. Only deal with one card in the deck (position 2020 at end of transform) and work backwards
through the transforms.
 -- So we need to make functions that only deal with one card at a time, and the 
inverses of those functions.
 -- Also, reverse the instruction list.
 -- Prove this all works by running day 1's problem backwards, generating the input from the output.
 
2. Reduce the instruction list to one step that moves a card given its initial pos and the deck size.
3. Look for a pattern (e.g. applying the full instruction set moves the card N places down the stack...) and compute
what happens if that were applied the required number of times.

1 is hard. 2 and 3 are things I hope work but have no idea if they will.
Here goes!

Update:
Finished (1). Brute-force application of the process will take ~1900 years without further optimization.
There are no position repeats during the first ~100K runs through the instruction set.
There are no apparent patterns in the position change (e.g. it doesn't move forward by 2 every time or anything nice.)

OK, easy optimization - remove the string processing step by pre-converting instruction list.
That gets us down to 190 years. Yay?

You could really express the whole instruction list as a big pile-o-math. 
f(f(f(f(f(pos))))) = math * math + math(pos) or suchlike.

Ultimately we are applying about 10^15 instructions here. That's ~1 million seconds at 1 GHz, or 11 days minimum.
If we have to compute the whole thing that's still too much.
There must be a way to simplify the math.

Gonna try and cram the whole instruction list into one (a*p + b) % d = 2020 expression and solve for p.
Each shuffle changes a, b, or both.
Initially a is 1, b is 0, and p is the card number (unknown).

Those ops will be applied n times, so it'll be an [a^(n)*p + b*n] % d = 2020. 
We'll move the b*n out by just applying mod d, to get: 
(a^n * p) %d = 2020 - (b*n) %d.
"""

from day22.inputs import inlist
from day22.cutit import inv_cut_one
from day22.dealit import inv_deal_one
from day22.dealincr import inv_deal_increment_one


def instructions_to_funclist(deck_size):
    """
    get rid of string comparison step in reading instruction list
    """
    flist = []
    for i, item in enumerate(inlist):
        instr, num = item.split()[-2:]
        if num == 'stack':
            flist.append(partial(inv_deal_one, **{'deck_size': deck_size}))
        elif instr == 'increment':
            flist.append(partial(inv_deal_increment_one, **{'n':int(num), 'deck_size': deck_size}))
        elif instr == 'cut':
            flist.append(partial(inv_cut_one, **{'c':int(num), 'stack_size': deck_size}))
        else:
            print("wat:", item)
    return flist


def apply_invert_instructions(pos, flist):
    for f in reversed(flist):
        pos = f(pos)
    return pos


def run_invert():
    pos = 2020
    n_iter = 101741582076661
    deck_size = 119315717514047
    t0 = time.time()
    flist = instructions_to_funclist(deck_size)
    for i in range(n_iter):
        pos = apply_invert_instructions(pos, flist)
        if pos == 2020:
            print(">>>>>>>>>>  FOUND IT", i)
        if i % pow(10, 7) == 0:
            print(i / n_iter, " done after", round((time.time()-t0)/60, 2), "min")
    return pos


if __name__ == '__main__':
    pos = run_invert()
    print(pos)