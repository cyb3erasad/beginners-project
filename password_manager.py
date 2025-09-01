from cryptography.fernet import Fernet

# def write_key():
#     key = Fernet.generate_key()
#     with open("Key.Key", 'wb') as key_file:
#         key_file.write(key)


def load_key():
    file = open("Key.Key", "rb")
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key)





def view():
    with open("passwords.txt", 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:",
                  fer.decrypt(passw.encode()).decode())



def add():
    name = input("Enter Account Name: ")
    pwd = input("Enter Password: ")

    with open("passwords.txt", 'a') as f:
       f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")
       



while True:
    mode = input("Would you like to add a new password or view existince ones? (view, add) press q to exit: ").lower()

    if mode == 'q':
        break
    if mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print("Invalid mode!")
        continue        