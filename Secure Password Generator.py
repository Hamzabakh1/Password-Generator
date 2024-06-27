import random
import string

def generate_password():
    # Define the character sets
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special_characters = "@#$!%*?&_"

    # Ensure the password contains at least one character from each set
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special_characters)
    ]

    # Fill the rest of the password length with random characters from all sets
    all_characters = uppercase + lowercase + digits + special_characters
    password_length = random.randint(8, 25)

    password += [random.choice(all_characters) for _ in range(password_length - 4)]

    # Shuffle the password list to ensure randomness
    random.shuffle(password)

    # Convert the list to a string and return it
    return ''.join(password)

# Generate and print a password
print(generate_password())
