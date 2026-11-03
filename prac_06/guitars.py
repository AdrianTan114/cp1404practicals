"""Playing the Guitars"""

from guitar import Guitar


def main():
    print("My guitars!")
    guitars = add_guitars()
    display_guitars(guitars)


def add_guitars():
    guitars = []
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print()
        name = input("Name: ")
    # guitars.append(Guitar("Fender Stratocaster", 2014, 765.40))
    # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    return guitars


def display_guitars(guitars):
    print("These are my guitars:")
    for i, guitar in enumerate(guitars):
        vintage_string = "(vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i + 1}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_string}")


main()
