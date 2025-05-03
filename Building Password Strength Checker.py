#Password Strength Checker Program
import re

#Password must be at least 12 charcters long
password = input ("Enter Your Password. ")
if len(password) < 12:
    print("Password must be at least 12 characters long.")
#Password must contain at least one uppercase letter.
elif not re.search("[A-Z]", password):
    print("Password must contain at least one uppercase letter.")
#Password must contain at least one lowercase letter.
elif not re.search("[a-z]", password):
    print("Password must contain at least one lowercase letter.")
#Password must contain at least one number
elif not re.search("[0-9]", password):
    print("Password must contain at least one digit.") 
#Password must contain at least one special character.
special_characters = re.compile(r"[@_!#$%^&*()<>?/\|}{~:].")
if not re.search("[!@#$%^&*(),.?\":{}|<>]", password):
    print ("Password should contain at least one special character.")
else:
    ("Strong: Password meets the criteria.")

def password():

    print ('enter password')
    print ()
    print ()
    print ('the password must be at least 6, and no more than 12 characters long')
    print ()

    password = input ('type your password    ....')


    weak = 'weak'
    med = 'medium'
    strong = 'strong'

    if len(password) >12:
        print ('password is too long It must be between 6 and 12 characters')

    elif len(password) <6:
        print ('password is too short It must be between 6 and 12 characters')


    elif len(password)    >=6 and len(password) <= 12:
        print ('password ok')

        if password.lower()== password or password.upper()==password or password.isalnum()==password:
            print ('password is', weak)

        elif password.lower()== password and password.upper()==password or password.isalnum()==password:
            print ('password is', med)

        else:
            password.lower()== password and password.upper()==password and password.isalnum()==password
            print ('password is', strong)
pythonpython-3.x
