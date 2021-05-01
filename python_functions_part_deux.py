
# Python program to check whether a number is divisible by 7

# Function to check whether a number is divisible by 7
def isDivisibleBy7(num) :
	
	# If number is negative, make it positive
	if num < 0 :
		return isDivisibleBy7( -num )

	# Base cases
	if( num == 0 or num == 7 ) :
		return True
	
	if( num < 10 ) :
		return False
		
	# Recur for ( num / 10 - 2 * num % 10 )
	return isDivisibleBy7( num / 10 - 2 * ( num - num / 10 * 10 ) )
	
# Driver program
num = 207
if(isDivisibleBy7(num)) :
	print ("Divisible")
else :
	print ("Not Divisible")




def isDivisibleby(num, divisor):
	if num % divisor == 0:
		print ('Evenly divisible')
	else:
		print ('Not evenly divisible')

isDivisibleby(15, 5)	
isDivisibleby(15, -8)	


def shout(word):
	print (word.upper(),'!')

shout('My name is Richard')
shout('print this in upper case')

#REMOVE # TO ACTIVATE COMMAND

#def introduce():
#	print(name.upper(), '!')

#name = input('What is your name? ')
#introduce()



def snack_check():
	print(favourite_snack in snack)

snack = ['marshmallows', 'soda', 'cotton-candy', 'meat-pie']
favourite_snack = 'cotton-candy'
snack_check()


def snacks_check ():
	if fav_snack in snacks:
		print ('Your favourite snack is there')
	else: 
		print ('Your favourite snack is not there')

snacks = ['hotdog', 'muffin', 'yoghurt', 'peanuts', 'burger']
fav_snack = 'muffin'
snacks_check()


def in_grocery_list():
	if type(grocery_item) == str:
		print (grocery_item, 'is a string')
	else:
		print (grocery_item, 'is not a string')

grocery_item = 'Eggs'
in_grocery_list()




import random
def you_won():
	if random_number > 10:
		print (random_number, 'True')
	else:
		print (random_number, 'False')


price_list = [9.42, 5.57, 3.25, 13.40, 7.50] 
random_number = random.choice(list(price_list))
you_won() 


from datetime import datetime, time
def current_time():
	if morn_lectures <= time_now <= aftern_lectures:
		print(time_now, 'Morning Lecture Time')
	elif aftern_lectures <= time_now <= aftern_lecture_end:
		print(time_now, 'Afternoon Lecture Time')
	else:
		print (time_now, 'Non-lecture hours') 

morn_lectures = time(9, 0, 0)
aftern_lectures = time(13, 0, 0)
aftern_lecture_end = time(17, 0, 0) 
time_now = datetime.now().time()	
current_time() 


def volume():
	print('Volume of the box is', (length*width*height), 'cm cubed')

length = int(input('Input the length of the box in cm '))
width = int(input('Input the width of the box in cm '))
height = int(input('Input the height of the box in cm '))
volume() 