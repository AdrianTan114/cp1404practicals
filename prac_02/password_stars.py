"""Display asterisks based on the length of a user-given password"""


def main():
    minimum_length = 8
    password = get_password(minimum_length)
    print_stars(password)


def get_password(minimum_length):
    password = input("Password: ")
    while len(password) < minimum_length:
        print("Password is too short")
        password = input("Password: ")
    return password


def print_stars(password):
    print("*" * len(password))


main()
