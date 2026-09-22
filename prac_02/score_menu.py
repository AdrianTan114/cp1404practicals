"""Menu-based program that will get a score, determine a result, and display stars based on the score."""

MENU = """(G)et Valid Score
(P)rint result
(S)how stars
(Q)uit"""


def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            pass
        elif choice == "P":
            pass
        elif choice == "S":
            pass
        else:
            print("Invalid input")
        print(MENU)
        choice = input(">>> ").upper()
    print("Farewell")


main()
