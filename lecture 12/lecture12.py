#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 02:24:10 2024

@author: sheeraz
"""

# LIST COMPREHENSION, FUNCTIONS AS OBJECTS,TESTING, DEBUGGING

# LIST COMPREHENSIONS

# LIST COMPREHENSIONS

# Applying a function to every element of a sequence, then creating a new
# list with these values is a common concept


# Example:
    
def f(L):

    Lnew = []
  # ---------
  # New List

    for e in L:
        
        Lnew.append(e ** 2)


# Python provides a concise one-liner way to do this, called a list
# comprehension
   
    # Creates a new list  
    
    # Applies a function to every element of another iterable
    
    # Optional, only apply to elements that satisfy a test 
    
    
# [expression for elem in iterable if test]

# LIST COMPREHENSIONS

# Create a new list, by applying a function to every element of another
# iterable that satisfies a test



#                                           #                                           #
#                                           #                  New List                 #
#  def f(L):                                #                    |  |                   #
#                                           #                    |  |                   #
#      Lnew = []                            #           ----------   ------------       #
#      --------                             #          |                        |       # 
#      New list                             #          ▼                        ▼       #
#                                           #           --------   -------------        #                
#      for e in L:                          #  Lnew = [| e ** 2 | | for e in L |]       #
#      -----------                          #          ---------  -------------         #
#      Look at every element                #                                           #   
#                                           #                                           #          
#      Lnew.append(e ** 2)                  #                                           #
#                 --------                  #                                           #
#                 Function to apply         #                                           #
#                                           #                                           #     
#      return Lnew                          #                                           #
#                                           #                                           #
#                                           #                                           #


def f(L):
    
    Lnew = []
    
    for e in L:
        
        Lnew.append(e ** 2)
        
    return Lnew


L = [10, 20, 30, 40, 50]


print(f(L))

Lnew = [e ** 2 for e in L]

print(Lnew)


# LIST COMPREHENSIONS

# Create a new list, by applying a function to every element of another
# iterable that satisfies a test


#                                          #                                          # 
#                                          #                                          #
#  def f(L):                               #                                          #                         
#                                          #                                          #
#      Lnew = []                           #                                          #
#                                          #                                          #
#      for e in L:                         #                                          #
#                                          #  Lnew = [e ** 2 for e in L]              #    
#          Lnew.append(e ** 2)             #                                          #
#                                          #                                          #
#      return Lnew                         #                                          #
#                                          #                                          #                                   
#                                          #                                          #
#                                          #                                          #
#  def f(L):                               #                                          #
#     ------------                         #                                          # 
#    | Lnew = [] |                         #                                          #
#    -------------                         #                                          #
#      New List                            #                                          #
#                                          #                                          #   
#    for e in L:                           #                                          #
#                                          #                                          #
#       -----------------                  #                                          #
#      | if e % 2 == 0: |                  #                                          #
#      -----------------                   #                                          #
#      Function to apply only test         #                                          # 
#      is True                             #                                          #
#                       ---------          #                                          #
#          Lnew.append(| e ** 2 |)         #                                          #
#                       --------           #                                          #
#                                          #                                          #
#    return Lnew                           #                                          #
#                                          #                                          #
#                                          #                                          #



def f(L):
    
    Lnew = []
    
    for e in L:
            
        Lnew.append(e ** 2)
            
    return Lnew


L = [1, 2, 3, 4, 5, 6]

print(f(L))

def f(L):
    
    Lnew = []
    
    for e in L:
        
        if e % 2 == 0:
            
            Lnew.append(e ** 2)
            
            
    return Lnew
   

L = [1, 2, 3, 4, 5, 6]

print(f(L))

Lnew = [e ** 2 for e in L]

print(Lnew)


# LIST COMPREHENSIONS

# Create a new list, by applying a function to every element of another
# iterable that satisfies a test



#                                     #                                              #
#                                     #                                              #
#    def f(L):                        #    Lnew = [e ** 2 for e in L]                #
#                                     #                                              #
#        Lnew = []                    #                                              #
#                                     #                                              #
#    for e in L:                      #                                              #
#                                     #                                              #   
#        Lnew.append(e ** 2)          #                                              #
#                                     #                                              #
#    return Lnew                      #                                              # 
#                                     #                                              #
#                                     #                                              #
#                                     #                                              #
#    def f(L):                        #                                              #
#                                     #                  New list                    #
#   ------------                      #                  |     |                     #
#  | Lnew = [] |                      #                  |     |                     #
#  -------------                      #            -------     -------------------   #
#                                     #           |                              |   #
#   for e in L:                       #           |                              |   # 
#                                     #           |                              |   #
#      if e % 2 == 0:                 #           |                              |   #
#                                     #           |                              |   #
#          Lnew.append(e ** 2)        #           ▼                              ▼    #
#                                     #    Lnew = [e ** 2 for e in L if e % 2 == 0]  #              
#  return Lnew                        #                                              #
#                                     #                                              #
#                                     #                                              #


def f(L):
    
    Lnew = []
    
    for e in L:
        
        Lnew.append(e ** 2)

    return Lnew



L = [1, 2, 3, 4, 5, 6]

print(f(L))


def f(L):
    
    Lnew = []
    
    for e in L:
        
        if e % 2 == 0:
            
            Lnew.append(e ** 2)
            
    return Lnew


L = [1, 2, 3, 4, 5, 6]

print(f(L))

  
Lnew = [e ** 2 for e in L]

print(Lnew)

Lnew = [e ** 2 for e in L if e % 2 == 0]

print(Lnew)


# LIST COMPREHENSIONS

# Create a new list, by applying a function to every element of another
# iterable that satisfies a test
     

#                                         #                                                      #    
#                                         #                                                      #  
#    def f(L):                            #    Lnew = [e ** 2 for e in L]                        #  
#                                         #                                                      # 
#        Lnew = []                        #                                                      # 
#                                         #                                                      #   
#    for e in L:                          #                                                      # 
#                                         #                                                      # 
#        Lnew.append(e ** 2)              #                                                      # 
#                                         #                                                      # 
#    return Lnew                          #                                                      #                          
#                                         #                                                      # 
#                                         #                                                      # 
#                                         #                                                      # 
#    def f(L):                            #                                                      # 
#                                         #                                                      # 
#        Lnew = []                        #                                                      # 
#                                         #                                                      # 
#   --------------                        #                                                      #    
#  | for e in L: |                        #                                                      # 
#   --------------                        #                                                      # 
#    Loop over elements                   #                                                      # 
#                                         #                                                      # 
#        if e % 2 == 0:                   #                                                      # 
#                                         #                    -------------                     # 
#            Lnew.append(e ** 2)          #    Lnew = [e ** 2 | for e in L | if e % 2 == 0  ]    # 
#                                         #                   --------------                     # 
#    return Lnew                          #                                                      # 
#                                         #                                                      # 
#                                         #                                                      # 


# LIST COMPREHENSIONS

# Create a new list, by applying a function to every element of another
# iterable that satisfies a test




#                                         #                                                      #    
#                                         #                                                      #  
#    def f(L):                            #    Lnew = [e ** 2 for e in L]                        #  
#                                         #                                                      # 
#        Lnew = []                        #                                                      # 
#                                         #                                                      #   
#    for e in L:                          #                                                      # 
#                                         #                                                      # 
#        Lnew.append(e ** 2)              #                                                      # 
#                                         #                                                      # 
#    return Lnew                          #                                                      #                          
#                                         #                                                      # 
#                                         #                                                      # 
#                                         #                                                      # 
#    def f(L):                            #                                                      # 
#                                         #                                                      # 
#        Lnew = []                        #                                                      # 
#                                         #                                                      # 
#                                         #                                                      #    
#    for e in L:                          #                                                      # 
#                                         #                                                      # 
#    Loop over elements                   #                                                      # 
#       -----------------                 #                                                      # 
#      | if e % 2 == 0: |                 # 
#      -----------------                  # 
#        Function to apply                #  
#        only if test is true             # 
#                                         #                    -------------                     # 
#                         ---------       #    Lnew = [e ** 2 | for e in L | if e % 2 == 0  ]    # 
#            Lnew.append(| e ** 2 |)      #                   --------------                     # 
#                        ---------        #                                                      # 
#                                         #                                                      # 
#                                         #                                                      # 
#        return Lnew                      #
#                                         #
#                                         #




# LIST COMPREHENSIONS

# [expression for elem in iterable if test]

def f(expr, old_list, test = lambda x: True):
    
    new_list = []
    
    for e in old_list:
        
        if test(e):
            
            new_list.append(expr(e))
            
            
    return new_list



print([e ** 2 for e in range(6)])  #  --> [0, 1, 4, 9, 16, 25]

print([e ** 2 for e in range(8) if e % 2 == 0])  #  --> [0, 4, 16, 36]

print([[e, e ** 2] for e in range(4) if e % 2 != 0]) # --> [[1,1], [3,9]]
  

# YOU TRY IT!

# What is the value returned by this expression?

# Step1: what are all values in the sequence

# Step2: which subset of values does the condition filter out?

# Step3: apply the function to those values

print([len(x) for x in ["xy", "abcd", 7, "4.0"] if type(x) == str])


# FUNCTIONS: DEFAULT PARAMETERS


# SQUARE ROOT with BISECTION

def bisection_root(x):
    
    epsilon = 0.01
    
    low = 0
    
    high = x
    
    guess = (high + low) / 2.0
    
    while abs(guess ** 2 - x) >= epsilon:
        
        if guess ** 2 < x:
            
            low = guess
            
        else:
            
            high = guess
            
        guess = (high + low) / 2.0
        
    return guess  


print(bisection_root(123))


# ANOTHER PARAMETER

# Motivation: want a more accurate answer

# def bisection_root(x)can be improved

# Options?

# Change epsilon inside function (all function calls are affected)

# Use an epsilon outside function (global variables are bad)

# Add epsilon as an argument to the function


# epsilon as a PARAMETER

def bisection_root(x, epsilon):
                    # -------
                    
    low = 0

    high = x

    guess = (high + low) / 2.0

    while abs(guess ** 2 - x) >= epsilon:

        if guess ** 2 < x:

            low = guess

        else:
            
            high = guess


        guess = (high + low) / 2.0


    return guess  


print(bisection_root(123, 0.01))
                        # -----
                        

# KEYWORD PARAMETERS & DEFAULT VALUES                        
 
# def bisection_root(x, epsilon)can be improved


# We added epsilon as an argument to the function

    # Most of the time we want some standard value, 0.01

    # Sometimes, we may want to use some other value
    

# Use a keyword parameter aka a default parameter


# Epsilon as a KEYWORD PARAMETER

def bisection_root(x, epsilon = 0.01):
                    # ---------------
                    # Default parameter, with default value of 0.01              
         
    low = 0

    high = x

    guess = (high + low) / 2.0
    
    
    while abs(guess ** 2 - x) >= epsilon:
        
        if guess ** 2 < x:
            
            low = guess
            
        else:
            
            high = guess
            
        guess = (high + low) / 2.0
        
    return guess


print(bisection_root(123))
    # -------------------
    # Uses epsilon as 0.01 (the default one in function def)
    
    
print(bisection_root(123, 0.5))
                        # ---
                        # Uses epsilon as 0.5
                         
                         
     
# RULES for KEYWORD PARAMETERS


# In the function definition:


# These are ok for calling a function:
    
# bisection_root_new(123)
# bisection_root_new(123, 0.001)
# bisection_root_new(123, epsilon=0.001)
# bisection_root_new(x=123, epsilon=0.1)
# bisection_root_new(epsilon=0.1, x=123)


# These are not ok for calling a function:
    
# bisection_root_new(epsilon=0.001, 123) #error

# bisection_root_new(0.001, 123) #no error but wrong    

# FUNCTIONS RETURNING FUNCTIONS


# OBJECTS IN A PROGRAM


def is_even(i):
    
    return i % 2 == 0


r = 2

pi = 22 / 7

my_func = is_even
# ---------------
# NOT a function call, just names!


a = is_even(3)
# ------------


b = my_func(4)
# ------------
# Functon calls




                                                   
                                                  ################## 
                                                  #                #     
    #############                                 #    function    #
    #  my_func  #  -----------                    #                #
    #############            |                    #    object      #                    
#                            |----------------▶︎   #                #
#                            |                    #    named       #
    #############            |                    #                #
    #  is_even  #  -----------                    #    is_even     #
    #############                                 #                #
                                                  ################## 
    
    
    #############                                ##################  
    #     r     #  ---------------------------▶︎  #  int object 2  #                
    #############                                ################## 
    
    
                                                 
                                                 ##################
    #############                                #  float object  #
    #    pi     #  ---------------------------▶︎  #  3.14285714    # 
    #############                                ##################                           
    
    
    
    
    #############                                ##################                             
    #     a     #  --------------------------▶︎   #     False      #
    #############                                ##################
    
    
    #############                                ##################
    #     b     #  --------------------------▶︎   #     True      #
    #############                                ##################
    



# FUNCTIONS CAN RETURN FUNCTIONS
    

def make_prod(a):
    
    def g(b):
  # ---------      
        
        return a * b
      # ------------
      # This function def is inside another function         


    return g
  # --------
  # This is not a function call! 




    ##################################      ##################################
    #                                #      #                                #      
    #                                #      #    doubler = make_prod(2)      #
    #    val = make_prod(2)(3)       #      #                                #
    #                                #      #    val = doubler(3)            #
    #    print(val)                  # SAME #                                #
    #                                #      #    print(val)                  #
    #                                #      #                                #
    ##################################      ##################################



print("-----------------------")

val = make_prod(2)(3)
print(val)

  
# SAME

print("-----------------------")

doubler = make_prod(2)

val = doubler(3)

print(val)

print("-----------------------")


# SCOPE DETAILS FOR WAY 1

def make_prod(a):
    
    def g(b):
        
        return a * b
    

    return g


val = make_prod(2)(3)

print(val)


# SCOPE DETAILS FOR WAY 1


                                      ################################
# def make_prod(a):                   #                              #
                                      #    Global scope              #
    ########################          #                              #
    #                      #          #                              #
    #  def g(b):           #          #                 ###########  # 
    #                      #          #    make_prod    #         #  #
    #      return a * b    #          #                 #  Some   #  #
    #                      #     -----#-----------------#----     #  #
    #                      #    |     #                 #  code   #  #
    #  return g   ◀︎--------#----      #                 #         #  #
    ########################          #                 ###########  # 
                                      #                              #
                                      #                              #
                                      #                              #
                                      #                              #
# val = make_prod(2)(3)               #                              #
                                      #                              # 
                                      #                              #
# print(val)                          #                              #
                                      #                              # 
                                      ################################




# SCOPE DETAILS FOR WAY 1

                                      ################################      #####################################     ##########################               
# def make_prod(a):                   #                              #      #                                   #     #                        #
                                      #    Global scope              #      #                                   #     #  Note: definition      #
#   def g(b):   ◀︎--------------       #                              #      #    make_prod                      #     #                        #
#                              |      #                 ###########  #      #                                   #     #  of g is done          #
#       return a * b           |      #    make_prod    #         #  #      #    scope                          #     #                        #
#                              |      #                 #  Some   #  #      #              ##############       #     #  within scope of       #                
#                  ------------|------#-----------------#---------#--#------#--------------#------|     #       #     #                        #
#   return g      |            |      #                 #  code   #  #      #              #      |     #       #     #  make_prod, so         #
#                 |            |      #                 #         #  #      #    a         #      ▼     #       #     #                        #
#        ---------------       |      #                 ###########  #      #              #      2     #       #     #  binding of g is       #
# val = | make_prod(2) | (3)   |      #                              #      #              #            #       #     #                        #
#       ---------------        |      #                              #      #              #            #       #     #  within that           #
#                              |      #                              #      #              ##############       #     #                        #
# print(val)                   |      #                              #      #                                   #     #  frame / scope         #
#                               ------#------------------------------#------#-----------                        #     #                        #
                                      #                              #      #          |                        #     ##########################
                                      #                              #      #          |   ##############       #
                                      #                              #      #          |   #            #       #
                                      #                              #      #    g     |   #    Some    #       #     ########################## 
                                      #                              #      #          ----#--- code    #       #     #                        #
                                      #                              #      #              #            #       #     #  Since g is bound      #
                                      #                              #      #              ##############       #     #                        #
                                      #                              #      #                                   #     #  in this frame,        #
                                      #                              #      #                                   #     #                        #
                                      #                              #      #                                   #     #  cannot access it      #
                                      #                              #      #                                   #     #                        #
                                      #                              #      #                                   #     #  by evaluation in      # 
                                      #                              #      #                                   #     #                        #
                                      #                              #      #                                   #     #  global frame          #    
                                      #                              #      #                                   #     #                        #
                                      ################################      #####################################     ########################## 
    
    
                                                                                                                      ##########################
                                                                                                                      #                        #
                                                                                                                      #  g can only be         #      
                                                                                                                      #                        #
                                                                                                                      #  accessed within       #
                                                                                                                      #                        #
                                                                                                                      #  call to               #
                                                                                                                      #                        #
                                                                                                                      #  make_prod, and        # 
                                                                                                                      #                        #
                                                                                                                      #  each call will        #
                                                                                                                      #                        #
                                                                                                                      #  create a new,         #
                                                                                                                      #                        #
                                                                                                                      #  internal g            #
                                                                                                                      #                        #
                                                                                                                      ##########################                        
                                                                                                                           
    

  
    
    

# SCOPE DETAILS FOR WAY 1

                                      ################################      #####################################                 
# def make_prod(a):                   #                              #      #                                   #     
                                      #    Global scope              #      #                                   #    
#   def g(b):   ◀︎--------------       #                              #      #    make_prod                      #   
#       ---------------        |      #                 ###########  #      #                                   #  
#      | return a * b |        |      #    make_prod    #         #  #      #    scope                          #    
#      ---------------         |      #                 #  Some   #  #      #              ##############       #                   
#           ----               |      #                 #         #  #      #              #            #       #     
#   return | g |               |      #                 #  code   #  #      #              #            #       #    
#          ----                |      #                 #         #  #      #    a         #            #       #    
#        ---------------       |      #                 ###########  #      #              #      2     #       #     
# val = | make_prod(2) | (3)   |      #                              #      #              #            #       #    
#       ---------------        |      #                              #      #              #            #       #   
#               this is g      |      #                              #      #              ##############       #     
# print(val)                   -------#-----------------------       #      #                                   #    
#                                     #                      |       #      #                                   #     
                                      #                      |       #      #                                   #     
                                      #                 ##########   #      #              ##############       #
                                      #                 #        #   #      #              #            #       #
                                      #                 #  g's   #   #      #    g         #    Some    #       #     
                                      #                 #        #   #      #              #    code    #---    #    
                                      #                 #  code  #   #      #              #            #  |    #     
                                      #                 #        #   #      #              ##############  |    #    
                                      #                 ##########   #      #                              |    #     
                                      #                      ▲       #      #                              |    #     
                                      #                      |       #      #                              |    #    
                                      #                      |       #      #                              |    #   
                                      #                      --------#------#-------------------------------    #     
                                      #                              #      #  return pointer to g code         #     
                                      #                              #      #                                   #       
                                      #                              #      #                                   #     
                                      ################################      #####################################  



# Evaluating make_prod(2) has returned an anonymous procedure



# SCOPE DETAILS FOR WAY 1  


                                      ################################      #####################################      #####################################                
# def make_prod(a):                   #                              #      #                                   #      #                                   #   
                                      #    Global scope              #      #                                   #      #    g scope                        #
#   def g(b):   ◀︎--------------       #                              #      #    make_prod                      #      #                                   #
#       ---------------        |      #                 ###########  #      #                                   #      #                                   #
#      | return a * b |        |      #    make_prod    #         #  #      #    scope                          #      #                                   #
#      ---------------         |      #                 #  Some   #  #      #              ##############       #      #              ##############       #                
#                              |      #                 #         #  #      #              #            #       #      #              #            #       #  
#   return  g                  |      #                 #  code   #  #      #              #            #       #      #              #            #       #  
#                              |      #                 #         #  #      #    a         #            #       #      #    b         #            #       #  
#        -------------------   |      #                 ###########  #      #              #      2     #       #      #              #      3     #       #  
# val = | make_prod(2)  (3) |  |      #                              #      #              #            #       #      #              #            #       #   
#       --------------------   |      #                              #      #              #            #       #      #              #            #       #  
#             | this is g(3)   |      #                              #      #              ##############       #      #              ##############       #   
# print(val)  |                -------#-----------------------       #      #                                   #      #                     ▲             #   
#             |                       #                      |       #      #                                   #      #                     |             #    
#             |                       #                      |       #      #                                   #      #                     |             #    
#             |                       #                 ##########   #      #              ##############       #      #                     |             #
#             |                       #                 #        #   #      #              #            #       #      #                     |             #
#             |                       #                 #  g's   #   #      #    g         #    Some    #       #      #                     |             #   
#             |                       #                 #        #   #      #              #    code    #       #      #                     |             #   
#             |                       #                 #  code! #   #      #              #            #       #      #                     |             #    
#             |                       #                 #        #   #      #              ##############       #      #                     |             #   
#             |                       #                 ##########   #      #                                   #      #                     |             #   
#             |                       #                              #      #                                   #      #                     |             #   
#             |                       #                              #      #                                   #      #                     |             # 
#             |                       #                              #      #                                   #      #                     |             #   
#              ------------------------------------------------------#------#-----------------------------------#------#---------------------              #                                         #    
                                      #                              #      #                                   #      #                                   #     
                                      #                              #      #                                   #      #                                   #     
                                      #                              #      #                                   #      #                                   #     
                                      ################################      #####################################      #####################################




# SCOPE DETAILS FOR WAY 1


                                      ################################      #####################################      #####################################                
# def make_prod(a):                   #                              #      #                                   #      #                                   #   
                                      #    Global scope              #      #                                   #      #    g scope                        #
#   def g(b):   ◀︎--------------       #                              #      #    make_prod                      #      #                                   #
#       ---------------        |      #                 ###########  #      #                                   #      #                                   #
#      | return a * b |        |      #    make_prod    #         #  #      #    scope                          #      #                                   #
#      ---------------         |      #                 #  Some   #  #      #              ##############       #      #              ##############       #                
#                              ----   #                 #         #  #      #              #            #       #      #              #            #       #  
#   return  g                     |   #                 #  code   #  #      #              #            #       #      #     b        #     3      #       #  
#                                 |   #                 #         #  #      #    a         #            #       #      #              #            #       #  
#  ----------------------------   |   #                 ###########  #      #              #      2     #       #      #              ##############       #  
# | val = | make_prod(2)  (3) |   |   #                              #      #              #            #       #      #                                   #   
# ----------------------------    |   #                              #      #              #            #       #      #                                   #  
#                                 |   #                              #      #              ##############       #      #                                   #   
# print(val)                      ----#-----------------------       #      #                                   #      #              ##############       #   
                                      #                      |       #      #                                   #      #              #            #       #    
                                      #                      |       #      #                                   #    ---------------  #      6     #       #    
                                      #                 ##########   #      #              ##############       #   |  #              #            #       #
                                      #                 #        #   #      #              #            #       #   |  #              ##############       #
##################################    #                 #  g's   #   #      #    g         #    Some    #       #   |  #                                   #   
#                                #    #                 #        #   #      #              #    code    #       #   |  #                                   #   
#  Internal procedure only       #    #                 #  code! #   #      #              #            #       #   |  #                                   #    
#                                #    #                 #        #   #      #              ##############       #   |  #                                   #   
#  accessible within scope from  #    #                 ##########   #      #                                   #   |  #                                   #   
#                                #    #                              #      #                                   #   |  #                                   #   
#  parent procedure's call       #    #                              #      #                                   #   |  #                                   # 
#                                #    #                              #      #                                   #   |  #                                   #
##################################    #                              #      #                                   #   |  #                                   #
                                      #                 ###########  #      #                                   #   |  #                                   #
                                      #                 #         #  #      #                                   #   |  #                                   #
                                      #                 #         #  #      #                                   #   |  #                                   #
                                      #                 #    6 ◀︎--#--#------#-----------------------------------#---   #                                   #
                                      #                 #         #  #      #                                   #      #                                   #
                                      #                 #         #  #      #                                   #      #                                   #   
                                      #                 ###########  #      #                                   #      #                                   #
                                      #                              #      #                                   #      #                                   #     
                                      #                              #      #                                   #      #                                   #     
                                      #                              #      #                                   #      #                                   #     
                                      ################################      #####################################      #####################################




# How does g get value for a?

# Interpreter can move up hierarchy of frames to see both b an a values

print("-----------------------")



# SCOPE DETAILS FOR WAY 2

def make_prod(a):
    
    def g(b):
        
        return a * b
    
    return g


doubler = make_prod(2)

val = doubler(3)

print(val)


# SCOPE DETAILS FOR WAY 2

                                        ##############################      ##############################    
                                        #                            #      #                            #           
def make_prod(a):                       #    Global scope            #      #    make_prod               #
                                        #                            #      #                            #
    def g(b):                           #                            #      #    scope                   #
                                        #    make_prod  ##########   #      #                            #
        return a * b                    #               #        #   #      #                            # 
                                        #               #  Some  #   #      #             ###########    #
    return g                            #               #        #   #      #             #         #    #
#                 g                     #               #  code  #   #      #    a        #    2    #    #
#            ---------------            #               #        #   #      #             #         #    #
# doubler = | make_prod(2) |            #               ##########   #      #             ###########    #
#            --------------             #                            #      #                            #
                                        #                            #      #                            #
val = doubler(3)                        #                            #      #                            #
                                        #               ##########   #      #             ###########    #
print(val)                              #               #        #   #      #             #         #    #
                                        #               #  go's  #   #      #             #  Some   #    #
                                        #               #        #   #      #     g       #         # ---#-------   
                                        #    doubler    #  code! #   #      #             #  code   #    #      |
                                        #               #        #   #      #             #         #    #      |
                                        #               ##########   #      #             ###########    #      |
                                        #                   ▲        #      #                            #      |
                                        #                   |        #      #                            #      |
                                        #                   |        #      #                            #      |
                                        #                   |        #      #                            #      |
                                        #                   |        #      #                            #      |
                                        #                   |        #      #                            #      |
                                        #                   ---------#------#----------------------------#-------
                                        #                            #      #                            #
                                        #                            #      #                            #
                                        #                            #      #                            #
                                        ##############################      ##############################
                                        
                                        
                                        
                                        

# SCOPE DETAILS FOR WAY 2                                        


                                        ##############################      ##############################    
                                        #                            #      #                            #           
# def make_prod(a):                     #    Global scope            #      #    make_prod               #
                                        #                            #      #                            # 
#   -------------------|                #                            #      #                            #
#  | def g(b):         |                #                            #      #    scope                   #
#  |                   |                #                            #      #                            #
#  |    return a * b   |                #               ##########   #      #                            #
#  --------------------|                #               #        #   #      #                            #  
                                        #               #  Some  #   #      #             ###########    #
#   return g                            #    make_prod  #        #   #      #             #         #    #
#                 g                     #               #  code  #   #      #    a        #    2    #    #
#  ---------------------------          #               #        #   #      #             #         #    #
# | doubler =   make_prod(2) |          #               ##########   #      #             ###########    #
#  --------------------------           #                            #      #                            #
                                        #                            #      #                            #
# val = doubler(3)                      #                            #      #                            #
                                        #               ##########   #      #             ###########    #
# print(val)                            #               #        #   #      #             #         #    #
                                        #               #  go's  #   #      #             #  Some   #    #
                                        #               #        #   #      #     g       #         #    #   
                                        #    doubler    #  code! #   #      #             #  code   #    #      
                                        #               #        #   #      #             #         #    #      
                                        #               ##########   #      #             ###########    #      
                                        #                            #      #                            #      
                                        #                            #      #                            #      
                                        #                            #      #                            #      
                                        #                            #      #                            #      
                                        #                            #      #                            #      
                                        #                            #      #                            #      
                                        #                            #      #                            #
                                        #                            #      #                            #
                                        #                            #      #                            #
                                        #                            #      #                            #
                                        ##############################      ##############################





#########################################
#                                       #
#  Evaluating make_prod(2) has          #
#                                       #
#  same effect as previous example -    #
#                                       #
#  doubler is a function object         # 
#                                       #
#                                       #
#########################################




# SCOPE DETAILS FOR WAY 2

                                     ####################################       #####################################       #####################################  
                                     #                                  #       #                                   #       #                                   #
# def make_prod(a):                  #    Global scope                  #       #                                   #       #                                   #
#                                    #                                  #       #    make_prod                      #       #    doubler scope                  #
#    def g(b):                       #                                  #       #                                   #       #                                   #
#                                    #                                  #       #    scope                          #       #                                   #
#                --------            #                  ##########      #       #                                   #       #                                   # 
#        return | a * b |            #                  #        #      #       #              ############         #       #              ############         #
#               --------             #                  #  Some  #      #       #              #          #         #       #              #          #         #
                                     #    make_prod     #        #      #       #    a         #    2     #         #       #    b         #    3     #         #
#    return g                        #                  #  code  #      #       #              #          #         #       #              #          #         #
                                     #                  #        #      #       #              ############         #       #              ############         #
                                     #                  ##########      #       #                                   #       #                                   #
doubler = make_prod(2)               #                                  #       #                                   #       #                                   #
                                     #                                  #       #                                   #       #                                   #
#  -------------------               #                                  #       #              ############         #       #              ############         #
# | val = doubler(3) |               #                  ###########     #       #              #          #         #       #              #          #         # 
# -------------------                #                  #         #     #       #              #  Some    #         #       #              #    6     #         #
#      Now Invoking g(3)             #     doubler      #  go's   #     #       #     g        #          #         #       #              #    |     #         #
                                     #                  #         #     #       #              #  code    #         #       #              #####|######         #
                                     #                  #  code!  #     #       #              #          #         #       #                   |               # 
print(val)                           #                  #         #     #       #              ############         #       #                   |               #
                                     #                  ###########     #       #                                   #       #                   |               #
                                     #                                  #       #                                   #       #                   |               #
                                     #                                  #       #                                   #       #                   |               #
                                     #                                  #       #                                   #       #                   |               #
                                     #                                  #       #                                   #       #                   |               #
                                     #                                  #       #                                   #       #                   |               #
                                     #     val           ##########     #       #                                   #       #                   |               #
                                     #                   #        #     #       #                                   #       #                   |               #
                                     #                   #   6    #     #       #                                   #       #                   |               # 
                                     #                   #        #  ◀︎--#-------#-----------------------------------#-------#-------------------                # 
                                     #                   ##########     #       #                                   #       #                                   #
                                     #                                  #       #                                   #       #                                   #
                                     #                                  #       #                                   #       #                                   # 
                                     #                                  #       #                                   #       #                                   #
                                     #                                  #       #                                   #       #                                   #
                                     #                                  #       #                                   #       #                                   # 
                                     ####################################       #####################################       #####################################                     
                                     
                                     
                                                                                                               #  Return value
                                                                                                               
                                                                                                               

# WHY BOTHER RETURNING FUNCTIONS?


# Code can be rewritten without returning function objects


# Good software design

    # Embracing ideas of decomposition, abstraction
    
    # Another tool to structure code


# Interrupting execution


# Example of control flow

    # A way to achieve partial execution and use result somewhere else before
    # finishing the full evaluation



# TESTING and DEBUGGING


    #########################################################################
    #                                                                       #
    #                                                                       #
    #                          DEFENSIVE PROGRAMMING                        #
    #                                                                       #
    #                                                                       #
    #       Wrte specfcations for a functions                               #
    #                                                                       #
    #       Modularze programs                                              # 
    #                                                                       #
    #      Check conditions on inputs / outputs (assertions)                #
    #                                                                       #
    #                                                                       #
    #########################################################################
#                    |                      |
#                    |                      |
#                    |                       ------------------
#                    |                                        |
#                    |                                        |
#                    |                                        |
#                    ▼                                        ▼
  ######################################    ######################################
  #                                    #    #                                    #
  #                                    #    #                                    #
  #                                    #    #    DEBUGGING                       #
  #        TESTING / VALIDATION        #    #                                    #
  #                                    #    #                                    #
  #                                    #    #                                    #
  #    Compare input / output          #    #    Study events leading up         #
  #                                    #    #                                    #
  #    pairs to specifications         #    #    to an error                     #
  #                                    #    #                                    #
  #    "it's not working"              #    #    "Why it is not working?"        #
  #                                    #    #                                    #
  #    "How can I break my program?"   #    #    "How can I fix my program?"     #
  #                                    #    #                                    #  
  #                                    #    #                                    #
  #                                    #    #                                    # 
  #                                    #    #                                    #
  ######################################    ######################################                                 



# SET YOURSELF UP FOR EASY TESTING AND DEBUGGING


# From the start, design code to ease this part

# Break program up into modules that can be tested and debugged individually


# Document constraints on modules

    # What do you expect the input to be?
    # What do you expect the output to be?
    
    
# Document assumptions behind code design

    # Ensure code runs
    
    # Remove syntax errors
    
    # Python interpreter can usually find these for you  
    
    
# Have a set of expected results

# An input set

# For each input, the expected output


# CLASSES OF TESTS

#     --------
#    |       |
#    |       ▼
#    |   --▶︎ Unit testing
#    |  |  
#    |  |       # Validate each piece of program
#    |  |       # Testing each function separately
#    |  |         
#    |  |         
#    |  ---- Regression testing
#    |    
#    |          # Add test for bugs as you find them
#    |          # Catch reintroduced errors that were previously fixed
#    |       
#    |           
#    ------ Integration testing
#            
#               # Does overall program work?
#               # Tend to rush to do this
    
        
    

# TESTING APPROACHES

# Intuition about natural boundaries to the problem


def is_bigger(x, y):
    
    """ Assumes x and y are ints
    Returns True if y is less than x, else False """    
        
    # can you come up with some natural partitions?        
        
        

# If no natural partitions, might do random testing

    # Probability that code is correct increases with more tests        
    
    # Better options below     
    
    
# Black box testing

    # Explore paths through specification    
    
    
# Glass box testing

    # Explore paths through code
    
    
    
# BLACK BOX TESTING    
    

def sqrt(x, eps):
    
    """ Assumes x, eps floats, x >= 0, eps > 0
    Returns res such that x-eps <= res*res <= x+eps """
    
    
# Designed without looking at the code    
    
# Can be done by someone other than the implementer to avoid some
# implementer biases    
 
# Testing can be reused if implementation changes


# Paths through specification

    # Build test cases in different natural space partitions
    # Also consider boundary conditions (empty lists, singleton list, large
    # numbers, small numbers)
    
    
    
# BLACK BOX TESTING    
   

def sqrt(x, eps):
    
    """ Assumes x, eps floats, x >= 0, eps > 0
    Returns res such that x-eps <= res*res <= x+eps """ 
    
    
    
    ##################################################################################
    #  CASE                    #  x                       #  eps                     #  
    ##################################################################################
    #                          #                          #                          # 
    #  boundary                #  0                       #  0.0001                  #
    #                          #                          #                          #
    ##################################################################################  
    #                          #                          #                          # 
    #  perfect square          #  25                      #  0.0001                  #
    #                          #                          #                          #
    ################################################################################## 
    #                          #                          #                          # 
    #  less than 1             #  0.05                    #  0.0001                  #
    #                          #                          #                          #
    ################################################################################## 
    #                          #                          #                          # 
    #  irrational square root  #  0                       #  0.0001                  #
    #                          #                          #                          #
    ##################################################################################
    #                          #                          #                          # 
    #  extremes                #  2                       #  1.0/2.0**64.0           #
    #                          #                          #                          #
    ################################################################################## 
    #                          #                          #                          # 
    #  extremes                #  1.0/2.0**64.0           #  1.0/2.0**64.0 0         #
    #                          #                          #                          #
    ################################################################################## 
    #                          #                          #                          # 
    #  extremes                #  2.0**64.0               #    1.0/2.0**64.0         #
    #                          #                          #                          #
    ################################################################################## 
    #                          #                          #                          # 
    #  extremes                #  1.0/2.0**64.0           #    2.0**64.0             #
    #                          #                          #                          #
    ##################################################################################
    #                          #                          #                          # 
    #  extremes                #  2.0**64.0               #    2.0**64.0             #
    #                          #                          #                          #
    ##################################################################################  




# GLASS BOX TESTING

# Use code directly to guide design of test cases

# Called path-complete if every potential path through code is tested at
# least once


# What are some drawbacks of this type of testing?

    # Can go through loops arbitrarily many times
    
    # Missing paths
    

# Guidelines


    # Branches  ------>  exericse all parts of a conditional 
    
    # For loops  ----------------->  loop not entered body of loop executed
    
    # more than once
    
    # While loops  ----------------------------->  same as for loops, cases
    
    # that catch all ways to exit loop
    
    

# GLASS BOX TESTING


def abs(x):

    """ Assumes x is an int Returns x if x >= 0 and -x otherwise """    
    
    if x < -1:
        
        return -x
    
    else:
        
       return x
 
    
print("----------------------") 
   
print(abs(-1))

print(abs(1))

print(abs(-2))

print(abs(2))   
   

# Aa path-complete test suite could miss a bug

# Path-complete test suite: 2 and -2

# But abs(-1) incorrectly returns -1

# Should still test boundary cases


# DEBUGGING


# Once you have discovered that your code does not run properly, you want to:
    
    # Isolate the bug(s)
    # Eradicate the bug(s)
    # Retest until code runs correctly for all cases
    # Steep learning curve    


# Goal is to have a bug-free program


# Tools

    # Built in to IDLE and Anaconda
    # Python Tutor
    # printstatement
    # Use your brain, be systematic in your hunt
    
    
# ERROR MESSAGES – EASY


# Trying to access beyond the limits of a list    
    
# test = [1,2,3] then test[4]  ------>  IndexError    
    
# Trying to convert an inappropriate type

# int(test)  ----->  TypeError

# Referencing a non-existent variable

# a  ------>  NameError

# Mixing data types without appropriate coercion

# '3'/4  ------>  TypeError

# Forgetting to close parenthesis, quotation, etc.

# a = len([1,2,3]

# print(a)  ------>  SyntaxError



# LOGIC ERRORS - HARD

    # think before writing new code

    # draw pictures, take a break

    # explain the code to
    
        # someone else
        
        # a rubber ducky
        
        
        
# DEBUGGING STEPS        


    # Study program code
    
        # Don’t ask what is wrong
        
        # Ask how did I get the unexpected result
        
        # Is it part of a family?
        
        
    # Scientific method  

        # Study available data
        
        # Form hypothesis
        
        # Repeatable experiments
        
        # Pick simplest input to test with
      
        
   
# PRINT STATEMENTS 


# Good way to test hypothesis


# When to print

    # Enter function
    
    # Parameters
    
    # Function results
    
    
# Use bisection method

    # Put print halfway in code
    
    # Decide where bug may be depending on values




    
    
    
    
    
    









       
        
        
        
        
        
        





      
        
        
        
        
        
        
        
        
        



















    
   
    
   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    








    
    
    
    
    
    





    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    









   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        
        
        
        
        















    
    

  
  
  
  
  
    
  
    
  
    
  
    
  
    
  
    
  
    
    
    
    
    
    
    
    
    
































                                                                                                               
                                     
































    













































    




































    







                         
                         
                         
                         
                         
                         
                         
                         
                         
                         
                         
            
    







    
            
            
            
            
            
            
            
            
    
    
    
    
    
    
    
    
    
    
    
    





                    















    




                       
                        
                        
                        
                        
                        
                        
                        








                  
    





























    




        
        
        
        
        
        
    
    
    
    
    
    
    









































       




























































































    












       







































    













    
    
    
    
    