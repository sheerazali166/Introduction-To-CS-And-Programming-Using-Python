#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 13:45:04 2024

@author: sheeraz
"""

# Program 1

type(5) # what you write into the python shell

type(3.0) # what you shows after hitting  enter

# what are trying to say or prove i am wrong

# offcourse get adjustement problem solved 


# YOU TRY IT!
 
# In your console, find the type of:
    
type(1234)

type(8.99)

type(9.0)

type(True)

type(False)


# TYPE CONVERSIONS (CASTING)

# Can convert object of one type to another

float(3) # casts the int 3to float 3.0

int(3.9) # casts (note the truncation!) the float 3.9to int 3

# Some operations perform implicit casts

round(3.9) # returns the int 4

# YOU TRY IT!

# In your console, find the type of:
    
float(123)
round(7.9)

float(round(7.2))

int(7.2)
int(7.9)


# EXPRESSIONS

# Combine objects and operators to form expressions

3 + 2
5 / 3



# An expression has a value, which has a type

# 3+2 has value 5 and type int

type(3 + 2)

# 5/3 has value 1.666667 and type float

type(5 / 3)

# Python evaluates expressions and stores the value. It doesn’t
# store expressions!

# Syntax for a simple expression

# <object> <operator> <object>


# BIG IDEA

# Replace complex
# expressions by ONE value

# Work systematically to evaluate the expression.


# EXAMPLES

3 + 2

(4 + 2) * 6 - 1 # Do computation left to right - like the math!

type((4 + 2) * 6-1) # Do computation inside parents first, left to right

float((4 + 2) * 6 - 1) # Take care about what operations you are doing


# YOU TRY IT!

#  In your console, find the values of the following expressions:
    
(13 - 4) / (12 * 12)

type(3 * 4)

type(4.0 * 3)

type(1 / 2)


# YOU TRY IT!

# Which of these are allowed in Python? Type them in the
# console to check.

x = 6

# 6 = x

# SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?

# x * y = 3 + 4

# SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?

xy = 3 + 4



# ABSTRACTING EXPRESSIONS

# Why give names to values of expressions?

    # To reuse names instead of values
    # Makes code easier to read and modify
    
    
# Choose variable names wisely

    # Code needs to read
    # Today, tomorrow, next year
    # By you and others
    # You’ll be fine if you stick to letters,
    # underscores, don’t start with a number


# Compute approximate value for pi

# comments start with a # and are not part of code
# executed used to tell others what your code s doing 


pi = 355 / 113
radius = 2.2

area = pi * (radius ** 2)
circumference = pi * (radius  * 2)

# an assignment expression on right variable name on left


# WHAT IS BEST CODE STYLE?

# do calculations


# meh

a = 355 / 113 * (2.2 ** 2) 
c = 355 / 113 * (2.2 * 2)


# ok

p = 355 / 113
r = 2.2

# multiply p with r squared
a = p * (r ** 2)

# multiply p with r times 2
c = p * (r * 2)

# best

# calculate area and circumference of a circle
# using an approximation 

pi = 355 / 113
radius = 2.2

area = pi * (radius ** 2)
circumference = pi * (radius * 2)


# r ? tax tenson or pansion with poison


# CHANGE BINDINGS

# Can re-bind variable names using new assignment statements
# Previous value may still stored in memory but lost the handle for it
# Value for area does not change until you tell the computer to do the calculation again

pi = 3.14
radius = 2.2
area = pi * (radius ** 2)
radius = radius + 1


# YOU TRY IT!

# These 3 lines are executed in order. What are the values of
# metersand feetvariables at each line in the code?


meters = 100

feet = 3.2808 * meters

meters = 200

# YOU TRY IT!

# Swap values of x and y without binding the numbers directly.
# Debug (aka fix) this code.

x = 1
y = 2

temp = x
x = y
y = temp

# Python Tutor to the rescue?


# SUMMARY

# Objects

# Objects in memory have types.
# Types tell Python what operations you can do with the objects.
# Expressions evaluate to one value and involve objects and operations.
# Variables bind names to objects.
# = sign is an assignment, for ex. var = type(5*4)
var = type(5*4)


# Programs

# Programs only do what you tell them to do.
# Lines of code are executed in order.
# Good variable names and comments help you read code later.









































































 


  





    









    



















































































    
    





 
   


    