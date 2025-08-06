#******************************************************************************
# missing.py
#******************************************************************************
# Eduardo E
#

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


#ask the user for the names
names = str(input('Enter some names on a single line: '))

#turn input into a list
name_list = names.split()


exceptions = []



for inx in range(len(name_list)):
#turrn each element of the list into a string and put the first letter of that string into a list
    check_name = str(name_list[inx])
    exceptions += check_name[0]

#remove all elements in exceptions from the given letters list    
for letter in exceptions:
        letters.remove(letter)
        
    
print('Missing Letters:', end = ' ')

for abc in letters:
    print(f'{abc}', end = ' ')
        

