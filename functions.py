#Find highest even number inside the list

def highest_even(li):

    highest = 0

    for i in li:
        if i % 2 == 0 and i > highest:
            highest = i

    return highest

li = [44, 100, 4, 8, 11, 23, 80]

print(highest_even(li))