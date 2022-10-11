import hashlib
import time
import string
import secrets

letter = string.ascii_letters # concatenation of letters lowercase and uppercase
digits = string.digits # the string containing the numbers 0 to 9
special_char = string.punctuation  # constant is the string of all special characters

alphabet = letter + digits + special_char # concatenate the above string constants to get the alphabet
pwd_lenght = 12


def pwd_generator():
    while True: # infinite loop
        pwd = ''
        for i in range(pwd_lenght):
            pwd += ''.join(secrets.choice(alphabet))
    
    # setting up the conditions
        if (any(char in special_char for char in pwd) and sum(char in digits for char in pwd)>=2):
            break

    print(pwd)



def signup():
    # getting user inputs
    email = input("Enter email address: ")
    pwd_gen = input("Type 'g' to generate new password or type 'm' to enter your own password: (g/m): ")
    if pwd_gen == 'g':
        pwd_generator()
    elif pwd_gen == 'm':
        pwd = input("Enter your password: ")
        
        conf_pwd = input("Confirm password: ")

    # email slicer
    for i in range(len(email)):
        if email[i] == '@':
            username  = email[:email.index('@')]
        else:
            domain = email[email.index('@') + 1:]
     
     # setting up the conditons
    if conf_pwd == pwd:
        enc = conf_pwd.encode()
        hash1 = hashlib.md5(enc).hexdigest()

    # saving the data
        with open("credentials.txt", "w") as f:
            f.write(email + "\n")
            f.write(hash1)
        f.close()
        time.sleep(2)
        print(f" Hello {username}, You have registered successfully!")
        print(f'Your user Name is {username} and domain is {domain}')
    else:
        print("Password did not match")



def login():
    email = input("Enter your email: ")
    pwd = input("Enter your password: ")

    auth = pwd.encode()
    authhash = hashlib.md5(auth).hexdigest()

    with open("credentials.txt", 'r') as f:
        stored_email, stored_pwd = f.read().split("\n")
    f.close()

    if email == stored_email and authhash == stored_pwd:
        print("Logged In Successfully!")
    else:
        print("LogIn Failed!")



while 1:
    print("********** Login System **********")
    print("1.Signup")
    print("2.Login")
    print("3.Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        signup()
    elif ch == 2:
        login()
    elif ch == 3:
        break
    else:
        print("Wrong Choice!")
