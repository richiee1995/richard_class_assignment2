# ccna_class_labs
This are the labs for the CCNA class. I will only provide the labs here
Clone this repository, Create a new repository and push your assignment to it and send me the link in slack. 
That said, we will also run this in the class so much sure this is a python file so that you can run it

For each of these sections, a .py file is required. i.e, you would create a variables.py file for the variables section. 
## Variables
1. Save a copy of your favorite snack in a variable. Print your snack 100 times.
2. Ask as a friend for their favorite snack. Save it as a variable. You should now have two variables. Add(concantenate) them together and print the result 100 times
3. Using the [] notation, create a list of 5 grocery items and save it as a variable. 
4. Using the variable from exercise 3 and the your friends snack from exercise 2, test if your friends snack is in the grocery list. 
5. Using the "fast swapping" to swap your favorite snack with your friends. Print both variables to see the result. Are you happy or sad with your new snack choice.

## Python Loops:
1. Write a for loop that prints out every character in the string 'blood-oxygenation level dependent functional magnetic resource imaging'. 
2. Crreate a grocery list of 5 items or more. Write a for loop that prints out every item with a message 'Note to self, buy'
3. Write a for loops that prints out a numbered list of your grocery list
4. Clearly your favorite snack is more important than anything else on your grocery list. Modify excercise 2 to use a 'break' statement that should stop the printing once yuur favorite snake has been found on the grocery list. Bonus, if your snack is not on the list, have your program print a warning at the end. 
5. Previously, we printed several copies of a string using the * operator. Print 10 copies of your favorite snack using a while loop. 
6. Mix and Match! White a while loop that uses * to print several copies of your favorite snack per line. Print out 10 lines with the number of copies per line corresponding to the line number. i.e your first line should have one copy and your last line should have 10. 
7. Wite a while loop that prints 100 copies on the same line. hint use + 
8. Use range to write a for loop that prints a numbered grocery list
9. Use enumerate to print out a numbered grocery list. 
10. Create a dictionary with your grocery items. For each item, have an appropriate value as the value. 
11. Challenge: use the .split() method to write a for loop that prints all words in 'blood-oxygenation level dependent functional magnetic resource imaging'. Hint: use help(split)
12. Challenge: Write a guess my number game that generates a random number and gives your user a fixed number of tries to guess the number. Use input to get the user's guesses. Think about what kind of loop you might use and how you would provide fedback based on the use input. Hint: what type does input return. You might need to convert this to a more useful type. What happens if your user inputs something that is not a number??

## Flow Control
1. Change the loop below so that it prints the numbers from 1 to 10
    for i in range(9)
        print(i)
    
2. Using a loop and enumerate, write a function getindex(string, character) to recreate the string method.index. 
   "skyscraper".index("c")

   4

   getindex("skyscraper", 'c')

   4

3. Using the shout functtion that you did previously, write a function shout_words(sentence) which takes a string argument and shouts each word on its own line. 
   shout_words("Everybody likes bananas")
   #EVERYBODY
   #LIKES
   #BANANAS

4. white a function extract_longer(length, sentence) that  takes a sentence and a word length and returns all words that are longer or equal to the given length. If no words match the length, return false. 

   etract_longer(5, "Try not to interrupt the speaker")
  ["interrupt", "speaker']

  extract_longer(7, "Sorry about the mess")
  #False
## Python Functions
1. Make a shopping list 5 items that you need at the grocery store. Remember to use quotes. 
  use print() so that each of your items displays
2. Your groceries ring up as 9.42, 5.57, 3.25, 13.40, and 7.50 respectively. Use python as a handy calculator to add these values. 
3. But wait, you decide to buy 5 more of the last item. Recalculate your total. 
4. Can you figure out how to get the output of exercise one with only one print statement. if yes can you do it with only one line of code. 
5. Write an all_the_snacks fuction that takes a snack (string) and uses * to print it 100 times. Test your function by using all the items on your shopping list. what happens if you enter a number into your function? Result what you expected?
6. You may have noticed that your all_the_snacks function prints out the results all squished together. Rewrite the all_the_snacks function to take an additional argument spacer. Use the + to combine the spacer and the snack before multiplying. Test your function with different inputs. What happens if you use a string for both snacks and the spacer? Both Numbers? A string and an integer? Is this what you expected?
7. Rewrite the all_the_snacks such that it takes a num variable allowing you to customize the number of times that you can print out the snacks. 
8. Write a grocery_list function which takes an item and returns true or false if the item is on your grocery list. 
9. Write a price_matcher function that takes no arguments but prints a random grocery item and a price from your list everytime its run. 
10. Rewrite the all_the_snacks function so that the num and spacer have defaults of '100' and ','. Usinig your favorite snack as input try running your function with no additional input. 
11. Try running the all_the_snacks function with the '! ' and no additional input. How would you run it while inputing your favorite snack and 42 as the num while keeping the default spacer? Can you use this method to enter spacer and num in reverse order. 
12. Write an april_swapper function that takes an input to get your favorite color, saved as my_color and another input saved as neighbors_color. Use a print statement to declare what your favorite color and your neighbors favorite colors are. Now add a line that prints the same values but swapping your favorite color for your neighbors. 

## Python Functions part deux
1. Write a function isDivisibleBy7() to check if a number is divisible by 7
2. write a function isDivisibleby(num, divisor) to check to check if num is evenly divisble by divisor
3. Make a function shout(word) that accepts a string and returns the string in Capital letters with and exclamation mark
4. Write a function introduce() which will ask a user for their name and shout it back to them 
5. Write a function snack_check() that takes a string snack and prints True or False depending on whether the snack is your favorite snack or not. 
6. Write a snack_check() function that takes a string snack and prints an appropriate responds depending on whether the input is your favorite snack or not. 
7. Write a function in_grocery_list() to test if an item grocery_item is a string. Print a message warning if its not
8. Write a function you_won() that randonly picks a number from your price list 9.42, 5.57, 3.25, 13.40, and 7.50 and prints True or False depending on whether the random number is greater than 10. 
9. Write a function that imports datetime and uses it to determine current time The function should print an appropriate message based on the time. for example if the time is between 0900 and 1300 H: print "Morning Lecture Time"
10. Write a function called volume which computes and returns the volume of a box when given the width, length and height. 


## Data Structures
1. if we list all natural numbers that are multiples of 3 and 5 we get 3, 5, 6 and 9. If you sum these numbers  we get 23. 
   find the sum of the all the multiples of 3 or 5 below 1000

2. Write a function which takes a list as a parameter and returns a second list that contains any items that appear more than once in the first list.
   duplicates([1,2,3,5,6,4,3,6]) should return [3,6]
   what should duplicates(['cow', 'pig', 'goat', 'pig'])return?

3. write a function that takes no arguments but ask the user for their name, their address, their ZIP code, their age, their hair color
   and their eye color. Store all of this info in a dictionary. Print out every key value pair of this dictionary 
