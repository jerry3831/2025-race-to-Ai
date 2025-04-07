# DICTIONARIES 
# this file demonstrates how to implement python dictionaries as well as 
# how to traverse them and loop thorugh them
# these data structures organize data as key value pairs

dict_1 = {'one':1,'two':2,'three':3}

# we can use the .items() built-in method of dictionaries to access and loop through dictionary items.
for key, value in dict_1.items():
    print(f"{key} : {value}")
print()
# dictionaries store data as key value pairs
#  a key can be any immutable type
#  values can either be mutable or immutable types
# values can also be of any data type

dict_2 = {
    'integers':[1,2,3,4],
    'floating-point-numbers':[1.3,3.4,34.6,2.0],
    ('pilars', 'huts'): True,
    'names':('john doe', 'janet smith')    
} # the dictionary contains strings and a tuple as keys, and hav two lists, a tuple and a boolean as values

for key in dict_2:
    # value accessed by passing the key as an index of the dictionary
    print(f'{key} : {dict_2[key]}')
print()

# example
# using a dictionary to store details as follows
#  >Book title
#  >Author
#  >ISBN
#  >Number of copies

def organizer():
    print('Book inventory dictionary example')
    title = input("Book title: ")
    author = input("Author: ")
    ISBN = input("ISBN: ")
    copies = int(input("Number of copies: "))
        
    books = {
        "Title" : title,
        "Author" : author,
        "ISBN" : ISBN,
        "Number of copies" : copies
    }
    
    # displaying details for each book
    for book in books:
        print(f"{book} : {books[book]}")
    print()
    
entries = int(input("Number of entries: ")) # Total number of entries
for entry in range(entries):
    print(f'Entry {entry+1}')
    organizer()
    print()
    














 