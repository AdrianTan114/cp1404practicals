"""Prac 7 - More Guitars! Exercise"""

from guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Display guitars from a file."""
    guitars = load_guitars(FILENAME)
    guitars.sort()
    for guitar in guitars:
        print(guitar)


def load_guitars(filename):
    """Load guitars from filename."""
    guitars = []
    with open(filename, "r") as in_file:
        for line in in_file:
            line = line.strip().split(",")
            guitar = Guitar(line[0], int(line[1]), float(line[2]))
            guitars.append(guitar)
    return guitars


main()
