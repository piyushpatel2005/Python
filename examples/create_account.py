def main():
    full_name = get_full_name()
    print()

    password = get_password()
    print()

    first_name = get_first_name(full_name)
    print("Hi", first_name, ", thanks for creating an account.")

def get_full_name():
    while True:
        name = input("Enter full name: ").strip()
        if " " in name:
            return name
        else:
            print("You must enter your full name.")

def get_password():
    while True:
        password = input("Enter password: ").strip()
        digit = False
        cap_letter = False
        for char in password:
            if char.isdigit():
                digit = True
            elif char.isupper():
                cap_letter = True
        if digit == False or cap_letter == False or len(password) < 8:
            print("Password must be 8 characters or more \n"
                + "with at least one digit and one uppercase letter.")
        else:
            return password

def get_first_name(full_name):
    index1 = full_name.find(" ")
    first_name = full_name[:index1]
    return first_name

if __name__ == "__main__":
    main()
