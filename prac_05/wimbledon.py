"""
Word Occurrences
Estimate: 25 minutes
Actual:   _ minutes
"""

FILENAME = "wimbledon.csv"


def main():
    records = load_file(FILENAME)
    print(records)


def load_file(filename):
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # Skip the header row
        records = []
        for line in in_file:
            records.append(line.strip().split(","))
    return records


main()
