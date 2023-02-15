import re

#Any letter followed by a dot and then a letter a or A/a!!!!  
regex = r'?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[\u0020-\u002f\u003A-\u0040\u005B-\u0060\u007B-\u007E]).{8,}'    

input = input("Enter the password: ")

def check(password):

    try:
        m = re.match(regex, password)
        
        if(m == None):    
            print("Invalid Password")
        else:  
            print("Valid Password")
    except:
        print("Invalid Password")

check(input)