"""
Project Management Program
Estimate: 45 minutes
Actual:   _ minutes
"""

from project import Project
from datetime import datetime

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
            filter_date = datetime.strptime(input("Show projects that start after date (dd/mm/yy): "), "%d/%m/%Y")
            filter_projects_by_date(projects, filter_date)
        elif choice == "A":
            add_project(projects)
        elif choice == "U":
            update_project(projects)
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
            date = convert_string_to_datetime(line[1]).date().strftime("%d/%m/%Y")
            project = Project(line[0], date, int(line[2]), float(line[3]), int(line[4]))
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


def filter_projects_by_date(projects, filter_date):
    for project in projects:
        if convert_string_to_datetime(project.date) > filter_date:
            print(project)


def convert_string_to_datetime(string):
    return datetime.strptime(string, "%d/%m/%Y")


def add_project(projects):
    print("Let's add a new project")
    name = input("Name: ")
    date = convert_string_to_datetime(input("Start date (dd/mm/yy): ")).date().strftime("%d/%m/%Y")
    priority = int(input("Priority: "))
    cost = float(input("Cost estimate: $"))
    completion_percentage = int(input("Percent complete: "))
    project = Project(name, date, priority, cost, completion_percentage)
    projects.append(project)


def update_project(projects):
    for i, project in enumerate(projects):
        print(i, project)
    project_choice = int(input("Project choice: "))
    print(projects[project_choice])
    percentage = input("New percentage: ")
    if percentage != "":
        projects[project_choice].completion_percentage = int(percentage)
    priority = input("New priority: ")
    if priority != "":
        projects[project_choice].priority = int(priority)


main()
