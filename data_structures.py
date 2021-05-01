def sum_of_numbers():
    print(sum([i for i in range(1000) if i % 3 == 0 or i % 5 == 0]))

sum_of_numbers()

def duplicates(list_of_elements):
    for elem in list_of_elements:
        if elem not in list_1:
            list_1.append(elem)
        else:
            print(elem, end=',')

list_1 = [] 
duplicates([1,2,3,5,6,4,3,6])


def duplicates(list_of_elements):
    for elem in list_of_elements:
        if elem not in list_1:
            list_1.append(elem)
        else:
            print('\n',elem, end=',')

list_1 = [] 
duplicates(['cow', 'pig', 'goat', 'pig']) 


def personal_info():
    print ('\n', database)

    
name = input('\n''What is your name? ') 
address = input('What is your address? ') 
zip_code = input('What is your ZIP Code? ') 
age = input('What is your age? ') 
hair_colour = input('What is your hair colour? ') 

database = {'Name': name, 'Address' : address, 'ZIP Code' : zip_code, 'Age' : age, 'Hair colour' : hair_colour} 

personal_info() 





