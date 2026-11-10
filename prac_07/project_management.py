"""
Project Management Program
Estimate: 45 minutes
Actual:   _ minutes
"""

from project import Project

DEFAULT_FILENAME = "projects.txt"


def main():
    print("Welcome to Pythonic Project Management")
    projects = load_projects(DEFAULT_FILENAME)
    display_menu()
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            filename = input("Filename: ")
            projects = load_projects(filename)
        elif choice == "S":
            pass
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            pass
        elif choice == "A":
            pass
        elif choice == "U":
            pass
        else:
            print("Invalid input")
        display_menu()
        choice = input(">>> ").upper()


def load_projects(filename):
    projects = []
    with open(filename, "r") as in_file:
        in_file.readline()  # Skip header row
        for line in in_file:
            line = line.strip().split("\t")
            project = Project(line[0], line[1], int(line[2]), float(line[3]), int(line[4]))
            projects.append(project)
    print(f"Loaded {len(projects)} projects from {filename}")
    return projects


def display_menu():
    print("- (L)oad projects")
    print("- (S)ave projects")
    print("- (D)isplay projects")
    print("- (F)ilter projects by date")
    print("- (A)dd new project")
    print("- (U)pdate project")
    print("- (Q)uit")


def display_projects(projects):
    incomplete_projects = [project for project in projects if project.completion_percentage < 100]
    incomplete_projects.sort()
    completed_projects = [project for project in projects if project.completion_percentage == 100]
    completed_projects.sort()
    print("Incomplete projects:")
    for project in incomplete_projects:
        print(project)
    print("Completed projects:")
    for project in completed_projects:
        print(project)


main()
