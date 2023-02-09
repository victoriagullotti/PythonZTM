# Decorators
def my_decorator(func):
    #We are able to pass as many args and keywords as possible!!!
    def wrap_func(*args, **kwargs):
        print('********************************')
        func(*args, **kwargs)
        print('********************************')
    return wrap_func

@my_decorator
def hello(greeting, emoji=':)'):
    print(greeting, emoji)

hello('Hi')

#********************************
#Hi :)
#********************************   


