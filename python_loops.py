for x in 'blood-oxygenated level dependent functional magnetic resource imaging':
    print(x) 

note = 'Note to self, buy'
grocery_list = ['bread', 'chocolate', 'milk', 'onions', 'mangoes']
for item in grocery_list:
    print ((note),(item)) 


for i, item in enumerate (grocery_list, 1):
    print (i,'.',item)


for item in grocery_list:
    if item == 'kitkat':
        break
    print (item) 
else:
    print ('Warning, no favourite snack')  


favourite_snack = 'kitkat' 
i = 1
while i<=10:
    print (favourite_snack)
    i=i+1 


j = 1
while j<=10:
    print(favourite_snack * j)
    j=j+1


k = 1
while k <= 100:
    print(favourite_snack, end=' ') 
    k=k+1 
    ('\n')



for i in range(0 , len(grocery_list)):
    Numbered_list = grocery_list[i]
    print(f'\n\n{i}: {Numbered_list}')


for i, item in enumerate (grocery_list, 1):
    print (i,'.',item)

bread = 'bread: a food made of flour, water, and yeast mixed together and baked'
chocolate = 'chocolate: a food in the form of a paste or solid block made from roasted and ground cacao seeds'
milk  = 'milk: an opaque white fluid rich in fat and protein, secreted by female mammals for the nourishment of their young'
onions = 'onion: a swollen edible bulb used as a vegetable, having a pungent taste and smell and composed of several concentric layers'
mangoes = 'mango: a fleshy, oval, yellowish-red tropical fruit that is eaten ripe or used green for pickles or chutneys' 

word_test = 'blood-oxygenated level dependent functional magnetic resource imaging'
for word in word_test.split():
    print (word) 


import random 
number = random.randrange(1, 50)
guess = int(input('Guess my number between 1 and 50. You have five tries: '))
tries = 1
while guess != number:
    if guess < number:
        print ('Try a higher number')
        guess = int(input('\nGuess my number between 1 and 50: '))
    else:
        print ('Try a lower number')
        guess = int(input('\nGuess my number between 1 and 50: '))

tries += 1
if tries <= 5:
    print('Sorry, you have failed to guess correctly. The number was', number, '\n Press any key to exit!') 


print ('Horray! You have guessed correctly!\n')

input ('\nPress enter key to exit.')








 


