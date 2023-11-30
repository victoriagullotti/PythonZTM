import re

#Any letter followed by a dot and then a letter a or A/a!!!!  
pattern = re.compile("?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[\u0020-\u002f\u003A-\u0040\u005B-\u0060\u007B-\u007E]).{8,}")

password = 'Aa1234567'

def check(password):

    try:
        m = re.search(pattern, password)
        
        if(m == None):    
            print("Invalid Password")
        else:  
            print("Valid Password")
    except:
        print("Invalid Password")


check(password)