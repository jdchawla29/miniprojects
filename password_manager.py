from cryptography.fernet import Fernet

"""
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
"""


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key)


def view():
    with open("passwords.txt", "r") as file:
        for line in file.readlines():
            acc, pwd = line.rstrip().split("|")
            print("Account:", acc, "| Password:", fer.decrypt(pwd.encode()).decode())


def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open("passwords.txt", "a") as file:
        file.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


while True:
    mode = input(
        "Would you like to add a new password or view existing ones? (view/add). Press q to exit. "
    ).lower()
    if mode == "q":
        quit()
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue
