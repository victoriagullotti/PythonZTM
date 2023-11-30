import re

regex = '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$'  
input = input("Enter your email: ")

def check(email):

    try:
        m = re.match(regex, email)
        if(m == None):    
            print("Invalid Email")
        else:  
            print("Valid Email")
    except:
        print("Invalid Email")

check(input)