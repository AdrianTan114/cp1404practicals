"""
Emails
Estimate: 25 minutes
Actual:   30 minutes
"""


def main():
    """Ask the user for emails, pair each of them with a name in a dictionary, and print them all at the end."""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = extract_name(email)
        name_confirmation = input(f"Is your name {name}? (Y/n) ")
        # Ask for name if the user does not enter y or enter
        if name_confirmation != "" and name_confirmation.lower() != "y":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")
    print()  # Print a blank line
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name(email):
    """Extract a name based on the email local-part."""
    name = email[:email.find("@")]  # Remove domain from email address
    if "." in name:
        name = " ".join(name.split("."))
    return name.title()


main()
