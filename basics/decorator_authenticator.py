# Create an @authenticated decorator that only allows the function 
# to run if the users has 'valid' set to True:

users = {
    'name': 'Vicky',
    'valid': True #changing this will either run or not run the message_friends function.
}

def authenticator(fn):
    def wrapper(*args, **kwargs):
        result = 0

        for argument in args:
            
            if users.get('name') == argument:
                print('Hi ' + argument) 
                result = fn(*args, **kwargs)
                break        
        
        if result == 0:
            print('You need to log in first...')

        return result
    return wrapper

@authenticator
def run_function(user):
    print('Doing something')

run_function('Victoria') #You need to log in first...
run_function('Vicky')   # 
