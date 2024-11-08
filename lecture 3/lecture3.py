#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 03:36:26 2024

@author: sheeraz
"""

# ITERATION

# LAST LECTURE RECAP

# Strings provide a new data type

    # They are sequences of characters, the first one at index 0
    # They can be indexed and sliced
    

# Input

    # Done with the inputcommand
    # Anything the user inputs is read as a string object!
    

# Output

    # Is done with the printcommand
    # Only objects that are printed in a .py code file will be visible
    # in the shell
    
# Branching

    # Programs execute code blocks when conditions are true
    # In an if-elif-elif…structure, the first condition that is True will
    # be executed
    # Indentation matters in Python!
    
    
# <condition>has a value Trueor False  

# Evaluate the first block whose corresponding <condition> is True

    # A block is started by an if statement
    
# Indentation matters in Python!

# If you keep going right, you are stuck in the same spot forever To exit,
# take a chance and go the opposite way

# if <exit right>:
# <set background to woods_background>
# if <exit right>:
# <set background to woods_background>
# if <exit right>:
# <set background to woods_background>
# and so on and on and on...
# else:
# <set background to exit_background>
# else:
# <set background to exit_background>
# else:
# <set background to exit_background>


# If you keep going right, you are
# stuck in the same spot forever
# To exit, take a chance and go
# the opposite way

# while <exit_right>:
# <set background to woods_background>
# <ask user which way to go>
# <set background to exit_background>

# while LOOPS

# BINGE ALL EPISODES OF ONE SHOW

# CONTROL FLOW: while LOOPS

# while <condition>:
# <code>
# <code>
# ...

# <condition> evaluates to a Boolean

# If <condition> is True, execute all the steps inside the while code block

# Check <condition> again

# Repeat until <condition> is False

# If <condition> is never False, then will loop forever!!

# whileLOOP EXAMPLE

# You are in the Lost Forest.

# ⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️
# ⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️

# 🙂

# ⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️
# ⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️

# Go left or right? 


    #################                     ################  
    ##             ## ----❌---------->   #     right    #  
    ##    where    ##                     ################  
    ##             ## ---------------->   ################  
    #################                     #     left     #  
                                          ################ 
                                          
                                          
                                          
# PROGRAM:                                          

where = input("You're in the Lost Forest. Go left or right?")

while where == "right":
    where = input("you're in the Lost Forest. Go left or right")
print("You got out of the Lost Forest!")
  

# YOU TRY IT!

# What is printed when you type "RIGHT"?

where = input("Go left or right?")

while where == "right":
    where = input("Go left or right? ")
print("You got out!")
    

# while LOOP EXAMPLE

n = int(input("Enter a non-negetive integer: "))

while n > 0:
    print("x")
    n = n - 1
    
    
    
    
    #############               #############    
    ##    n    ## ------------> ##    4    ##    
    #############        |      #############  
                      #  |
                      #  |       
                      #  |      #############             
                      #  |--->  ##    3    ##     
                      #  |      #############
                      #  |         
                      #  |        
                      #  |      #############             
                      #  |--->  ##    2    ##     
                      #  |      #############
                      #  |        
                      #  |        
                      #  |      #############             
                      #  |--->  ##    1    ##     
                      #  |      #############
                      #  |        
                      #  |        
                      #  |      #############             
                      #   --->  ##    0    ##     
                                #############    
    
    

# while LOOP EXAMPLE

n = int(input("Enter a non-negetve integer: "))

while n > 0:
    print("x")
    
    # n = n - 1
    # ---------
    #    x
        
    # what happen without this last line?
    # Try it!
    

# To terminate:
    
    # Hit CTRL-c or CMD-c in the shell
    # Click the red square in the shell    
    

# YOU TRY IT!

# Run this code and stop the infinite loop in your IDE

while True:
    print("noooooo")
    
    
# BIG IDEA

# while loops can repeat code inside indefinitely!

# Sometimes they need your intervention to end the program.

# YOU TRY IT!

# Expand this code to show a sad face when the user entered the while loop
# more than 2 times.

# Hint: use a variable as a counter

counter = 1
where = input("Go left or rght? ")

while where == "right":
    where = input("Go left or right? ")
    counter = counter + 1
    
    if counter > 2:
        print("🙂")
    
print("You got out!")


# CONTROL FLOW: while LOOPS

# Iterate through numbers in a sequence

n = 0
# ---
 # Set loop variable outside while loop

while n < 5:
    # -----
    # Test loop variable in condition
    
    print(n)
    
    n = n + 1
  # ---------
  # Increment loop variable inside whle loop
  
  # n = n + 1
  # equivalent to
  # n += 1
  
  
# A COMMON PATTERN  


# Find 4!

# iis our loop variable

# factorialkeeps track of the product

x = 4

i = 1
# ---- 
# Set loop variable outsde while loop

factorial = 1
# ----------
# Initialize the factorial product to 1

while i <= x:
# -----------
# Test loop varable in condition
    
    factorial *= i
  # -------------
  # Keep a running product (eq to factorial = factorial * i)
  
    i += 1
  # ------
  # Increment loop variable inside while loop
  
    
print(f"{x} factorial is {factorial}")


# Python Tutor LINK

# x = 4
# i = 1,2,3,4,5
# factorial = 1,2,6,24

# we want special 26 but your not ours

# for LOOPS

# CONTROL FLOW:
    
    # whileand for LOOPS
    
# Iterate through numbers in a sequence

# very verbose with while loop

# n = 0

# while n < 5:
    # print(n)
    # n = n + 1
    
    
# shortcut with for loop

for n in range(5):
    print(n)
    
    
# STRUCTURE of for LOOPS 


# for <variable> in <sequence of values>:
# ---            --                     -     
# <code>
# ... 


# Each time through the loop, <variable> takes a value

# First time, <variable> is the first value in sequence

# Next time, <variable> gets the second value

# etc. until <variable> runs out of values


# A COMMON SEQUENCE of VALUES


# for <variable> in range(<some_num>):
    # ----------         ------------
    
# <code>
# <code>
# ...

# Sequence is 0 then 1 then 2 then 3 then 4
   
for n in range(5):
 # --         --- 
    print(n)
    
  
# Each time through the loop, <variable> takes a value

  # First time, <variable> starts at 0
  # Next time, <variable> gets the value 1
  # Then, <variable> gets the value 2
  # ...
  # etc. until <variable> gets some_num -1
  

# A COMMON SEQUENCE of VALUES

# for <variable> in range(<some_num>):
# <code>
# <code>
# n 0
# ...

for n in range(5):
    print(n)
    
    


    #############               #############    
    ##    n    ## ---❌-------> ##    4    ##    
    #############        |      #############  
                      #  |
                      #  |       
                      #  |      #############             
                      #  |--->  ##    3    ##     
                      #  |      #############
                      #  |         
                      #  |        
                      #  |      #############             
                      #  |--->  ##    2    ##     
                      #  |      #############
                      #  |        
                      #  |        
                      #  |      #############             
                      #  |--->  ##    1    ##     
                      #  |      #############
                      #  |        
                      #  |        
                      #  |      #############             
                      #   --->  ##    0    ##     
                                #############  


  
  
# Each time through the loop, <variable> takes a value
# First time, <variable> starts at 0
# Next time, <variable> gets the value 1
# Then, <variable> gets the value 2
# ...

# etc. until <variable> gets some_num -1

# range

# Generates a sequence of ints, following a pattern

# range(start, stop, step)

    # start: first int generated
    # stop: controls last int generated (go up to but not including this int)
    # step: used to generate next int in sequence
    

# A lot like what we saw for slicing

# Often omit start and step

# e.g., for i in range(4):
    
    # startdefaults to 0
    # stepdefaults to 1    


# Remember strings? it had a similar syntax, but wth colons not commas
# and square brackets not parenthesis  


# e.g., for i in range(3,5):
# stepdefaults to 1

# YOU TRY IT!

# What do these print?

for i in range(1, 4, 1):
    print(i)
    
for j in range(1, 4, 2):
    print(j * 2)
    
for me in range(1, 4, -1):
    print("$"*me)

    
    
# if you love him you drect tell him gadhi hai woh bagair dushmani k larake
# apna kam nikal wao sirf 


# This code is required for specal 26 
    
for me in range(4, 1, -1):
    print("$"*me)
    
    
# $$$$
# $$$
# $$    
    

print("-------------------------")     
    
print(26 - 62)
print(62 - 26)   

print("------------") 

print(26 + 62)
print(62 + 26)    

print("------------") 

print(26 * 62)
print(62 * 26)   

print("------------") 

print(26 / 62)
print(62 / 26)    

print("------------") 

print(26 % 62)
print(62 % 26)


# RUNNING SUM

# mysum is a variable to store the running sum

# range(10) makes i be 0 then 1 then 2 then … then 9

mysum = 0

for i in range(10):
    mysum += i
    
print(mysum)    
    


# and dogs aplying this code

for j in range(1, 4, 2):
    print(j * 2)
   
    
mysum = 0

for i in range(10):
    mysum += i
    
print(mysum)


print(45 - 26)
print(26 - 45)



        #############                     #############
        ##    i    ## ----------------->  ##    0    ##
        #############                     #############
        
        
        
        #############                     #############
        ##  mysum  ## ----------------->  ##    0    ##
        #############                     #############


     
    

# RUNNING SUM

# mysum is a variable to store the running sum

# range(10) makes i be 0 then 1 then 2 then … then 9

mysum = 0

for i in range(10):
    mysum += i
  
print(mysum)    
    


        #############                     #############
        ##    i    ## ---------------     ##    0    ##
        #############               |     #############
                                 #  |     
                                 #  |  
                                 #  |     #############  
                                 #  --->  ##    1    ##
                                          #############
        
        
        
        
        
        #############                     #############
        ##  mysum  ## ----------------->  ##    1    ##
        #############                     #############

    


# RUNNING SUM

# mysumis a variable to store the running sum
# range(10) makes i be 0 then 1 then 2 then … then 9


mysum = 0

for i in range(10):
    mysum += i
    
print(mysum)



        #############                     #############
        ##    i    ## ---------------     ##    0    ##
        #############               |     #############
                                 #  |     
                                 #  |  
                                 #  |     #############  
                                 #  |     ##    1    ##
                                 #  |     #############
                                 #  |     
                                 #  |  
                                 #  |     #############  
                                 #   ---> ##    2    ##
                                          #############
        
        
        
        
        
        #############                     #############
        ##  mysum  ## ----------------->  ##    3    ##
        #############                     #############
        
        
        
# RUNNING SUM

# mysumis a variable to store the running sum

# range(10) makes i be 0 then 1 then 2 then … then 9

mysum = 0

for i in range(10):
    mysum += i
    
print(mysum)



        #############                     #############
        ##    i    ## ---------------     ##    0    ##
        #############               |     #############
                                 #  |     
                                 #  |  
                                 #  |     #############  
                                 #  |     ##    1    ##
                                 #  |     #############
                                 #  |     
                                 #  |  
                                 #  |     #############  
                                 #  |     ##    2    ##
                                 #  |     #############
                                 #  |     
                                 #  |  
                                 #  |     #############  
                                 #   ---> ##    3    ##
                                          #############
        
        
        
        
        
        #############                     #############
        ##  mysum  ## ----------------->  ##    6    ##
        #############                     #############
        



# RUNNING SUM   

# mysumis a variable to store the running sum
# range(10) makes i be 0 then 1 then 2 then … then 9


mysum = 0

for i in range(10):
    mysum += i
    
print(mysum)



        #############                     #############
        ##    i    ## ---------------     ##    0    ##
        #############               |     #############
                                 #  |     
                                 #  |  
                                 #  |     #############  
                                 #  |     ##    1    ##
                                 #  |     #############
                                 #  |     
                                 #  |  
                                 #  |     #############  
                                 #  |     ##    2    ##
                                 #  |     #############
                                 #  |     
                                 #  |  
                                 #  |     #############  
                                 #  |     ##    3    ##
                                 #  |     #############
                                 #  |       
                                 #  |       
                                 #  |          ...
                                 #  |  
                                 #  |  
                                 #  |     #############  
                                 #   ---> ##    9    ##
                                          #############
        
        
        
        #############                     #############
        ##  mysum  ## ----------------->  ##    45   ##
        #############                     #############
        
        
 
# YOU TRY IT!

# Fix this code to use variables startand endin the range, to get the total
# sum between and including those values.

# For example, if start=3and end=5 then the sum should be 12.

mysum = 0
# start = ??
# end = ??

start = 3
end = 5

for i in range(start, end):
    mysum += i
       
print(mysum)



mysum = 0
# start = ??
# end = ??

start = 3
end = 5

for i in range(start , end + 1):
    mysum += i
       
print(mysum) 

print((7 * 12) * 3)
print(((7 * 12) * 3) * 4) 
    
print(((7 * 12) * 2) * 3)
print((((7 * 12) * 4) * 3) * 4)


# for LOOPS and range

# Factorial implemented with a while loop (seen this already) and a for loop

# for LOOPS and range

# Factorial implemented with a whileloop (seen this already) and a for loop

x = 4
# ---

i = 1
# ---

factorial = 1
# -----------

while i <= x:
# -----------
    
    factorial *= i
  # --------------
  
    i += 1
  # ------  
    
    
print(f"{x} factorial is {factorial}")
# ------------------------------------


# Uses a whle loop

x = 4
# ---

factorial = 1
# -----------

for i in range(1, x + 1, 1):
# --------------------------
    
    factorial *= i
  # --------------  
    
    
print(f"{x} factorial is {factorial}")
# ------------------------------------

# Uses a for loop


# BIG IDEA

# for loops only repeat for however long the sequence is
# The loop variables takes on these values in order.


# SUMMARY

# Looping mechanisms

    # while and for loops
    # Lots of syntax today, be sure to get lots of practice!

# While loops

    # Loop as long as a condition is true
    # Need to make sure you don’t enter an infinite loop
 
# For loops 

    # Can loop over ranges of numbers
    # Can loop over elements of a string
    # Will soon see many other things are easy to loop over
    
    










    


















    
    
    
    




















        







 
  
  
  
  
  


    
    
    
























  
    
    
    
    
    
    

    
    






   










  

    
    
    
    
    
















































    





  
    
    
    
    
    
    
    
    
    
    

    