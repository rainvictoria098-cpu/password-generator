import secrets
import string

print("Welcome to Rain's Password Generator!")

# Ask how long the password should be
length = int(input("How many characters should the password have? "))

# Check the length
if length < 8:
    print("Please choose at least 8 characters.")

else:
    # These are the characters the program can use
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation

    all_characters = letters + numbers + symbols

    # Start with an empty password
    password = ""

    # Add one random character at a time
    for count in range(length):
        password = password + secrets.choice(all_characters)

    # Show the new password
    print("\nYour new password is:")
    print(password)

    print("\nKeep your password private.")