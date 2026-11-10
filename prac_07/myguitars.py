"""Prac 7 - More Guitars! Exercise"""

from guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Display guitars from a file."""
    guitars = load_guitars(FILENAME)
    for guitar in guitars:
        print(guitar)
    print("Add new guitars")
    get_guitar(guitars)
    guitars.sort()
    save_guitars(guitars, FILENAME)


def load_guitars(filename):
    """Load guitars from filename."""
    guitars = []
    with open(filename, "r") as in_file:
        for line in in_file:
            line = line.strip().split(",")
            guitar = Guitar(line[0], int(line[1]), float(line[2]))
            guitars.append(guitar)
    return guitars


def get_guitar(guitars):
    """Get information on new guitars from the user."""
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print()
        name = input("Name: ")


def save_guitars(guitars, filename):
    """Save guitars to filename."""
    with open(filename, "w") as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)


main()
