#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 04:17:07 2024

@author: sheeraz
"""


# FUNCTIONS as OBJECTS


# FUNCTION FROM LAST LECTURE


def is_even(i):
    
    """
        Input: i, a positve input 
        Returns True if i is even and False otherwise  
    
    """
    
    return i % 2 == 0


# A function always returns something

print(is_even(8))


# WHAT IF THERE IS NO return KEYWORD

def is_even(i):
    
    """
    
        Input: i, a positive int
        does not return anything
    
    """
    
    i % 2 == 0
  # ----------
  # without a return statement
  
 
# Python returns the value None, if no returngiven

# Represents the absence of a value

    # If invoked in shell, nothing is printed
    
# No static semantic error generated

def is_even(i):
    
    """
    
        Input: i, a positive int
        does not return anything
    
    """
    
    i % 2 == 0
    
        # None s a value of type NoneType (not a string, not a number, etc)    
        # -----
    return None
  # ------
  # A line python adds implctly (do not add it yourself)
  
  
# YOU TRY IT!

# What is printed if you run this code as a file?

def add(x, y):
    
    return x + y

def mult(x, y):
    
    print(x * y)
   
   
    
add(1, 2)

print(add(2, 3))


mult(3, 4)

print(mult(4, 5))

 
    #   return                       vs.              print
       
    
    # return only has meaning                print can be used outsid 
    # inside a function                      functions
      
    # only one return executed              can execute many print statements
    # inside a function                     inside a function 
  
    # code inside function, but             code inside function can be                                                      
    # after return statement,               executed after a print
    # not executed                          statement
  
    # has a value associated                # has a value associated with
    # with it, given to function            # it, outputted to the console
    # caller
                                            # print expression itself returns
                                            # Nonevalue     
    
  
    
# YOU TRY IT!

# Fix the code that tries to write this function

def is_triangular(n):
    
    """
        n is an int > 0
        returns True if n is triangular, i.e. equals a continued
        summation of natural numbers (1 + 2 + 3 + ... +k), False
        otherwise
    
    """
    
    total = 0
    
    for i in range(n + 1):
        
        total += i
        
        if total == n:
            
            print(True)
            
    print(False)
        
   


is_triangular(10)


# FUNCTIONS SUPPORT MODULARITY
         
# Here is our bisection square root method as a function

def bisection_root(x):
    
   #############################################
                                               #
    epsilon = 0.01                             #
  # --------------                             #
                                               # 
    low = 0                                    # 
  # -------                                    #
                                               #   Intialize variables  
    high = x                                   #
  # --------                                   #
                                               #
    ans = (low + high) / 2.0                   #
  # ------------------------                   #
                                               #
   #############################################
    
  
   ############################################################ 
                                                              #
    while abs(ans ** 2 - x) >= epsilon:                       #
  # -----------------------------------                       #
  #    guess not close enough                                 #
                                                              #
        #############################                         #
                                    #                         #                        
                                    #                         #
        if ans ** 2 < x:            #                         #
      # ----------------            #                         #
                                    #                         #  
            low = ans               #                         #
          # ---------               #  update low or hght,    #
                                    #  depends on guess too   #  iterate
        else:                       #  small or too large     #
      # -----                       #                         #
                                    #                         #
            high = ans              #                         #
          # ----------              #                         #
                                    #                         #
                                    #                         #
        #############################                         #
                                                              #
        ans = (high + low) / 2.0                              #
      # ------------------------                              #
      #   new value for guess                                 #
                                                              #
     ##########################################################
    
    
  #################################################### 
                                                     #
    # print(ans, "is close to the root of", x)       #
                                                     #
    return ans                                       #  return result 
  # ----------                                       #
                                                     #
                                                     #
  ####################################################
  
  
  
  
# FUNCTIONS SUPPORT MODULARITY
  
# Call it with different values
  
print(bisection_root(4))
  
print(bisection_root(123))


# Write a function that calls this one!

# YOU TRY IT!

# Write a function that satisfies the following specs

# def count_nums_with_sqrt_close_to (n, epsilon):
    
    # """ n is an int > 2
    # epsilon is a positive number < 1
    # Returns how many integers have a square root within epsilon of n """

     
# Use bisection_rootwe already wrote to get an approximation for the sqrt
# of an integer.

# For example: print(count_nums_with_sqrt_close_to(10, 0.1))

# prints 4 because all these integers have a sqrt within 0.1

    # sqrt of 99is 9.949699401855469
    # sqrt of 100is 9.999847412109375
    # sqrt of 101is 10.049758911132812
    # sqrt of 102is 10.099456787109375
    
    
# ZOOMING OUT    


# this is my "black box"

#         |
#         |
#         |
#         |
#         ▼

def sum_odd(a, b):                           #########################################
                                             #                                       #
    sum_of_odds = 0                          #                                       #
                                             #  Program Scope                        #
    for i in range(a, b + 1):                #                                       #
                                             #                                       #
        if i % 2 == 1:                       #                     ------------      #
                                             #  sum_odd           |  functon   |     #
            sum_of_odds += i                 #                    |  object    |     #
                                             #                    -------------      #
                                             #                                       #
    return sum_of_odds                       #                    --------------     #                
                                             #   low             |      2      |     # 
                                             #                    --------------     # 
low = 2                                      #                                       #
                                             #                    --------------     #
high = 7                                     #   high            |      7      |     #
                                             #                    --------------     #
my_sum = sum_odd(low, high)                  #                                       #
       # ------------------                  #                                       #
       # one functon call                    #                                       #
                                             #                                       #
                                             #   my_sum                              #
                                             #                                       #
                                             #########################################        



print(my_sum)

        


def sum_odd(a, b):
        #  -- -- 
      # a = 2  b = 7
                                             #########################################
                                             #                                       #
    sum_of_odds = 0                          #                                       #
                                             #  Program Scope                        #
    for i in range(a, b + 1):                #                                       #
                                             #                                       #
        if i % 2 == 1:                       #                     ------------      #
                                             #  sum_odd           |  functon   |     #
            sum_of_odds += i                 #                    |  object    |     #
                                             #                    -------------      #
                                             #                                       #
    return sum_of_odds                       #                    --------------     #                
                                             #   low             |      2      |     # 
                                             #                    --------------     # 
low = 2                                      #                                       #
                                             #                    --------------     #
high = 7                                     #   high            |      7      |     #
                                             #                   --------------      #
#                   ------   -------         #                                       #
# my_sum = sum_odd(| low |, | high |)        #                                       #
#                  ------   --------         #                                       #
                                             #                                       #
                                             #                                       #
                                             #   my_sum                              #
                                             #                                       #
                                             ######################################### 



# ZOOMING OUT

       
# this is my "black box"

#         |
#         |
#         |
#         |
#         ▼

def sum_odd(a, b):                           #########################################
                                             #                                       #
    sum_of_odds = 0                          #                                       #
                                             #  Program Scope                        #
    for i in range(a, b + 1):                #                                       #
                                             #                                       #
        if i % 2 == 1:                       #                     ------------      #
                                             #  sum_odd           |  functon   |     #
            sum_of_odds += i                 #                    |  object    |     #
                                             #                    -------------      #
#   ----------------------                   #                                       #
#  |  return sum_of_odds |                   #                    --------------     #                
#  -----------------------                   #   low             |      2      |     # 
                                             #                    --------------     # 
low = 2                                      #                                       #
                                             #                    --------------     #
high = 7                                     #   high            |      7      |     #
           #  -----------------------        #                    --------------     #
# my_sum =   |  sum_odd(low, high)  |        #                                       #
           # ------------------------        #                                       #
                                             #                    --------------     #
#                      ▲                     #                   |      15     |     #
#                      |                     #   my_sum           --------------     #
#                      |                     #                                       #
#                                            #########################################     
#                     15  
#                          
    

# FUNCTION SCOPE

# UNDERSTANDING FUNCTION CALLS


# How does Python execute a function call?
# How does Python know what value is associated with a variable name?


# It creates a new environment with every function call!

# Like a mini program that it needs to complete
# The mini program runs with assigning its parameters to some inputs
# It does the work (aka the body of the function)
# It returns a value
# The environment disappears after it returns the value


# ENVIRONMENTS


# Global environment

    # Where user interacts with Python interpreter
    # Where the program starts out
    

# Invoking a function creates a new environment (frame/scope)


# VARIABLE SCOPE


# Formal parameters get bound to the value of input parameters

# Scope is a mapping of names to objects

    # Defines context in which body is evaluated
    # Values of variables given by bindings of names
    
    
# Expressions in body of function evaluated wrt this new scope


###################################
                                  #
                                  # 
def f(x):                         #     
   # ---                          #
   # formal parameter             #
                                  #         function definition
   x = x + 1                      #
                                  #
   print("in f(x): x = ", x)      # 
                                  # 
   return x                       #
                                  #
                                  #
                                  ##########################################





###########################
                          #  Main program code             
y = 3                     #  
# --                      #  * initializes a variable x  
                          #  * makes a function call f(x) 
z = f(y)                  #  * assigns return of function to variable z 
   # --                   #
   # actual parameter     #  Can be any legal value
                          #
                          ################################################### 
    
   


# VARIABLE SCOPE after evaluating def   
  
                                          
#####################################     ##############################
                                    #     #                            # 
def f(x):                           #     #   Global scope             # 
                                    #     #                            # 
    x = x + 1                       #     #         ---------------    #
                                    #     #   f    |   function   |    #
    print("in f(x): x =", x)        #     #        |   object     |    #
                                    #     #        ----------------    #
    return x                        #     #                            #
                                    #     #                            #
                                    #     #                            #
x = 3                               #     #                            #
# --                                #     #                            #
z = f(x)                            #     #                            #
                                    #     #                            #
                                    #     ##############################
                                    #
                                    #########################################


print(z)



# VARIABLE SCOPE after exec 1st assignment





#       This is my "black box"       
#
#               |
#               |
#               |     
#               ▼         

#####################################     ##############################
                                    #     #                            # 
def f(x):                           #     #   Global scope             # 
                                    #     #                            # 
    x = x + 1                       #     #         ---------------    #
                                    #     #   f    |   function   |    #
    print("in f(x): x =", x)        #     #        |   object     |    #
                                    #     #        ----------------    #
    return x                        #     #                            #
                                    #     #         --------------     #
                                    #     #   x    |      3      |     #
x = 3                               #     #        ---------------     #
# --                                #     #                            #
z = f(x)                            #     #                            #
                                    #     #                            #
                                    #     ##############################
                                    #
                                    #########################################


print(z)



# VARIABLE SCOPE after f invoked





#       This is my "black box"       
#
#               |
#               |
#               |     
#               ▼         


#         ---------------------------------------------------------------------- 
#        |                                                                     |
#        |                                                                     |
#########|###########################     ##############################     ##|###########################   
#        |                          #     #                            #     # |                          #
# def f(x):                         #     #   Global scope             #     # |  f scope                 # 
#                                   #     #                            #     # |                          #
#    x = x + 1                      #     #         ---------------    #     #  --                        #
#                                 --#-----#---> f  |   function   |    #     #    ▼    -------------      #
#   print("in f(x): x =", x)     |  #     #        |   object     |    #     #    x   |     3      |      #
#                                |  #     #        ----------------    #     #        --------------      #
#                                |  #     #                            #     #          ▲    ▲            # 
#                                |  #     #                            #     #          |    |            #
#   return x                     |  #     #  --------------------------#-----#--------- |    |            #
#                     -----------   #     # |       --------------     #     #               |            #
#                    |              #     # |      |    -------   |    #     #               |            # 
#       -------------|--------------#-----#---> x  |   |  3   |---|----#-----#---------------             #
#      |             |              #     #        |    ------    |    #     #                            #
# x = 3  ------------               #     #        ---------------     #     #                            #
# --    |                           #     #                            #     #                            #
# z = f(x)                          #     #                            #     #                            #
                                    #     #                            #     #                            #
                                    #     ##############################     ##############################
                                    #
                                    #######################################################################


# print(z)


# VARIABLE SCOPE after f invoked


# Name of variable irrelevant, only value important. You can
# also pass in the value directly.



###########################################     ##############################     #############################
                                          #     #                            #     #                           #
                                          #     #    Global scope            #     #  f scope                  #
#  def f(x):                              #     #                            #     #                           #
                                          #     #                            #     #           -----------     #
       # x = x + 1                        #     #          ----------        #     #    x     |     3     |    #
                                          #     #    f    |  Some   |        #     #          ------------     #
       # print("in f(x): x =", x)         #     #         |  code   |        #     #                           #
                                          #     #         ----------         #     #                           #
       # return x                         #     #                            #     #                           # 
                                          #     #   ----   ----------        #     #                           #
                                          #     #  | y  | |    3    |        #     #                           #
#  ----                                   #     #   ----  -----------        #     #                           # 
# | y |  = 3                              #     #                            #     #                           #
# ----                                    #     #                            #     #                           #
                                          #     #                            #     #                           #
                                          #     #                            #     #                           #
                                          #     ##############################     #############################                       
#            ----                         #
# --> z = f(| y |)                        #
#           ----                          #########################################################################

     


# VARIABLE SCOPE eval body of f in f’s scope







#                                                                in f(x): x = 4 printed out 
#
#                  -------------------------------------------------------------------
#                 |                                                                  | 
##################|########################     ##############################     ##|##########################
#                 |                       #     #                            #     # |                         #
#                 |                       #     #    Global scope            #     # |  f scope                #
#  def f(x):      |                       #     #                            #     #  ---                      #
#                 |                       #     #                            #     #     |                     # 
#         -------------------             #     #                            #     #     ▼                     #
#        |        --         |            #     #                            #     #   -----     -----------   #
#        | x = | |x| + 1 |   |            #     #          ----------        #     #  |  x  |   |     4    |   #
#        |       --          |            #     #    f    |  Some   |        #     #  ------     ----------    #
#         -------------------             #     #         |  code   |        #     #     ▲                     #
#                                         #     #         ----------         #     #     |                     #
#       -------------------------------   #     #                            #     #     |                     #
#      |                        ----  |   #     #                            #     #     |                     #  
#      | print("in f(x): x =", | x |)-|---#-----#----------------------------#-----#-----                      #  
#      |                       ----   |   #     #                            #     #                           # 
#       ------------------------------    #     #                            #     #                           # 
#                                         #     #                            #     #                           #
                                          #     #                            #     #                           #
       # return x                         #     #          ----------        #     #                           #
#                                         #     #    x    |    3    |        #     #                           #
#                                         #     #         -----------        #     #                           # 
#  x = 3                                  #     #                            #     #                           #
                                          #     #                            #     #                           #
                                          #     #                            #     #                           #
                                          #     #                            #     #                           #
                                          #     ##############################     #############################                       
#                                         #
# --> z = f(x)                            #
#                                         #########################################################################




# VARIABLE SCOPE during return


                                                             
###########################################     ##############################     #############################
                                          #     #                            #     #                           #
                                          #     #    Global scope            #     #   f scope                 #
#  def f(x):                              #     #                            #     #                           #
                                          #     #                            #     #                           # 
                                          #     #                            #     #                           #
                                          #     #                            #     #           -----------     #
#      x = x  + 1                         #     #          ----------        #     #    x     |    4     |     #
                                          #     #    f    |  Some   |        #     #           ----|-----      #
                                          #     #         |  code   |        #     #               |           #
                                          #     #         ----------         #     #               |           #
                                          #     #                            #     #               |           #  
#      print("in f(x): x =", x)           #     #                            #     #               |           #  
                                          #     #                            #     #               |           #
#     ------------                        #     #                            #     #               |           #
#    | return x  |                        #     #          ----------        #     #               |           #
#     -----------                         #     #    x    |    3    |        #     #               |           #
                                          #     #         -----------        #     #               |           # 
#  x = 3                                  #     #                            #     #               |           #
                                          #     #               ◀︎------------#-----#----------------           #
                                          #     #                            #     #                           #
                                          #     #                            #     #                           #
                                          #     ##############################     #############################                       
#       -----------  function call        #
#      | z = f(x) |  replace with         #
#      ------------  return value         #########################################################################
      




# VARIABLE SCOPE after exec 2nd assignment


# If I now ask for value of x in Python interpretor, it wll prnt 3

    

#####################################     ##############################
                                    #     #                            # 
# def f(x):                         #     #   Global scope             # 
                                    #     #                            # 
    # x = x + 1                     #     #         ---------------    #
                                    #     #   f    |   function   |    #
    # print("in f(x): x =", x)      #     #        |   object     |    #
                                    #     #        ----------------    #
    # return x                      #     #                            #
                                    #     #         --------------     #
                                    #     #   x    |      3      |     #
# x = 3                             #     #        ---------------     #
                                    #     #                            #
                                    #     #                            #
#   ------------                    #     #        --------------      #
#  | z = f(x)  |   <----            #     #   z   |      4      |      #
#  ------------                     #     #        -------------       #
                                    #     #                            #
                                    #     #                            #
                                    #     #                            # 
                                    #     ##############################
                                    #
                                    #########################################



# BIG IDEA


# You need to know what expression you are executing to know the scope
# you are in.


# ANOTHER SCOPE EXAMPLE

# Inside a function, can access a variable defined outside

# Inside a function, cannot modify a variable defined outside (can by using
# global variables, but frowned upon)


# Use the Python Tutor to step through these!



 
#  def f(y):                  #   def g(y):                                #    def h(y):
#                             #                                            #          
#       ---------             #              ----                          #         ---------
#      | x = 1  |             #       print(| x |)                         #        | x += 1 |
#      ---------              #       print(| x | + 1)                     #        ---------
#                             #             ----                           #
#      x += 1                 #       x from outside g                     #     ---------
#                             #                                            #    | x = 5  |
#                             #                                            #    ---------
#   ---------                 #    ---------                               #    
#  | x = 5  |                 #   | x = 5  |                               #    h(x)
#  ----------                 #   ---------                                #    print(x)
#  x is re-defined            #                                            #
#  in scope of f              #   g(x)                                     #
#                             #                                            #    UnboundLocalError: local
#  f(x)                       #   print(x)                                 #    variable "x" referenced
#  print(x)                   #                                            #    before assignment
#                             #                                            #
#   ------                    #    ------                                  #
#  |  2  |                    #   |  5  |    x inside g is picked up       #
#  |  5  |                    #   |  6  |    from scope that called        #                -----------
#  ------                     #   |  5  |    function g                    #                |  error  |
#  different x objects        #   ------                                   #                -----------
#                             #                                            #


def f(y):
    
    x = 1
    
    x += 1
    
    print(x)
    
    
x = 5

f(x)

print(x)    
    
 
def g(y):

    print(x)
    print(x + 1)    
    
x = 5

g(x)

print(x)


# def h(y):
    
    # x += 1
    # cannot access local variable 'x' where it is not associated with a value
    
# x = 5    
# h(x)
# print(x)


def h(y):
    
    # x += 1
    # cannot access local variable 'x' where it is not associated with a value
    x = 2
    
    x -= 3 
    
    print(x)
    

print("-----------------------")
    
x = 5    
h(x)
print(x) 

print(65 -51)



# FUNCTIONS as ARGUMENTS
    

# HIGHER ORDER PROCEDURES


# Objects in Python have a type

    # int, float, str, Boolean, NoneType, function
    
    
# Objects can appear in RHS of assignment statement    

    # Bind a name to an object
    
  
# Objects

    # Can be used as an argument to a procedure
    # Can be returned as a value from a procedure
    
    
# Functions are also first class objects!


# Treat functions just like the other types    

    # Functions can be arguments to another function
    # Functions can be returned by another function
    


# OBJECTS IN A PROGRAM


def is_even(i):

    return i % 2 == 0


r = 2

pi = 22 / 7


my_function = is_even


a = is_even(3)
# ------------

b = is_even(4)
# ------------
# Two function calls 


                                                         #################
        ###############                                  #               #
        #   my_func   #  ############                    #               #
        ###############             #                    #  function     # 
                                    ######## -------->   #  object with  # 
                                    #                    #  some code    #
        ###############             #                    #               #
        #   is_even   #  ############                    #               #
        ###############                                  #################



                                                          
        #########                               ####################
        #   r   #  ------------------------->   #   int object 2   #
        #########                               ####################


                                                #################### 
        ##########                              #   float object   #
        #   pi   #  ------------------------>   #   3.14285714     #
        ##########                              #################### 


        
        #########                               #############
        #   a   #   ------------------------>   #   False   #
        #########                               #############
        
        
        
        #########                               #############
        #   b   #   ------------------------>   #    True   #
        #########                               #############



# BIG IDEA


# Everything in Python is an object.


# FUNCTION AS A PARAMETER


def calc(op, x, y):
    
    return op(x, y)


def add(a, b):
    
    return a + b

def div(a, b):
    
    if b != 0:
        
        return a / b
    
    print("Denominator was 0.")

print(calc(add, 2, 3))



# STEP THROUGH THE CODE




def calc(op, x, y):                   ##################################
                                      #                                # 
    return op(x, y)                   #  Program Scope                 #
                                      #                                #
                                      #                                #
def add(a, b):                        #              ------------      #
                                      #  calc       |  function  |     #
    return a + b                      #             |  object    |     #
                                      #             -------------      #
def div(a, b):                        #                                #
                                      #                                #
    if b != 0:                        #              ------------      #
                                      #  add        |  functon  |      #           
        return a / b                  #             |  object   |      #
                                      #             -------------      #
    print("Denom was 0.")             #                                #
                                      #                                # 
                                      #              ------------      #
                                      #  div        |  function |      # 
res = calc(add, 2, 3)                 #             |  object   |      #
                                      #             ------------       #
                                      #                                #
                                      #                                #
                                      #                                #
                                      #  res                           #
                                      #                                #
                                      #                                #     
                                      #                                #
                                      ##################################






# CREATE calc SCOPE


def calc(op, x, y):                   ##################################    ##########################
                                      #                                #    #                        #
    return op(x, y)                   #  Program Scope                 #    #  calc scope            #
                                      #                                #    #                        #
                                      #                                #    #                        #
def add(a, b):                        #              ------------      #    #                        #
                                      #  calc       |  function  |     #    #                        #
    return a + b                      #             |  object    |     #    #                        #
                                      #             -------------      #    #                        #
def div(a, b):                        #                                #    #                        #
                                      #                                #    #                        #
    if b != 0:                        #              ------------      #    #                        #
                                      #  add        |  functon  |      #    #                        #          
        return a / b                  #             |  object   |      #    #                        #
                                      #             -------------      #    #                        #
    print("Denom was 0.")             #                                #    #                        #
                                      #                                #    #                        #
                                      #              ------------      #    #                        #
                                      #  div        |  function |      #    #                        #
res = calc(add, 2, 3)                 #             |  object   |      #    #                        #
                                      #             ------------       #    #                        #
                                      #                                #    #                        #
                                      #                                #    #                        #
                                      #                                #    #                        #
                                      #  res                           #    #                        #
                                      #                                #    #                        #
                                      #                                #    #                        #    
                                      #                                #    #                        #
                                      ##################################    ##########################



# MATCH FORMAL PARAMS in calc



                                                                                  
#              ----------------------------------------------------------------                          
#             |                                                               | 
#           -----   ----   ----                                               |
# def calc(| op |, | x |, | y |):     ##################################    ##|#######################
#          -----    ---   -----       #                                #    # |                      #
#           |       |        |        #                                #    # |                      #
#  ---------        -------  ------   #                                #    # |                      #
# |   return op(x, y)      |      |   #  Program Scope                 #    # |calc scope            #
# |                        |      |   #                                #    # |                      #
# ---------------------    |      |   #                                #    #  ---                   #
#                     |    |      |   #                                #    #    |                   #
#                     |    |      |   #                                #    #    ▼                   #
# def add(a, b):      |    |      |   #              ------------      #    #   ----     ---------   #
#                     |    |      |   #  calc       |  function  |     #    #  | op |   |  add   |   #
    # return a + b    |    |      |   #             |  object    |     #    #   ----     --------    #
#                     |    |      |   #             -------------      #    #                        #
# def div(a, b):      |     ------|---#--------------------------------#----#-----                   #
#                     |           |   #                                #    #    |                   #           
#                      -------    |   #                                #    #    ▼                   #
    # if b != 0:              |   |   #  ------      ------------      #    #   ---      ---------   #
#                             |   |   # | add |     |  functon  |      #    #  | x |    |   2    |   #          
        # return a / b        |   |   #  ------     |  object   |      #    #  ----     ---------    #
#                             |   |   #    ▲         -------------      #    #                        #
    # print("Denom was 0.")   |   |   #    |                           #    #                        #
#                             |   ----#----|---------------------------#----#-----                   #                 
#                -------------        #    |                           #    #    |                   #
#               |   ------------------#-----                           #    #    ▼                   #
#               ▼  |                  #              ------------      #    #   ---      ---------   #
#             ------                  #  div        |  function |      #    #  | y |    |    3   |   #
# res = calc(| add |, 2, 3)           #             |  object   |      #    #   ---     ---------    #
#             -----                   #             ------------       #    #                        #
                                      #                                #    #                        #
                                      #                                #    #                        #
      # function obj NOT              #                                #    #                        #
      # function call                 #                                #    #                        #
                                      #                                #    #                        #
                                      #  res                           #    #                        #
                                      #                                #    #                        #
                                      #                                #    #                        #    
                                      #                                #    #                        #
                                      ##################################    ##########################
    
 
    
    
# MATCH FORMAL PARAMS in calc



def calc(op, x, y):                   ##################################    ##########################
                                      #                                #    #                        #
    return op(x, y)                   #  Program Scope                 #    #  calc scope            #
        #  --------                   #                                #    #                        #
#          return add                 #                                #    #                        #
#          Just replace each          #                                #    #                        #                                            
#          param with its value       #                                #    #                        #
                                      #                                #    #                        # 
def add(a, b):                        #              ------------      #    #        -----------     #
                                      #  calc       |  function  |     #    #  op   |   add    |     #
    return a + b                      #             |  object    |     #    #        ----------      #
                                      #             -------------      #    #                        #
def div(a, b):                        #                                #    #                        #
                                      #                                #    #                        #
    if b != 0:                        #              ------------      #    #        -----------     #
                                      #  add        |  functon  |      #    #  x    |    2     |     #          
        return a / b                  #             |  object   |      #    #       -----------      #
                                      #             -------------      #    #                        #
    print("Denom was 0.")             #                                #    #                        #
                                      #                                #    #                        #
                                      #              ------------      #    #        -----------     #
                                      #  div        |  function |      #    #  y    |    3     |     #
res = calc(add, 2, 3)                 #             |  object   |      #    #       -----------      #
    # ----                            #             ------------       #    #                        #
    # Function call                   #                                #    #                        #
                                      #                                #    #                        #
                                      #                                #    #                        #
                                      #  res                           #    #                        #
                                      #                                #    #                        #
                                      #                                #    #                        #    
                                      #                                #    #                        #
                                      ##################################    ########################## 
    
 
    
 
# MATCH FORMAL PARAMS in calc



def calc(op, x, y):                   ##################################    ##########################    ##########################
                                      #                                #    #                        #    #                        #
    return op(x, y)                   #  Program Scope                 #    #  calc scope            #    #  add scope             #
        #  --------                   #                                #    #                        #    #                        #
#          Function call in           #                                #    #                        #    #                        #
#          calc scope: add(2, 3)      #                                #    #                        #    #                        #                                           
#                                     #                                #    #                        #    #                        #
                                      #                                #    #                        #    #                        #
def add(a, b):                        #              ------------      #    #        -----------     #    #                        #
                                      #  calc       |  function  |     #    #  op   |   add    |     #    #                        #
    return a + b                      #             |  object    |     #    #        ----------      #    #                        #
                                      #             -------------      #    #                        #    #                        #
def div(a, b):                        #                                #    #                        #    #                        #
                                      #                                #    #                        #    #                        #
    if b != 0:                        #              ------------      #    #        -----------     #    #                        #
                                      #  add        |  functon  |      #    #  x    |    2     |     #    #                        #         
        return a / b                  #             |  object   |      #    #       -----------      #    #                        #
                                      #             -------------      #    #                        #    #                        #
    print("Denom was 0.")             #                                #    #                        #    #                        #
                                      #                                #    #                        #    #                        #
                                      #              ------------      #    #        -----------     #    #                        #
                                      #  div        |  function |      #    #  y    |    3     |     #    #                        #
res = calc(add, 2, 3)                 #             |  object   |      #    #       -----------      #    #                        #
                                      #             ------------       #    #                        #    #                        #
                                      #                                #    #                        #    #                        #
                                      #                                #    #                        #    #                        #
                                      #                                #    #                        #    #                        #
                                      #  res                           #    #                        #    #                        #
                                      #                                #    #                        #    #                        #
                                      #                                #    #                        #    #                        #   
                                      #                                #    #                        #    #                        #
                                      ##################################    ##########################    ########################## 
    
    
    

# MATCH FORMAL PARAMS in calc



def calc(op, x, y):                   ##################################    ##########################    ##########################
                                      #                                #    #                        #    #                        #
    return op(x, y)                   #  Program Scope                 #    #  calc scope            #    #  add scope             #
        #  --------                   #                                #    #                        #    #                        #
#          Function call in           #                                #    #                        #    #                        #
#          calc scope: add with       #                                #    #                        #    #                        #                                           
#          formal params a = 2        #                                #    #                        #    #                        #
#          and b = 3                  #                                #    #                        #    #                        #
                                      #                                #    #                        #    #                        #
def add(a, b):                        #              ------------      #    #        -----------     #    #        ----------      #
                                      #  calc       |  function  |     #    #  op   |   add    |     #    #  a    |    2     |     #
    return a + b                      #             |  object    |     #    #        ----------      #    #       -----------      #
                                      #             -------------      #    #                        #    #                        #
def div(a, b):                        #                                #    #                        #    #                        #
                                      #                                #    #                        #    #                        #
    if b != 0:                        #              ------------      #    #        -----------     #    #        ----------      #
                                      #  add        |  functon  |      #    #  x    |    2     |     #    #  b    |    3     |     #         
        return a / b                  #             |  object   |      #    #       -----------      #    #       -----------      #
                                      #             -------------      #    #                        #    #                        #
    print("Denom was 0.")             #                                #    #                        #    #                        #
                                      #                                #    #                        #    #                        #
                                      #              ------------      #    #        -----------     #    #                        #
                                      #  div        |  function |      #    #  y    |    3     |     #    #                        #
res = calc(add, 2, 3)                 #             |  object   |      #    #       -----------      #    #                        #
                                      #             ------------       #    #                        #    #                        #
                                      #                                #    #                        #    #                        #
                                      #                                #    #                        #    #                        #
                                      #                                #    #                        #    #                        #
                                      #  res                           #    #                        #    #                        #
                                      #                                #    #                        #    #                        #
                                      #                                #    #                        #    #                        #   
                                      #                                #    #                        #    #                        #
                                      ##################################    ##########################    ##########################     
    



# EXECUTE LINE OF add



def calc(op, x, y):                   ##################################    ##########################    ##########################
                                      #                                #    #                        #    #                        #
    return op(x, y)                   #  Program Scope                 #    #  calc scope            #    #  add scope             #
                                      #                                #    #                        #    #                        # 
                                      #                                #    #                        #    #                        #
def add(a, b):                        #              ------------      #    #        -----------     #    #        ----------      #
                                      #  calc       |  function  |     #    #  op   |   add    |     #    #  a    |    2     |     #
    return a + b                      #             |  object    |     #    #        ----------      #    #       -----------      #
  # ------------                      #             -------------      #    #                        #    #                        #
                                      #                                #    #                        #    #                        #
def div(a, b):                        #                                #    #                        #    #                        #
                                      #                                #    #                        #    #                        #
    if b != 0:                        #              ------------      #    #        -----------     #    #        ----------      #
                                      #  add        |  functon  |      #    #  x    |    2     |     #    #  b    |    3     |     #         
        return a / b                  #             |  object   |      #    #       -----------      #    #       -----------      #
                                      #             -------------      #    #                        #    #                        #
    print("Denom was 0.")             #                                #    #                        #    #             |          #
                                      #                                #    #                        #    #            |           #
                                      #              ------------      #    #        -----------     #    #           |            #
                                      #  div        |  function |      #    #  y    |    3     |     #    #          |             #
res = calc(add, 2, 3)                 #             |  object   |      #    #       -----------      #    #         |              #
                                      #             ------------       #    #                        #    #        |               #
                                      #                                #    #            ▲           #    #       |                #
                                      #                                #    #           |            #    #      |                 #
                                      #                                #    #          |             #    #     |                  #
                                      #  res                           #    #          --------------#----#-----                   #
                                      #                                #    #                        #    #           returns 5    #
                                      #                                #    #                        #    #                        #   
                                      #                                #    #                        #    #                        #
                                      ##################################    ##########################    ##########################  





# REPLACE FUNC CALL WITH RETURN



def calc(op, x, y):                   ##################################    ##########################    
                                      #                                #    #                        #    
    return op(x, y)                   #  Program Scope                 #    #  calc scope            #    
         # --------                   #                                #    #                        #    
         #    5                       #                                #    #                        #   
                                      #                                #    #                        #    
def add(a, b):                        #              ------------      #    #        -----------     #    
                                      #  calc       |  function  |     #    #  op   |   add    |     #    
    return a + b                      #             |  object    |     #    #        ----------      #    
                                      #             -------------      #    #                        #    
                                      #                                #    #                        #    
def div(a, b):                        #                                #    #                        #    
                                      #                                #    #                        #  
    if b != 0:                        #              ------------      #    #        -----------     #    
                                      #  add        |  functon  |      #    #  x    |    2     |     #             
        return a / b                  #             |  object   |      #    #       -----------      #    
                                      #             -------------      #    #                        #   
    print("Denom was 0.")             #                                #    #                        #    
                                      #                                #    #                        #    
                                      #              ------------      #    #        -----------     #    
                                      #  div        |  function |      #    #  y    |    3     |     #    
res = calc(add, 2, 3)                 #             |  object   |      #    #       -----------      #   
                                      #             ------------       #    #                        #    
                                      #                                #    #                        #    
                                      #                                #    #                        #    
                                      #                                #    #                        #   
                                      #  res                           #    #                        #   
                                      #                                #    #                        #    
                                      #                                #    #                        #     
                                      #                                #    #                        #   
                                      ##################################    ##########################   






# EXECUTE LINE OF calc



def calc(op, x, y):                   ##################################    ##########################    
                                      #                                #    #                        #    
    return op(x, y)                   #  Program Scope                 #    #  calc scope            #    
  # ---------------                   #                                #    #                        #    
                                      #                                #    #                        #   
                                      #                                #    #                        #    
def add(a, b):                        #              ------------      #    #        -----------     #    
                                      #  calc       |  function  |     #    #  op   |   add    |     #    
    return a + b                      #             |  object    |     #    #        ----------      #    
                                      #             -------------      #    #                        #    
                                      #                                #    #                        #    
def div(a, b):                        #                                #    #                        #    
                                      #                                #    #                        #  
    if b != 0:                        #              ------------      #    #        -----------     #    
                                      #  add        |  functon  |      #    #  x    |    2     |     #             
        return a / b                  #             |  object   |      #    #       -----------      #    
                                      #             -------------      #    #                        #   
    print("Denom was 0.")             #                                #    #                        #    
                                      #                                #    #                        #    
                                      #              ------------      #    #        -----------     #    
                                      #  div        |  function |      #    #  y    |    3     |     #    
res = calc(add, 2, 3)                 #             |  object   |      #    #       -----------      #   
                                      #             ------------       #    #            |           #    
                                      #                                #    #           |            #    
                                      #                                #    #          |             #    
                                      #                                #    #         |              #   
                                      #  res               ◀︎-----------#----#---------               #   
                                      #                                #    #                        #    
                                      #                                #    #     returns 5          #     
                                      #                                #    #                        #   
                                      ##################################    ########################## 




# REPLACE FUNC CALL WITH RETURN



def calc(op, x, y):                   ##################################      
                                      #                                #     
    return op(x, y)                   #  Program Scope                 #    
                                      #                                #     
                                      #                                #    
                                      #                                #      
def add(a, b):                        #              ------------      #      
                                      #  calc       |  function  |     #       
    return a + b                      #             |  object    |     #      
                                      #             -------------      #       
                                      #                                #        
def div(a, b):                        #                                #       
                                      #                                #   
    if b != 0:                        #              ------------      #        
                                      #  add        |  functon  |      #                
        return a / b                  #             |  object   |      #       
                                      #             -------------      #      
    print("Denom was 0.")             #                                #       
                                      #                                #      
                                      #              ------------      #        
                                      #  div        |  function |      #      
res = calc(add, 2, 3)                 #             |  object   |      #     
    # ---------------                 #             ------------       #       
    #      5                          #                                #       
                                      #                                #       
                                      #             -------------      #      
                                      #  res       |     5      |      # 
                                      #             -------------      #       
                                      #                                #        
                                      #                                #      
                                      ##################################    




print("---------------------------")



# YOU TRY IT!


# Do a similar trace with the function call

def calc(op, x, y):
    
    return op(x, y)


def div(a, b):
    
    if b != 0:
        
        return a / b
    
    print("Denom was 0.")
    

res = calc(div, 2, 0)
# res = calc(div, 22, 7)

print(res)


# ANOTHER EXAMPLE: FUNCTIONS AS PARAMS


def func_a():
    
    print("inside func_a")
    

def func_b(y):

    print("insde func_b")

    return y


def func_c(f, z):
    
    print("inside func_c")
    
    return f(z)


print("-----------------------------")


print(func_a())
   #  --------
   #  call func_a, takes no parameters 



print(5 + func_b(2))
        # ---------
        # call func_b, takes one parameter, an int
        
        
print(func_c(func_b, 3)) 
    # -----------------
    #  call func_c, takes two parameters another
    # function and an int
   
    
    
# FUNCTIONS AS PARAMETERS 

                                                                               #  No bindings
                                                                               # (no parameters)        
   
   
                                       #############################     ############################### 
                                       #                           #     #                             #
def func_a():                          #                           #     #                             #                   
                                       #  Global scope             #     #  func_a scope               #
    print("inside func_a ")            #                           #     #                             #
                                       #                           #     #                             #
def func_b(y):                         #             ---------     #     #                             #
                                       #  func_a    |  Some  |     #     #                             #
    print("inside func_b")             #            |  code  |     #     #                             #
                                       #            ---------      #     ###############################
    return y                           #                           #     
                                       #                           #    
def func_c(f, z):                      #             --------      #    
                                       #  func_b    |  Some  |     #     
    print("inside func_c")             #            |  code  |     #         
                                       #            ---------      #     
    return f(z)                        #                           #     
                                       #                           #    
# ----->                               #             ---------     #   
print(func_a())                        #  func_c    |  some  |     #    
#     -------                          #            |  code  |     #    
# ---->                                #            ----------     #    
                                       #                           #     
print(5 + func_b(2))                   #                           #   
                                       #                           #     
print(func_c(func_b, 3))               #############################       



# FUNCTIONS AS PARAMETERS



                                                                               #  body prints inside
                                                                               #  "func_a" on console        
   
   
                                       #############################     ############################### 
                                       #                           #     #                             #
def func_a():                          #                           #     #                             #                   
                                       #  Global scope             #     #  func_a scope               #
    print("inside func_a ")            #                           #     #                             #
                                       #                           #     #                             #
def func_b(y):                         #             ---------     #     #                     |       #
                                       #  func_a    |  Some  |     #     #                    |        #
    print("inside func_b")             #            |  code  |     #     #                   |         #
                                       #            ---------      #     ###################|###########
    return y                           #                           #                       |
                                       #                           #                      |      
def func_c(f, z):                      #             --------      #                     |
                                       #  func_b    |  Some  |     #                    |
    print("inside func_c")             #            |  code  |     #                   | 
                                       #            ---------      #                  |
    return f(z)                        #                           #                 |
                                       #                           #                |
                                       #             ---------     #               |
print(func_a())                        #  func_c    |  some  |     #              | 
                                       #            |  code  |     #             |
                                       #            ----------     #            |
                                       #                           #           | 
# ---->                                #                           #          |      
print(5 + func_b(2))                   #             ---------     #         |
                                       #            |  None  | ◀︎---#---------
                                       #            ---------      # 
print(func_c(func_b, 3))               #                           #        * no return, so returns None  
                                       #                           #
                                       #                           #
                                       #                           #
                                       #                           #
                                       #                           #     
                                       ############################# 





# FUNCTIONS AS PARAMETERS

                                                                             
   
   
                                       #############################  
                                       #                           #     
def func_a():                          #                           #                     
                                       #  Global scope             #     
    print("inside func_a ")            #                           #    
                                       #                           #     
def func_b(y):                         #             ---------     #     
                                       #  func_a    |  Some  |     #     
    print("inside func_b")             #            |  code  |     #     
                                       #            ---------      #     
    return y                           #                           #                       
                                       #                           #                            
def func_c(f, z):                      #             --------      #                     
                                       #  func_b    |  Some  |     #                    
    print("inside func_c")             #            |  code  |     #                    
                                       #            ---------      #                  
    return f(z)                        #                           #                 
                                       #                           #                
                                       #             ---------     #               
print(func_a())                        #  func_c    |  some  |     #               
# ---->                                #            |  code  |     #    print displays None         
                                       #            ----------     #    on console        
                                       #                           #                           
print(5 + func_b(2))                   #                           #         
                                       #                           #
                                       #                           # 
print(func_c(func_b, 3))               #                           #          
                                       #                           #          
                                       #                           #
                                       #                           #
                                       #                           #
                                       #                           #     
                                       ############################# 





# FUNCTIONS AS PARAMETERS


       
   
   
                                       #############################     ############################### 
                                       #                           #     #                             #
def func_a():                          #                           #     #                             #                   
                                       #  Global scope             #     #  func_b scope               #
    print("inside func_a ")            #                           #     #                             #
                                       #                           #     #             -----------     #
def func_b(y):                         #             ---------     #     #      y     |     2     |    #
                                       #  func_a    |  Some  |     #     #            ------------     #
    print("inside func_b")             #            |  code  |     #     #                   |         #
                                       #            ---------      #     ###################|###########
    return y                           #                           #                       |
                                       #                           #                      |      
def func_c(f, z):                      #             --------      #                     |
                                       #  func_b    |  Some  |     #                    |
    print("inside func_c")             #            |  code  |     #                   | 
                                       #            ---------      #                  |
    return f(z)                        #                           #                 |
                                       #                           #                |
                                       #             ---------     #               |
print(func_a())                        #  func_c    |  some  |     #              | 
                                       #            |  code  |     #             |
                                       #            ----------     #            |
                                       #                           #           | 
                                       #                           #          |      
                                       #             ---------     #         |
#                 ---------------      #            |  None  |     #        |
#                |              |      #            ---------      #       |
#                ▼              |      #                           #      |  
print(5 + func_b(2))        #    ------#---------------------------#------                     
# ---->                                #                           #
                                       #                           #
print(func_c(func_b, 3))               #                           #
                                       #                           #     
                                       ############################# 

    
    
    
    
       
# FUNCTIONS AS PARAMETERS


                                                                                 # body prints    
                                                                                 # "inside func_b"
                                                                                 # on console
   
   
                                       #############################     ############################### 
                                       #                           #     #                             #
def func_a():                          #                           #     #                             #                   
                                       #  Global scope             #     #  func_b scope               #
    print("inside func_a ")            #                           #     #                             #
                                       #                           #     #             -----------     #
def func_b(y):                         #             ---------     #     #      y     |     2     |    #
                                       #  func_a    |  Some  |     #     #            ------------     #
    print("inside func_b")             #            |  code  |     #     #                             #
  # ----------------------             #            ---------      #     ###############################
    return y                           #                           #                        
                                       #                           #                            
def func_c(f, z):                      #             --------      #                     
                                       #  func_b    |  Some  |     #                    
    print("inside func_c")             #            |  code  |     #                    
                                       #            ---------      #                  
    return f(z)                        #                           #                 
                                       #                           #                
                                       #             ---------     #               
print(func_a())                        #  func_c    |  some  |     #              
                                       #            |  code  |     #             
                                       #            ----------     #            
                                       #                           #           
                                       #                           #                
                                       #             ---------     #         
                                       #            |  None  |     #        
                                       #            ---------      #       
                                       #                           #        
print(5 + func_b(2))                   #                           #                    
# ---->                                #                           #
                                       #                           #
print(func_c(func_b, 3))               #                           #
                                       #                           #     
                                       #############################     
    
    
    
    

# FUNCTIONS AS PARAMETERS


                                                                                 # value of 2    
                                                                                 # is returned and
                                                                                 # added to 5
   
   
                                       #############################     ############################### 
                                       #                           #     #                             #
def func_a():                          #                           #     #                             #                   
                                       #  Global scope             #     #  func_b scope               #
    print("inside func_a ")            #                           #     #                             #
                                       #                           #     #             -----------     #
def func_b(y):                         #             ---------     #     #      y     |     2     |    #
                                       #  func_a    |  Some  |     #     #            ------|-----     #
    print("inside func_b")             #            |  code  |     #     #                  |          #
                                       #            ---------      #     ###################|###########
    return y                           #                           #                        |
  # --------                           #                           #                        |    
def func_c(f, z):                      #             --------      #                        |
                                       #  func_b    |  Some  |     #                        |         
    print("inside func_c")             #            |  code  |     #                        |            
                                       #            ---------      #                        |              
    return f(z)                        #                           #                        |           
                                       #                           #                        |             
                                       #             ---------     #                        |             
print(func_a())                        #  func_c    |  some  |     #                        |             
                                       #            |  code  |     #                        |            
                                       #            ----------     #                        |           
                                       #                           #                        |
                                       #                           #                        |   
                                       #                           #                        |
                                       #             ---------     #                        |
                                       #            |  None  |     #                        |
                                       #            ---------      #                        | 
                                       #                           #                        |
print(5 + func_b(2))                   #                           #                        |       
    # -------------                    #                           #                        |
# ---->                                #            ---------      #                        | 
                                       #           |    7    | ◀︎---#------------------------
                                       #            ---------      #                     
                                       #                           #                      return 2
                                       #                           #
                                       #                           #
                                       #                           #
print(func_c(func_b, 3))               #                           #     
                                       #############################      
    
 
    
 
    
# FUNCTIONS AS PARAMETERS


                                                                                   
                                                                          
                                                                               
   
   
                                       #############################   
                                       #                           #    
def func_a():                          #                           #                   
                                       #  Global scope             #   
    print("inside func_a ")            #                           #    
                                       #                           #    
def func_b(y):                         #             ---------     #    
                                       #  func_a    |  Some  |     #     
    print("inside func_b")             #            |  code  |     #     
                                       #            ---------      #   
    return y                           #                           #                        
  # --------                           #                           #                            
def func_c(f, z):                      #             --------      #                        
                                       #  func_b    |  Some  |     #                                
    print("inside func_c")             #            |  code  |     #                                    
                                       #            ---------      #                                      
    return f(z)                        #                           #                                  
                                       #                           #                                   
                                       #             ---------     #                                    
print(func_a())                        #  func_c    |  some  |     #                                     
                                       #            |  code  |     #                                   
                                       #            ----------     #                                   
                                       #                           #                        
                                       #                           #                           
                                       #                           #                        
                                       #             ---------     #                        
                                       #            |  None  |     #                        
                                       #            ---------      #                        
                                       #                           #                        
print(5 + func_b(2))                   #                           #                               
# ------------------                   #                           #                        
# ---->                                #            ---------      #                         
                                       #           |    7    |     #    print displays 7
                                       #            ---------      #    on console                 
                                       #                           #            
                                       #                           #
                                       #                           #
                                       #                           #
print(func_c(func_b, 3))               #                           #     
                                       #############################      
    
    



# FUNCTIONS AS PARAMETERS


                                                                                 # body of func_c   
                                                                                 # prints "inside func_c"
                                                                                 # on console
   
   
                                       #############################     ############################### 
                                       #                           #     #                             #
def func_a():                          #                           #     #                             #                   
                                       #  Global scope             #     #  func_c scope               #
    print("inside func_a ")            #                           #     #                             #
                                       #                         --#-----#-----------------            #     
                                       #                        |  #     #                |            #
                                       #                        |  #     #           -----------       #
def func_b(y):                         #             ---------  |  #     #   f    ▶︎ |  func_b   |      #
                                       #  func_a    |  Some  |  |  #     #       |  ------------       #
    print("inside func_b")             #            |  code  |  |  #     #       |                     #
                                       #            ---------   |  #     #-      |                     #
                                       #                   -----   #     #       |                     # 
    return y                           #                  |        #     #       |   ------------      #
  # --------                           #                  ▼        #     #   z   |  |     3     |      #    
def func_c(f, z):                      #             --------      #     #       |   -----------       #
                                       #  func_b    |  Some  |     #     #       |          ▲          #
    print("inside func_c")             #            |  code  |     #     #       |          |          # 
 #  ----------------------             #            ---------      #     #       |          |          #   
    return f(z)                        #                           #     #       |          |          #                                
                                       #                           #     #       |          |          #                               
                                       #             ---------     #     ########|######################  
print(func_a())                        #  func_c    |  some  |     #             |          |             
                                       #            |  code  |     #             |          |            
                                       #            ----------     #             |          |           
                                       #                           #             |          |
                                       #                           #             |          |   
                                       #                           #             |          |
                                       #             ---------     #             |          |
                                       #            |  None  |     #             |          |
                                       #            ---------      #             |          | 
                                       #                           #             |          |
print(5 + func_b(2))                   #                           #             |          |       
    # -------------                    #                           #             |          |
# ---->                                #            ---------      #             |          | 
                                       #           |    7    |     #             |          |
                                       #            ---------      #             |          |
#                ----------------------#---------------------------#-------------           |                 
#               |     -----------------#---------------------------#-------------------------                 
#               |    |                 #                           #
#               |    |                 #                           #
print(func_c(func_b, 3))               #                           #     
                                       #############################     
    
    
    
              
    
    
    
  
    
  
    
# FUNCTIONS AS PARAMETERS

                                                                            # body of function_b
                                                                            # prints inside functon_b               
                                                                            # on console
                                                                            

                                       #############################    #################################   
                                       #                           #    #                               #  
def func_a():                          #                           #    #   func_scope                  #               
                                       #  Global scope             #    #                               # 
    print("inside func_a ")            #                           #    #                               #
                                       #                           #    #            -------------      #
def func_b(y):                         #             ---------     #    #  f        |   func_b   |      #
                                       #  func_a    |  Some  |     #    #           -------------       # 
    print("inside func_b")             #            |  code  |     #    #                               # 
                                       #            ---------      #    #                               #
    return y                           #                           #    #           --------------      #                    
                                       #                           #    #  z       |      3      | -----#------------------------------                             
def func_c(f, z):                      #             --------      #    #          --------------       #                              |
                                       #  func_b    |  Some  |     #    #                               #                              |
    print("inside func_c")             #            |  code  |     #    #                               #                              |  
                                       #            ---------      #    #           --------------      #                              |      
    return f(z)                        #                           #    #    ----▶︎ |      3      |      #                              |
         # ---                         #                           #    #   |      --------------       #                              | 
                                       #                           #    #   |                           #                              |
                                       #             ---------     #    #   |                           #                              |
print(func_a())                        #  func_c    |  some  |     #    #   |                           #                              |   
                                       #            |  code  |     #    #   |                           #                              |   
                                       #            ----------     #    #   |                           #                              |    
                                       #                           #    #   |                           #                              |
                                       #                           #    ####|############################                              |
                                       #                           #        |                                                          |
                                       #             ---------     #         -----                                                     |   
                                       #            |  None  |     #              |                                                    |
                                       #            ---------      #              |       ################################             |                     
                                       #                           #              |       #                              #             |
print(5 + func_b(2))                   #                           #              |       #                              #             |    
                                       #                           #              |       #  func_b scope                #             |
                                       #            ---------      #  return 3    |       #                              #             |
                                       #           |    7    |     #              |       #                              #             |
                                       #            ---------      #              |       #           -------------      #             |        
                                       #                           #              |       #  y       |      3     | ◀︎----#--------------
                                       #                           #              |       #          -------------       # 
                                       #                           #              |       #                |             # 
                                       #                           #              --------#-----------------             # 
print(func_c(func_b, 3))               #                           #                      #                              # 
# ---->                                #############################                      ################################     
    




    
    
# FUNCTIONS AS PARAMETERS

                                                                            # print displays
                                                                            # 3 on console              
                                                                            
                                                                            

                                       #############################    #################################   
                                       #                           #    #                               #  
def func_a():                          #                           #    #   func_scope                  #               
                                       #  Global scope             #    #                               # 
    print("inside func_a ")            #                           #    #                               #
                                       #                           #    #            -------------      #
def func_b(y):                         #             ---------     #    #  f        |   func_b   |      #
                                       #  func_a    |  Some  |     #    #           -------------       # 
    print("inside func_b")             #            |  code  |     #    #                               # 
                                       #            ---------      #    #                               #
    return y                           #                           #    #           --------------      #                    
                                       #                           #    #  z       |      3      |      #                             
def func_c(f, z):                      #             --------      #    #          --------------       #                              
                                       #  func_b    |  Some  |     #    #                               #                              
    print("inside func_c")             #            |  code  |     #    #                               #                                
                                       #            ---------      #    #           --------------      #                                    
    return f(z)                        #                           #    #    ----- |      3      |      #                              
         # ---                         #                           #    #   |      --------------       #                               
                                       #                           #    #   |                           #                              
                                       #             ---------     #    #   |                           #                              
print(func_a())                        #  func_c    |  some  |     #    #   |                           #                                 
                                       #            |  code  |     #    #   |                           #                                
                                       #            ----------     #    #   |                           #                                  
                                       #                           #    #   |                           #                              
                                       #                           #    ####|############################                              
                                       #                           #        |
                                       #             ---------     #        |    
                                       #            |  None  |     #        |    
                                       #            ---------      #        |                           
                                       #                           #        |      
print(5 + func_b(2))                   #                           #        |               
                                       #                           #        |          
                                       #            ---------      #        |
                                       #           |    7    |     #        |         
                                       #            ---------      #        |                 
                                       #                           #        |            
                                       #                           #        |    returns 3
                                       #                           #        |
                                       #                           #        |
                                       #            ----------     #        |
                                       #           |    3     | ◀︎--#--------
                                       #           ----------      # 
                                       #                           #
                                       #                           #              
                                       #                           #              
print(func_c(func_b, 3))               #                           #                     
# ----------------------               #############################    
# ------>



# YOU TRY IT!


# Write a function that meets these specs.


def apply(criteria,n):
    
    """
    * criteria is a func that takes in a number and returns a bool
    * n is an int
    Returns how many ints from 0 to n (inclusive) match
    the criteria (i.e. return True when run with criteria)
    """


# SUMMARY


# Functions are first class objects

# They have a type
# They can be assigned as a value bound to a name
# They can be used as an argument to another procedure
# They can be returned as a value from another procedure


# Have to be careful about environments

    # Main program runs in the global environment
    # Function calls each get a new temporary environment
    
    
# This enables the creation of concise, easily read code    
















    
    