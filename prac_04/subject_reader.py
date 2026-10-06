"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Program to load and display subject data from file."""
    subject_records = load_subject_data(FILENAME)
    # print(subject_records)
    print_subject_details(subject_records)


def load_subject_data(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    data = []
    input_file = open(filename)
    for line in input_file:
        # print(line)  # See what a line looks like
        # print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        # print(parts)  # See what the parts look like (notice the integer is a string)
        # Make the number an integer as part of a new, poorly named, list
        record = [parts[0], parts[1], int(parts[2])]
        # print(record)  # See if that worked
        # print("----------")
        data.append(record)
    input_file.close()
    return data


def print_subject_details(data):
    for record in data:
        subject_code, teacher, number_of_students = record
        print(f"{subject_code} is taught by {teacher:12} and has {number_of_students:3} students")


main()
