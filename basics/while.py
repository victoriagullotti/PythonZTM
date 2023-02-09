# While loop
i = 0

while i < 50:
    # i = i + 1
    i += 1
    print(i)


# Print numbers 1 to 50 and than print Done
i = 0
while i < 50:
    i = i + 1
    print(i)
else:
    print('Done')

# Most common use!!!
while True:
    input('Hey. Say something... ')
    break

# Waiting for specific word - Bay
while True:
    inp = input("Say something ")
    if inp == 'Bay':
        print('See you soon ')
        break

ln = [1, 2, 3]
i = 0

# Break, pass, continue
while i < len(ln):
    continue
    print(ln[i]) #this never prints bacause of continue 

#Use pass as a temporary thing
while i < 10 :
    pass # we are not sure what is going to be here yet !!!