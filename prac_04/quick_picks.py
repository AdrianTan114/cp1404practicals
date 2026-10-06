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
        for number in quick_pick:
            print(f"{number:2}", end=" ")
        print()


def create_quick_pick(low, high, number_of_numbers):
    """Create a line containing number_of_numbers numbers, sorted in ascending order."""
    numbers = []
    for i in range(number_of_numbers):
        number = randint(low, high)
        while number in numbers:
            number = randint(low, high)
        numbers.append(number)
    numbers.sort()
    return numbers


main()
