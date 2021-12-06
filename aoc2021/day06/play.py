"""
simpler system.
just have fish reproduce every 7 days
they all start at a 0-counter
they spawn fish with a 6 on them so everything's in sync
"""

# initially we have one fish
# fish = [0]
# after day 0 we have 2 fish:
# fish = 6, 6
# after day 7 we have 4 fish, etc.
# after day 14 we have 8 fish, etc.
# So it's 2^(days//7) fish.

# Simplistic model:
"""
for days in range(22):
    print(days, pow(2, days // 7 + 1))
"""

# Now let's add fish clocks.



