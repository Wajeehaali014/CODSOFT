import random

def Password_Generator():

    sp_characters = "~@#$%^&*()<>/"
    uppercase_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase_alphabet = "abcdefghijklmnopqrstuvwxyz"
    random_digit = str(random.randint(0, 9))
    random_sp_characters = random.choice(sp_characters)
    random_uppercase_alphabet = random.choice(uppercase_alphabet)
    random_lowercase_alphabet = random.choice(lowercase_alphabet)

    print("**********************************")
    print("WELCOME TO THE PASSWORD GENERATOR")
    print("**********************************")

    length = int(input("Please specify the length of the password (Minimum length must be 5):"))

    if length <= 4:
        print("Enter Valid Length")

    while length > 4:

        print("What do yo want?")
        print("1). Complex Password")
        print("2). Simple Password")
        print("3). Exit")

        choice = int(input("Enter your choice number: "))

        if choice == 1:
            random_complex_password = random_digit + random_sp_characters + random_lowercase_alphabet + random_uppercase_alphabet
            remaining_length = length - 4
            remaining_cp = ''.join(random.choices(sp_characters + uppercase_alphabet + lowercase_alphabet + random_digit, k=remaining_length))
            generated_password = random_complex_password + remaining_cp
            print(f"Here's your password: {generated_password}")
            break

        elif choice == 2:
            generated_password = ''.join(random.choices(uppercase_alphabet + lowercase_alphabet + random_digit, k=length))
            print(f"Here's your password: {generated_password}")
            break

        elif choice == 3:
            break

        else:
            print("Enter the valid choice")

Password_Generator()
