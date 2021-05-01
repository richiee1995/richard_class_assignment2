shopping_list = ['bread', 'milk', 'eggs', 'oranges', 'chicken']
print(shopping_list)

bread = 9.42 
milk = 5.57
eggs = 3.25
oranges = 13.40 
chicken = 7.50 



print (bread+milk+eggs+oranges+chicken)
print (bread+milk+eggs+oranges+(chicken*6)) 

#one line of code for ex1 ????


def all_the_snacks(snack):
    print ((snack)*100)

all_the_snacks('kitkat')    



def all_the_snacks(snack):
    print ((snack)*100)

all_the_snacks('bread')    



def all_the_snacks(snack):
    print ((snack)*100)

all_the_snacks('milk') 



def all_the_snacks(snack):
    print ((snack)*100)

all_the_snacks('eggs') 



def all_the_snacks(snack):
    print ((snack)*100)

all_the_snacks('oranges') 



def all_the_snacks(snack):
    print ((snack)*100)

all_the_snacks('chicken') 


def all_the_snacks(snack):
    print ((snack)*100)

all_the_snacks(20) 
#Result is number is multiplied by 100, i.e 20*100=2000. I expected an error. 


def all_the_snacks(snack):
    print ((snack + ' ')*100)

all_the_snacks('kitkat') 



def all_the_snacks(snack):
    print ((snack + ' ')*100)

all_the_snacks('milk') 


def all_the_snacks(snack):
    print ((snack + ' ')*100)

all_the_snacks('bread') 



def all_the_snacks(snack):
    print ((snack + 'eggs')*100)

all_the_snacks('kitkat') 

def all_the_snacks(snack):
    print ((snack + ' ')*100)

all_the_snacks('kitkat') 


def all_the_snacks(snack):
    print ((snack + ' ')* (print_number))

number = 3 
print_number = int(number)
all_the_snacks('kitkat') 


#THIS WORKS! SOLVED
#def item_check(item):
#    print(item in health)

#health = ['pizza', 'frozen custard', 'apples']
#item_check('pizza')


def grocery_list(item):
    print (item in items_to_check)
items_to_check = ['icecream', 'pineapples', 'beans', 'apples'] 
grocery_list('beans') 


def grocery_list(item):
    print (item in items_to_check)
items_to_check = ['icecream', 'pineapples', 'beans', 'apples'] 
grocery_list('mangoes') 


#def price_matcher ()

import random 
def price_matcher ():
    print(random_item)

grocery_list = {'watermelon': 1.55, 'avocadoes' : 2.30, 'honey': 1.10, 'flour':1.75 }
random_item = random.choice(list(grocery_list.items())) 
price_matcher() 

 
def all_the_snacks(snack):
    print ((snack + ',')*100)

all_the_snacks('kitkat') 

def all_the_snacks(snack):
    print ((snack + '!')*42)

all_the_snacks('kitkat')

def april_swapper():
    my_color = input('My favourite color is ')
    neighbors_color = input('Neighbors favourite color is ')
    print('My favourite color is', my_color,  'and my neighbors favourite color is', neighbors_color)
    print('My favourite color is now', neighbors_color,  'and my neighbors favourite color is now', my_color, 'when swapped')
    

april_swapper() 





