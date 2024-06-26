import string
import random

# Function that generate a password
def generate_password():
    # Define the characters that must be used in the password
    characters_for_password = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    # Generate a password using random
    password = ''.join(random.choice(characters_for_password) for _ in range(8))
    return password

def main():
    # Loop that generate 5 passwords and print them
    for _ in range(5):
        # Generate a password
        password = generate_password()
        # Print the generated password
        print("Generated password: " + password)

main()
