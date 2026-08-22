from cryptography.fernet import Fernet

'''
def write_key():
    key= fernet.generete_key()
    with open("Key.key", "wb") as Key_file:
        Key_file.write(key) '''

def load_key():
    file= open("Key.key","rb")
    Key=file.read()
    file.close()
    return Key

Key= load_key()
fer=Fernet(Key)

def view():
    with open('passwords.txt','r') as f:
        for line in f.readlines():
            data=line.rstrip()
            user,passw = data.split("!")
            print("User:",user,", password:",fer.decrypt(passw.encode()).decode())

def add():
    name=input ("Acoount name: ")
    pwd=input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + ""+ fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode=input(" Would you like to ass a new password or view existing ones or quit (View,Add,Q)? ").lower()
    if mode=="q":
        break
    if mode== "view":
        view()
    elif mode=="add":
        add()
    else:
        print("Invalid mode.")
    continue

