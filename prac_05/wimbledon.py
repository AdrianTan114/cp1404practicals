"""
Wimbledon
Estimate: 25 minutes
Actual:   35 minutes
"""

FILENAME = "wimbledon.csv"
CHAMPION_INDEX = 2
COUNTRY_INDEX = 1


def main():
    """Display champions of Wimbledon and their win counts and the champion's countries, from data from a file."""
    records = load_file(FILENAME)
    champion_to_count, countries = process_records(records)
    display_results(champion_to_count, countries)


def load_file(filename):
    """Load contents of a file into a list."""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # Skip the header row
        records = []
        for line in in_file:
            records.append(line.strip().split(","))
    return records


def process_records(records):
    """Extract champions, their win counts, and country from the record."""
    champion_to_count = {}
    countries = set()
    for record in records:
        if record[CHAMPION_INDEX] in champion_to_count:
            champion_to_count[record[CHAMPION_INDEX]] += 1
        else:
            champion_to_count[record[CHAMPION_INDEX]] = 1
        countries.add(record[COUNTRY_INDEX])
    return champion_to_count, countries


def display_results(champion_to_count, countries):
    """Display formatted results in the console."""
    print("Wimbledon Champions:")
    for champion in champion_to_count:
        print(champion, champion_to_count[champion])
    print()
    print(f"These {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))


main()
