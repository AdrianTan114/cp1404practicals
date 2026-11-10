"""
Project Management Program
Estimate: 30 minutes
Actual:   _ minutes
"""

from project import Project

DEFAULT_FILENAME = "projects.txt"


def main():
    projects = load_projects(DEFAULT_FILENAME)
    for project in projects:
        print(project)


def load_projects(filename):
    projects = []
    with open(filename, "r") as in_file:
        in_file.readline()  # Skip header row
        for line in in_file:
            line = line.strip().split("\t")
            project = Project(line[0], line[1], int(line[2]), float(line[3]), int(line[4]))
            projects.append(project)
    return projects


main()
