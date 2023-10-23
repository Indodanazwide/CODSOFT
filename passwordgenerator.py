import random, string

def check_password():
    global password_length
    while password_length <= 5:
        print("Invalid length!")
        password_length = int(input("Enter desired password length(must be greater than 5): "))


def password_generator():
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_letters = string.punctuation

    all_char = uppercase_letters+lowercase_letters+digits+special_letters
    char_list = list(all_char)
    random.shuffle(char_list)
    join_char = "".join(char_list)

    made_password = random.sample(join_char, password_length)

    password = "".join(made_password)

    print(f"\nYour password is {password}")

password_length = int(input("Enter desired password length(must be greater than 5): "))

check_password()

password_generator()
