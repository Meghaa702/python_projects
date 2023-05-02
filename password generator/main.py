import random
import string

def generate_password(length=12, uppercase=True, lowercase=True, digits=True, symbols=True):
    letters_upper = string.ascii_uppercase if uppercase else ''
    letters_lower = string.ascii_lowercase if lowercase else ''
    numbers = string.digits if digits else ''
    symbols = string.punctuation if symbols else ''

    characters = letters_upper + letters_lower + numbers + symbols

    if not characters:
        raise ValueError("At least one character set must be included in the password")

    password = ''.join(random.choice(characters) for _ in range(length))

    return password

password = generate_password(length=16, uppercase=True, lowercase=True, digits=True, symbols=False)
print("your new generated password is:",password)
