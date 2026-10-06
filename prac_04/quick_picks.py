"""Program to generate random lottery tickets."""

from random import randint

NUMBER_OF_RANDOM_NUMBERS = 6
LOWEST_NUMBER = 1
HIGHEST_NUMBER = 45


def main():
    """Generate a user-specified number of quick pick lines."""
    number_of_quick_picks = int(input("How many quick picks? "))
    for i in range(number_of_quick_picks):
        quick_pick = create_quick_pick(LOWEST_NUMBER, HIGHEST_NUMBER, NUMBER_OF_RANDOM_NUMBERS)
        # for number in quick_pick:
        #     print(f"{number:2}", end=" ")
        # print()
        print(" ".join(f"{number:2}" for number in quick_pick))


def create_quick_pick(low, high, numbers_per_line):
    """Create a line containing numbers_per_line numbers, sorted in ascending order."""
    quick_pick = []
    for i in range(numbers_per_line):
        number = randint(low, high)
        while number in quick_pick:
            number = randint(low, high)
        quick_pick.append(number)
    quick_pick.sort()
    return quick_pick


main()
