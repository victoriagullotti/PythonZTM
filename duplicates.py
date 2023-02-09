#List of characters with duplicates

import pdb

some_list = ['a', 'b', 'c', 'd', 'a', 's', 'c']

#Function returns character if duplicate present or ''
#Not used!!!
def is_duplicate(char):
    count = 0

    for i, character in enumerate(some_list):
        # pdb.set_trace()
        # print(f'{char}  {character} {count}')
        
        if char == character:
            count += 1
    
    if count > 1:
        return True
    else:
        return False 

list = '' #list of duplicates

for i in some_list:
    
        if some_list.count(i) > 1:

            try:
                list.index(i)
                
            except ValueError:
                list += ' ' + i
                continue;
    

print('List of duplicated items: ' + list)