#Nonlocal used to pull variable from outer funtion/global scope
def outer():
    x = "local"
    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)  # inner: nonlocal
    inner()
    print("outer:", x)      # outer: nonlocal
outer()

#inner:nonlocal
#outer:nonlocal