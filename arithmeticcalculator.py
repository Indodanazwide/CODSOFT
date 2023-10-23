import string
import random

def password_check():
    password_length = input("Enter password length from 8 to 15: ")

    while not (8 <= int(password_length) <= 15):
        print("\nInvalid input. Password length must be between 8 and 15.")
        password_length = input("\nEnter password length from 8 to 15: ")

    return int(password_length)

def password_generator():
    password_length = password_check()
   
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    specials = string.punctuation

    password_panctuation = random.sample(specials, 2)
    password_numbers = random.sample(digits, 2)
    password_uppercase = random.sample(uppercase_letters, 1)
    password_lowercase = random.sample(lowercase_letters, password_length - 5)
    
    string_password = password_panctuation + password_numbers + password_uppercase + password_lowercase
    
    random.shuffle(string_password)
    password = "".join(string_password)
    
    print("Recommended password is: " + password)

password_generator()
