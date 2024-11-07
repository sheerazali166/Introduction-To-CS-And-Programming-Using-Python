#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 22:00:26 2024

@author: sheeraz
"""

# STRINGS, INPUT/OUTPUT, and BRANCHING

# RECAP

pi = 3.14
radius = 2.2

area = pi * (radius ** 2)

print(area)

radius = radius + 1 

area = pi * (radius ** 2)


print(area)

print(54 - 17)
print(54 + 17)

# nothing is free

var = type(5 * 4)
print(var)

# Objects

# Objects in memory have types.
# Types tell Python what operations you can do with the objects.
# Expressions evaluate to one value and involve objects and operations.
# Variables bind names to objects.
# = sign is an assignment, for ex. var = type(5*4)


# Programs

# Programs only do what you tell them to do.
# Lines of code are executed in order.
# Good variable names and comments help you read code later.

# STRINGS

# STRINGS

# Think of a stras a sequence of case sensitive characters

# Letters, special characters, spaces, digits

# Enclose in quotation marks or single quotes

# Just be consistent about the quotes

a = "me"

z = "you"

# Concatenate and repeat strings

b = "myself"
c = a + b
d = a + " " + b
silly = a * 3


# YOU TRY IT!

# What’s the value of s1 and s2?

b = ":"
c = ")"
s1 = b + 2 * c

f = "a"
g = " b"
h = "3"
s2 = (f + g) * int(h)



# STRING OPERATIONS

# len()is a function used to retrieve the length of a string in the
# parentheses

# STRING OPERATIONS

# len()is a function used to retrieve the length of a string in the
# parentheses

s = "abc"

len(s) # --> evaluates to 3

chars = len(s)
      # -----
      
# Expresson that evaluates to 3

# SLICING to get ONE CHARACTER IN A STRING 

# Square brackets used to perform indexing into a string to get the value at
# a certain index/position

s = "abc" 

# index: 0 1 2 <-- indexing always starts at 0
# index: -3 -2 -1 <-- index of last element is len(s) - 1 or -1

s[0] # --> evaluates to "a"
s[1] # --> evalutes to "b"
s[2] # --> evaluates to "c"
s[3] # --> trying to index out of bounds, error

s[-1] # --> evaluates to "c"
s[-2] # --> evaluates to "b"
s[-3] # --> evaluates to "a"

# SLICING to get a SUBSTRING

# Can slice strings using [start:stop:step]

# Get characters at start up to and including stop-1 taking every step
# characters

# This is confusing as you are starting out :( can't go wrong with
# explicitly giving start, stop, end every time


# If give two numbers, [start:stop], step=1by default
# If give one number, you are back to indexing for the character at one
# location (prev slide)

# You can also omit numbers and leave just colons (try this out!)

# SLICING EXAMPLES

# Can slice strings using [start:stop:step]

# Look at step first. +ve means go left-to-right -ve means go right-to-left

         # <---> 
#   s = "abcdefgh"
# index: 01234567

# s = "abcdefgh"
       # ----

# index: 0 1 2 3 4 5 6 7
# index:-8-7-6-5-4-3-2-1 

# If unsure what some command does, try it out in your console!

s = "abcdefgh"

s[3:6] # --> evaluates to "def" same as s[3:6:1]

s[3:6:2] # --> evaluates to "df" 

s[:] # --> evaluates to "abcdefgh", same as s[0:len(s):1]

s[::-1] # --> evaluates to "fgfedcba"

s[4:1:-2] # --> evaluates to ec 

# YOU TRY IT!

s = "ABC d3f ghi"

s[3:len(s) -1]
s[4:0:-1]
s[6:3]


# IMMUTABLE STRINGS

# Strings are “immutable” – cannot be modified

# You can create new objects that are versions of the original one

# Variable name can only be bound to one object

s = "car"

s[0] = "b" # --> gives an error 

s = "b" + s[1: len(s)] # --> is allowed s bound to new object





#
#######  ----❌----> Car 
## s ##
####### -----------> Bar


# BIG IDEA

# If you are wondering “what happens if”…
# Just try it out in the console!


# INPUT/OUTPUT

# PRINTING

# Used to output stuff to console

3 + 2

# 5

# "Out" tells you it's an interacton wthin the shell only 

# Command is print

print(3 + 2)

# No "Out" means it is actually shown to a user, apparant when you edt/run
# files

# Printing many objects in the same command

    # Separate objects using commas to output them separated by spaces
    
    # Concatenate strings together using + to print as single object
    

a = "the"

b = 3

c = "musketeers"

print(a, b, c)

print(a + str(b) + c)
        # -----
        
# Every piece being concatenated must be a string

# INPUT

x = input(s)         


    # Prints the value of the string s
    
    # User types in something and hits enter
    
    # That value is assigned to the variable x


# Binds that value to a variable

text = input("Type anything: ")
print(5 * text)



        #################################################
        #                                               #     
        #   shell                                       #
        #                                               #  
        #                                               #  
        #       Type anything:                          #
        #                                               #
        #                                               #
        #                                               #
        #                                               # 
        #                       And wat for characters  #
        #                       and Enter to be hit     #
        #                                               #
        #                                               #
        #################################################



# INPUT

x = input(s)

# Prints the value of the string s

# User types in something and hits enter

# That value is assigned to the variable x

# Binds that value to a variable

text = input("Type anythng: ")
     # ----------------------
             # howdy
             
print(5 * text)


        #################################################
        #                                               #     
        #   shell                                       #
        #                                               #  
        #                                               #  
        #       Type anything: howdy                    #
        #                      -----                    #
        #                                               #
        #                                               #
        #                                               # 
        #                                               #
        #                                               #
        #                                               #
        #                                               #
        #################################################



# INPUT


x = input(s)

    # Prints the value of the string s
    # User types in something and hits enter
    # That value is assigned to the variable x

# Binds that value to a variable

text = input("Type anything: ")
print(5 * text)


        #################################################
        #                                               #     
        #   shell                                       #
        #                                               #  
        #                      |-------|                #  
        #       Type anything: | howdy |                #
        #                      |-------|                #
        #                                               #
        #                                               #
        #                                               # 
        #                                               #
        #                                               #
        #                                               #
        #                                               #
        #################################################





                #############
                ## "howdy" ##
                #############
                
    
                
# INPUT

x = input(s)

    # Prints the value of the string s
    # User types in something and hits enter
    # That value is assigned to the variable x
    
# Binds that value to a variable

text = input("Type anything: ")
print(5 * text)



        #################################################
        #                                               #     
        #   shell                                       #
        #                                               #  
        #                                               #  
        #       Type anything: howdy                    #
        #                                               #
        #                                               #
        #                                               #
        #                                               # 
        #                                               #
        #                                               #
        #                                               #
        #                                               #
        #################################################




          #############             #############
          ##  text   ##  ------->   ## "howdy" ##
          #############             #############




# INPUT

x = input(s)

    # Prints the value of the string s
    # User types in something and hits enter
    # That value is assigned to the variable x
    
# Binds that value to a variable

text = input("Type anythnig: ")

print(5 * text)
# -------------



        #################################################
        #                                               #     
        #   shell                                       #
        #                                               #  
        #                                               #  
        #       Type anything: howdy                    #
        #                                               #
        #   howdyhowdyhowdyhowdyhowdy                   #
        #                                               #
        #                                               # 
        #                                               #
        #                                               #
        #                                               #
        #                                               #
        #################################################




          #############             #############
          ##  text   ##  ------->   ## "howdy" ##
          #############             #############



# INPUT

# input always returns an str, must cast if working with numbers

num1 = input("Type a number: ") # "3"
     # ----------------------- 
     
print(5 * num1)

num2 = int(input("Type a number: "))

print(5 * num2)



        #################################################
        #                                               #     
        #   shell                                       #
        #                                               #  
        #                                               #  
        #       Type a number: 3                        #
        #                                               #
        #                                               #
        #                                               #
        #                                               # 
        #                                               #
        #                                               #
        #                                               #
        #                                               #
        #################################################




          #############             #############
          ## "num1"  ##  ------->   ##    3    ##
          #############             #############



# INPUT

# input always returns an str, must cast if working with numbers

num1 = input("Type a number: ")

print(5 * num1)
# ------------

num2 = int(input("Type a number: "))

print(5 * num2)



        #################################################
        #                                               #     
        #   shell                                       #
        #                                               #  
        #                                               #  
        #       Type a number: 3                        #
        #                                               #
        #       33333                                   #
        #                                               #
        #                                               # 
        #                                               #
        #                                               #
        #                                               #
        #                                               #
        #################################################




          #############             #############
          ##  num1   ##  ------->   ##   "3"   ##
          #############             #############
          
          
 
# INPUT

# input always returns an str, must cast if working with numbers

num1 = input("Type a number: ")

print(5 * num1)

num2 = int(input("Type a number: ")) # "3"
        # -------------------------
        
print(5 * num2)   



        #################################################
        #                                               #     
        #   shell                                       #
        #                                               #  
        #                                               #  
        #       Type a number: 3                        #
        #                                               #
        #       33333                                   #
        #                                               #
        #       Type a number: 3                        # 
        #                                               #
        #                                               #
        #                                               #
        #                                               #
        #################################################
        




          #############             #############
          ##  num1   ##  ------->   ##   "3"   ##
          #############             #############
                   


# INPUT

# input always returns an str, must cast if working with numbers

num1 = input("Type a number: ")

print(5 * num1)

num2 = int(input("type a number: "))

print(5 * num2)



        #################################################
        #                                               #     
        #   shell                                       #
        #                                               #  
        #                                               #  
        #       Type a number: 3                        #
        #                                               #
        #       33333                                   #
        #                                               #
        #       Type a number: 3                        # 
        #                                               #
        #                                               #
        #                                               #
        #                                               #
        #################################################
        




          #############             #############
          ##  num1   ##  ------->   ##   "3"   ##
          #############             #############
          
          
          
          #############             #############
          ##  num2   ##  ------->   ##    3    ##
          #############             #############
                  
    


# INPUT

# input always returns an str, must cast if working with numbers

num1 = input("Type a number: ")
print(5 * num1)

num2 = int(input("Type a number: "))
print(5 * num2)
# -------------



        #################################################
        #                                               #     
        #   shell                                       #
        #                                               #  
        #                                               #  
        #       Type a number: 3                        #
        #                                               #
        #       33333                                   #
        #                                               #
        #       Type a number: 3                        # 
        #                                               #
        #       15                                      #
        #                                               #
        #                                               #
        #################################################
        




          #############             #############
          ##  num1   ##  ------->   ##   "3"   ##
          #############             #############
          
          
          
          #############             #############
          ##  num2   ##  ------->   ##    3    ##
          #############             #############


         
# YOU TRY IT!

# Write a program that

    # Asks the user for a verb
    # Prints “I can _ better than you” where you replace _ with the verb.
    # Then prints the verb 5 times in a row separated by spaces.
    # For example, if the user enters run, you print:
        
        # I can run better than you!
        # run run run run run
        
x = input("Input: ")


print(f"{x * 5} ")


# AN IMPORTANT ALGORITHM: NEWTON’S METHOD

# Finds roots of a polynomial

# E.g., find g such that f(g, x) = g^3 – x = 0

# Algorithm uses successive approximation

# next_guess = guess  - (f(𝑔uess) / f'(𝑔uess))

# Partial code of algorithm that gets input and finds next guess

# Try Newton Raphson for cube root

x = int(input("What x to find the cube root of? "))
g = int(input("What guess to start with? "))

print("Current estimate cubed = ", g ** 3)

next_g = g - ((g ** 3) / (3 * g ** 2))
            # -------    -----------
            #   f(g)        f'(g)
            
print("Next guess to try = ", next_g)            


# F-STRINGS

# Available starting with Python 3.6

# Character f followed by a formatted string literal
                          # ------------------------ 

    # Anything that can be appear in a normal string literal
    # Expressions bracketed by curly braces { }
    
    
# Expressions in curly braces evaluated at runtime, automatically converted
# to strings, and concatenated to the string preceding them

num = 3000

fraction = 1 / 3

print(num * fraction, "is", fraction * 100, "% f", num)
                                        # -
                                        # Introduces an extra space 

print(num * fraction, "is", str(fraction * 100) + "% of", num)
print(f"{num * fraction} is {fraction * 100}% of {num}")
      # ---------------     ---------------      -----
        # expression
        
        

print(f"{(num * fraction) * 100} is {(fraction * 100) * 100}% of {(num) * 100}")

# 100000.0 is 3333.333333333333% of 300000
# balidan to direct bangali daan

 
# BIG IDEA


# Expressions can be placed anywhere.

# Python evaluates them!

# CONDITIONS for BRANCHING

# BINDING VARIABLES and VALUES


# In CS, there are two notions of equal

    # Assignment and Equality test
    
    
# variable = value

    # Change the stored value of variable to value
    # Nothing for us to solve, computer just does the action
    

# some_expression == other_expression

    # A test for equality
    # No binding is happening
    # Expressions are replaced by values and computer just does
    # the comparison


# Replaces the entire line with Trueor False


# COMPARISON OPERATORS

# i and j are variable names

    # They can be of type ints, float, strings, etc.
    
    
# Comparisons below evaluate to the type Boolean

    # The Boolean type only has 2 values: Trueand False
    
    
# i > j
# i >= j
# i < j
# i <= j

# With strings, be careful about case senstivity 

# "March" != "march"

# i == i  --> equality test, Truei f i is the same as j
# i != j --> inequality test, True if i is the same as j


# LOGICAL OPERATORS on bool

# aand bare variable names (with Boolean values)

# not a --> True if a is False
          # False if a is True 
          
# a and b --> True if both are True

# a or b --> Trueif either or both are True


    ##########################################################
    #     A     #     B     #     A and B    #     A or B    #         
    ##########################################################
    #           #           #                #               #
    #   True    #    True   #      True      #     True      #
    #           #           #                #               #
    ##########################################################
    #           #           #                #               #
    #   True    #   False   #      False     #     True      #
    #           #           #                #               #
    ##########################################################
    #           #           #                #               #
    #   False   #    True   #      False     #     True      #
    #           #           #                #               #
    ##########################################################
    #           #           #                #               #
    #   False   #   False   #      False     #     False     #
    #           #           #                #               #
    ##########################################################
    
    
    
# COMPARISON EXAMPLE 

pset_time = 15
sleep_time = 8

print(sleep_time > pset_time)
# ---------------------------
 # Prints the boolean false

derive = True
drink = False

both = drink and derive

print(both)
# --------
# Prints the boolean false

# YOU TRY IT!

#  Write a program that

    # Saves a secret number in a variable.
    # Asks the user for a number guess.
    # Prints a bool Falseor Truedepending on whether the guess matches the
    # secret.
    
    
    
# WHY bool?

# When we get to flow of control, i.e. branching to different expressions
# based on values, we need a way of knowing if a condition is true 

# E.g., if something is true, do this, otherwise do that
         # -----------------  -------  -----------------
              # Boolean        Some       Some other  
                            #  commands    commands
                            

# <condition> has a value True or False
# Indentation matters in Python!
# Do code within if block if condition is True


# BRANCHING IN PYTHON

# <condition> has a value True or False

# Indentation matters in Python!

# Do code within if block when condition is Trueor code within else block
# when condition is False

# BRANCHING EXAMPLE

# pset_time = ???
# sleep_time = ???


# if (pset_time + sleep_time) > 24:
    # -----------------------------
    # Condition that evaluates to a boolean
    
      # print("impossible!")
      # --------------------
      # This indented code executed if line above is True    
      
# elif (pset_time + sleep_time) >= 24:
    #  ------------------------------
      # This indented code executed
    
    
      # print("full schedule!")
      # -----------------------
      # if line above is True and the if condition is False 
      
# else:
# This else block runs only      
    
      # leftover = abs(24-pset_time-sleep_time)
      # ---------------------------------------
      
      # print(leftover,"h of free time!")
      # ---------------------------------
      # if previous conditions were all false 
      
      
# print("end of day")


# YOU TRY IT!

# Semantic structure matches visual structure
# Fix this buggy code (hint, it has bad indentation)!

x = int(input("Enter a number for x: "))
y = int(input("Enter a different number for y: ")) # this is bug

if x == y:
    # print(x, "is the same as", y)
    print(f"{x} is the same as {y}")

print("These are equals")

x = int(input("Enter a number for x: "))
y = int(input("Enter a different number for y: ")) # this is bug

if x == y:
    print(f"{x} is the same as {y}")

print("These are equals")

x = int(input("Enter a number for x: "))
y = int(input("Enter a different number for y: ")) # this is bug

if x == y:
    print(f"{x} is the same as {y}")
else:
    print("These not are equals")
    
# please don't hire illigal puppies who mislead people and take job 
# at other's credit     


# INDENTATION and NESTED BRANCHING

# Matters in Python

# How you denote blocks of code

x = float(input("Enter a number for x: "))   #     5        5        0

y = float(input("Enter a number for y: "))   #     5        0        0

if x == y:                                   #    True    False    False
                    
     print("x and y are equal")              #    <--               <--
     
     
elif y != 0:                                 #    True              False

    print("therefor, x / y is", x / y)       #    <--
    
    
elif y  < x:                                 #            False
    
    print("x is smaller")

else:                                         
    
    print("y is smaller")                    #             <-- 
    
print("thanks")                              #    <--      <--       <--        
    
    
    
    
# BIG IDEA

# Practice will help you build a mental model of how to trace the code

# Indentation does a lot of the work for you!


# YOU TRY IT!

# What does this code print with

y = 2

y = 20

y = 11


# What if if x <= y:becomes elif x <= y: ?

answer = ""
x = 11

if x == y:
    answer = answer + "M"
if x >= y:
    answer = answer + "i"
else:
    answer = answer + "T"

print(answer)


# YOU TRY IT!

# Write a program that

# Saves a secret number.

# Asks the user for a number guess.

# Prints whether the guess is too low, too high, or the same as the secret.

# BIG IDEA

# Debug early, debug often.

# Write a little and test a little.

# Don’t write a complete program at once. It introduces too many errors.

# Use the Python Tutor to step through code when you see something unexpected!

# SUMMARY

# Strings provide a new data type

    # They are sequences of characters, the first one at index 0
    # They can be indexed and sliced

# Input

    # Done with the inputcommand
    # Anything the user inputs is read as a string object!
    
# Output

    # Is done with the printcommand
    # Only objects that are printed in a .py code file will be visible in
    # the shell
    
# Branching

    # Programs execute code blocks when conditions are true
    # In an if-elif-elif…structure, the first condition that is True will
    # be executed

    # Indentation matters in Python!
    
