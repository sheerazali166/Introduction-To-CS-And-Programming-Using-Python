#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 18:09:23 2024

@author: sheeraz
"""

def sum_digits(s):

    """ s is a non-empty string containing digits.
      Returns sum of all chars that are digits """
      
    total = 0
    
    for char in s:
        
        if char in "0123456789":
            
            val = int(char)
            
            total += val
            
    return total       
      
    
      
print(sum_digits("11223"))

print(sum_digits("11223 kinza"))



# CODE WITH EXCEPTIONS

def sum_digits(s):
    
    """ s is a non-empty string containing digits.
       Returns sum of all chars that are digits """ 
       
    total = 0
    
    for char in s:
        
        try:
      # ----
            val = int(char)
          # ---------------
          # Problematic if try to do int(a)
           
            total += val
            
        except:
      # -------
            print("can't convert", char)
         #  ----------------------------
         #  Print and move on to next char
         
        return total 
    
    
    
print(sum_digits("11223"))

print(sum_digits("kinza"))


# a = int(input("Tell me one number"))

# b = int(input("Tell me another number:"))

# print(a / b) 


# Use try/except around the problematic code

# try:
    
    # a = int(input("Tell me one number:"))
    # b = int(input("Tell me another number:"))
    
    # print(a / b)
    
# except:

    # print("Bug in user input.")
    
    

# HANDLING SPECIFIC EXCEPTIONS

# Have separate exceptclauses to deal with a particular type of exception

# try:
    
    # a = int(input("Tell me one number: "))
    # b = int(input("Tell me another number: "))

    # print("a/b = ", a / b)   
    
    # print("a+b = ", a + b)
    
# except ValueError:
# ---------------
# only execute if these errors come up

    # print("Could not convert to a number")
    
# except ZeroDivisionError:
# -----------------------

    # print("Can't dvde by zero ") 
    # print("a/b = infinity")
    # print("a+b =", a + b)


# except:
# -----
# for all other errors

    # print("Something went very wrong.")    



# Execution stopping means a bad result is not propagated

def sum_digits(s):
    
    """ s is a non-empty string containing digits.
        Returns sum of all chars that are digits """
        
    total = 0

    for char in s:
        
        try:
            
            val = int(char)
            total += val
            
        except:
            
            raise ValueError("string contained a character")
          # ------------------------------------------------
          # Halt execution as soon as you see a non-digit with
          # our own informative message. Does not go on to next
          # char!
          
          
    return total



    
print(sum_digits("11223"))

# print(sum_digits("211kinza"))



# YOU TRY IT!
 
def pairwise_div(Lnum, Ldenom):
    
    """ Lnum and Ldenom are non-empty lists of equal lengths containing
        numbers Returns a new list whose elements are the pairwise division
        of an element in Lnum by an element in Ldenom. Raise a ValueError if
        Ldenom contains 0. """
   
        
    result = []
   
    try:
        
        listSize = len(Lnum)
        
        for i in range(listSize):
        
            result.append(Lnum[i] / Ldenom[i])
       
    except ZeroDivisionError:
       
        raise ZeroDivisionError("Can't divide by zero")
        
    
    return result



# For example:

L1 = [4, 5, 6]

L2 = [1, 2, 3]

print(pairwise_div(L1, L2))  # prints [4.0,2.5,2.0]



L1 = [4, 5, 6]

L2 = [1, 0, 3]


# print(pairwise_div(L1, L2))


# Execution stopping means a bad result is not propagated

def sum_digits(s):
    
    """ s is a non-empty string containing digits.
        Returns sum of all chars that are digits """
        
    assert len(s) != 0, "s is empty"    
  # --------------------------------
  # Halt execution when specification is not met
  
    total = 0
    
    for char in s:
        
        try:
            
            val = int(char)
            
            total += val
            
        except:
             
            raise ValueError("string contained a character")




sum_digits("11223")

# sum_digits("211kinza")

# sum_digits("")


test_grades = [[["peter", "parker"], [80.0, 70.0, 85.0]],
                       ["bruce", "wayne"], [100.0, 80.0, 74.0]]
             # -----------------------------------------------
             # Two students, each with a name list and a grades list
             
             
print(test_grades)



def get_stats(class_list):

    new_stats = []

    for stu in class_list:
      # ---
      # elt is for example:
      # [["peter", "parker"], [80.0, 70.0, 85.0]] 

        new_stats.append([stu[0], stu[1], avg(stu[1])])
                       # -------  ------  --- ------
     
    return new_stats


def avg(grades):
  # ---  
    
    return sum(grades) / len(grades)



        
        



test_grades = [[['peter', 'parker'], [80.0, 70.0, 85.0], 78.33333], [['bruce', 'wayne'], [100.0, 80.0, 74.0], 84.666667]]


print(get_stats(test_grades))


def get_stats(class_list):

    new_stats = []

    for stu in class_list:
      # ---
      # elt is for example:
      # [["peter", "parker"], [80.0, 70.0, 85.0]] 

        new_stats.append([stu[0], stu[1], avg(stu[1])])
                       # -------  ------  --- ------
     
    return new_stats


def avg(grades):

    try:

        return sum(grades) / len(grades)

    except ZeroDivisionError:
        
        print("warning: no grades data")


print("---------------------------------")



test_grades = [[['peter', 'parker'], [10.0, 55.0, 85.0], 50.0],
    [['bruce', 'wayne'], [10.0, 80.0, 75.0], 55.0],
    [['captain', 'america'], [80.0, 10.0, 96.0], 62.0],
    [['deadpool'], [], None]]


for grade in get_stats(test_grades):
    print(grade)
   

def get_stats(class_list):

    new_stats = []

    for stu in class_list:
      # ---
      # elt is for example:
      # [["peter", "parker"], [80.0, 70.0, 85.0]] 

        new_stats.append([stu[0], stu[1], avg(stu[1])])
                       # -------  ------  --- ------
     
    return new_stats



def avg(grades):
    
    try:
        
        return sum(grades) / len(grades)
    
    except ZeroDivisionError:
        
        print("warning: no grades data")
        
        return 0.0



print("---------------------------------")


test_grades = [[['peter', 'parker'], [10.0, 55.0, 85.0], 50.0],
                [['bruce', 'wayne'], [10.0, 80.0, 75.0], 55.0],
                [['captain', 'america'], [80.0, 10.0, 96.0], 62],
                [['deadpool'], [], 0.0]]
    
   
for grade in get_stats(test_grades):
    print(grade)    
   
   
def get_stats(class_list):

    new_stats = []

    for stu in class_list:
      # ---
      # elt is for example:
      # [["peter", "parker"], [80.0, 70.0, 85.0]] 

        new_stats.append([stu[0], stu[1], avg(stu[1])])
                       # -------  ------  --- ------
     
    return new_stats   



def avg(grades):
    assert len(grades) != 0, 'no grades data'
    return sum(grades)/len(grades)


print("---------------------------------")


test_grades = [[['peter', 'parker'], [10.0, 55.0, 85.0], 50.0],
               [['bruce', 'wayne'], [10.0, 80.0, 75.0], 55.0],
               [['captain', 'america'], [80.0, 10.0, 96.0], 62],
               [['deadpool'], [], 0.0]]
    


   
for grade in get_stats(test_grades):
    print(grade) 







             











    