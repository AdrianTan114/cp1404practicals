"""Menu-based program that will get a score, determine a result, and display stars based on the score."""

MENU = """(G)et Valid Score
(P)rint result
(S)how stars
(Q)uit"""


def main():
    score = get_valid_number(0, 100, "Score: ")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_number(0, 100, "Score: ")
        elif choice == "P":
            pass
        elif choice == "S":
            pass
        else:
            print("Invalid input")
        print(MENU)
        choice = input(">>> ").upper()
    print("Farewell")


def get_valid_number(low, high, prompt):
    """Get a number from the user, ensuring it is within the boundaries low and high"""
    number = float(input(prompt))
    while number < low or number > high:
        print("Invalid number")
        number = float(input(prompt))
    return number

main()
