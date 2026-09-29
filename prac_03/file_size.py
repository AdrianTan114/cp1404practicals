"""Program to print the number of lines in a file."""


def main():
    """Count the number of lines in user-specified files, with exception catching, until empty string is entered."""
    filename = input("Enter filename: ")
    while filename != "":
        try:
            number_of_lines = count_lines(filename)
            print(f"{filename} has {number_of_lines} lines.")
        except FileNotFoundError:
            print(f"ERROR: {filename} does not exist.")
        filename = input("Enter filename: ")
    print("Finished.")


def count_lines(filename):
    """Count the number of lines in the file filename."""
    in_file = open(filename, "r")
    number_of_lines = 0
    for line in in_file:
        number_of_lines += 1
    in_file.close()
    return number_of_lines


main()
