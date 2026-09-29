"""Experiment with the random module."""

# What did you see on line 1? 20, 18, 8, 7, 7, 12
# What was the smallest number you could have seen, what was the largest? Smallest: 5, Largest: 20

# What did you see on line 2? 5, 3, 5, 3, 9
# What was the smallest number you could have seen, what was the largest? Smallest: 3, Largest: 9
# Could line 2 have produced a 4? No, it can only produce a 3, 5, 7, or 9

# What did you see on line 3? 4.620368349084233, 5.086972856033505, (floats with a lot of decimals)
# What was the smallest number you could have seen, what was the largest? Smallest: 2.5, Largest: 5.5

# Write code, not a comment, to produce a random number between 1 and 100 inclusive.
import random
print(random.randint(1, 100))