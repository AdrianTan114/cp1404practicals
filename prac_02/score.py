"""
CP1404/CP5632 - Practical
Program to determine score status
"""

import random


def main():
    user_score = float(input("Enter score: "))
    user_result = determine_result(user_score)
    print(f"User score {user_score} is {user_result}")
    random_score = random.randint(0, 100)
    random_result = determine_result(random_score)
    print(f"Random: {random_score} = {random_result}")


def determine_result(score):
    if score < 0 or score > 100:
        return "Invalid"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
