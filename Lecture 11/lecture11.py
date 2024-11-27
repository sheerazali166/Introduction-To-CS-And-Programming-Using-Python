#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 08:06:54 2024

@author: sheeraz
"""

# ALIASING, CLONING

# MAKING A COPY OF THE LIST

# Can make a copy of a list object by duplicating all elements (top-level)
# into a new list object

# Lcopy = L[:]

# Equivalent to looping over L and appending each element to Lcopy

# This does not make a copy of elements that are lists (will see how to do
# this at the end of this lecture)

Loriginal = [4, 5, 6]

Lnew = Loriginal[:]


# Equivalent to looping over L and appending each element to Lcopy

# This does not make a copy of elements that are lists (will see how to do
# this at the end of this lecture)


Loriginal = [4, 5, 6]

Lnew = Loriginal[:]




        ###############                         ###############        
        #  Loriginal  #  ------------------>    #  4,  5,  6  # 
        ###############                         ###############
        
        
        
        
        ##########                              ###############
        #  Lnew  #  ----------------------->    #  4,  5,  6  #  
        ##########                              ###############   
        
        
        

# YOU TRY IT!

# Write a function that meets the specification.

# Hint. Make a copy to save the elements. The use L.clear() to empty out
# the list and repopulate it with the ones you’re keeping.



def remove_all(L, e):
    
    """
    L is a list
    Mutates L to remove all elements in L that are equal to e
    Returns None
    """        
        
        

# L = [1,2,2,2]
# remove_all(L, 2)
# print(L) # prints [1]        
        
# OPERATION ON LISTS: remove

# Delete element at a specific index with del(L[index]) 

# Remove element at end of list with L.pop(), returns the removed element
# (can also call with specific index: L.pop(3)) 


# Remove a specific element with L.remove(element)

    # Looks for the element and removes it (mutating the list)
    # If element occurs multiple times, removes first occurrence
    # If element not in list, gives an error
    

L = [2, 1, 3, 6, 3, 7, 0]  # do blow in order
  # -- 
  
#                                       ---
L.remove(2)  #  ---->  mutates L = [1, | 3 |, 6, 3, 7, 0]
#       ---                            ----

#                                       -----
L.remove(3)  #  ---->  mutates L = [1, | 6, | 3, 7, 0]
#       ---                            -----


del (L[1])

#
a = L.pop()  #  ---->  returns 0 and mutates L = [1, 3, 7]
#   ------- 


# EXERCISE WITH REMOVE INSTEAD OF COPY AND CLEAR


# Rewrite the code to remove eas long as we still had it in the list

# It works well!

def remove(L, e):
    
    """
    
    L is a list
    Mutates L to remove all elements in L that are equal to e 
    Returns None.
    
    """
    
    while e in L:
        
        L.remove(e)
        


# EXERCISE WITH REMOVE INSTEAD OF COPY AND CLEAR


# What if the code was this:
    
def remove_all(L, e):

    """
    L is a list
    Mutates L to remove all elements in L that are equal to e 
    Returns None.
    """ 
    
    for elem in L:
        
        if elem == e:
            
            L.remove(e)
            
 
L = [1, 2, 2, 2]

remove_all(L, 2)

print(L) # should print [1]

      
# Actually prints [1, 2]


# EXERCISE WITH REMOVE INSTEAD OF COPY AND CLEAR

def remove_all(L, e):
    
    """
    
    L is a list
    Mutates L to remove all elements in L that are equal to e
    Returns None.
    
    """

    for elem in L:
        
        if elem == e:
            
            L.remove(e)
            
            

L = [1, 2, 2, 2]

remove_all(L, 2)

print(L)  #  should print [1]





                ##########
                #  elem  #  -----------------
                ##########                  |
#                                           |
#                                           | 
#                                           |
#                                           |
#                                           |
#                                           ▼
        #######                         ##################
        #  L  #                         #  [1, 2, 2, 2]  #
        #######                         ##################


            
            



# EXERCISE WITH REMOVE INSTEAD OF COPY AND CLEAR            
            
def remove_all(L, e):
    
    """
    L is a list
    Mutates L to remove all elements in L that are equal to e 
    Returns None.
    """
    
    for elem in L:
        
        if elem == e:
            
            L.remove(e)
            


L = [1, 2, 2, 2]

remove_all(L, 2)

print(L)  #  # should print [1]



                ##########
                #  elem  #  -------------------
                ##########                     |
#                                              |
#                                              | 
#                                              |
#                                              |
#                                              |
#                                              ▼
        #######                         ##################
        #  L  #                         #  [1, 2, 2, 2]  #
        #######                         ##################





# EXERCISE WITH REMOVE INSTEAD OF COPY AND CLEAR


def remove_all(L, e):
    
    """
    L is a list
    Mutates L to remove all elements in L that are equal to e
    Returns None.
    """
    
    for elem in L:
        
        if elem == e:
      # -------------      
            L.remove(e)
          # -----------
          
          
      # Removes the 2, but doesn't shift the pointer back!
      
 
      
L = [1, 2, 2, 2]

remove_all(L, 2)

print(L)  # should print [1]



                ##########
                #  elem  #  -------------------
                ##########                     |
#                                              |
#                                              | 
#                                              |
#                                              |
#                                              |
#                                              ▼
        #######                         ###############
        #  L  #                         #  [1, 2, 2]  #
        #######                         ###############

 
    


# EXERCISE WITH REMOVE INSTEAD OF COPY AND CLEAR  


def remove_all(L, e):

    """
    L s a list
    Mutates L to remove all elements in L that are equal to e
    Returns None.
    """

    for elem in L:
  # --------------
  # elem moves forward in the 

        if elem == e:
            
            L.remove(e)
            


L = [1, 2, 2, 2]

remove_all(L, 2)

print(L)  #  should print [1]

 

                ##########
                #  elem  #  -----------------------
                ##########                        |
#                                                 |
#                                                 | 
#                                                 |
#                                                 |
#                                                 |
#                                                 ▼
        #######                         ###############
        #  L  #                         #  [1, 2, 2]  #
        #######                         ###############




# EXERCISE WITH REMOVE INSTEAD nOF COPY AND CLEAR
            

# It’s not correct! We removed items as we iterated over the list!


def remove_all(L, e):

    """
    L is a list
    Mutates L to remove all elements in L that are equal to e
    Return None.
    """    

    for elem in L:

        if elem == e:
      # ------------
            L.remove(e)
          # -----------
          # Remove the 2, and done
     
          
L = [1, 2, 2, 2]

remove_all(L, 2)

print(L)  # should print [1]

     


                ##########
                #  elem  #  -------------------------
                ##########                          |
#                                                   |
#                                                   | 
#                                                   |
#                                                   |
#                                                   |
#                                                   ▼
        #######                         ###################
        #  L  #                         #  [1, 2]         #
        #######                         ###################        
     
          
            
          
# Not what we wanted!
 
# in simple words for pure freedom you have to become extra ordinary specal
# person            

print((12 * 6))


# TRICKY EXAMPLES OVERVIEW 

# TRICKY EXAMPLE 1:
    
    # A loop iterates over indices of L and mutates L each time  (adds more
    # elements).    

# TRICKY EXAMPLE 2:
    
    # A loop iterates over L’s elements directly and mutates L each time 
    # (adds more elements).    

# TRICKY EXAMPLE 3:
    
    # A loop iterates over L’s elements directly but reassigns L to a new
    # object each time    

#############################################################################
#                                                                           #
#  TRICKY EXAMPLE 4                                                         #
#                                                                           #
#    A loop iterates over L’s elements directly and mutates L by removing   #
#    elements.                                                              #
#                                                                           #
#############################################################################



# TRICKY EXAMPLE 4

# PYTHON TUTOR LINK to see step-by-step

# Want to mutate L1 to remove any elements that are also in L2

def remove_dups(L1, L2):
    
    for e in L1:
        
        if e in L2:
            
           L1.remove(e) # ❌
                 
           

# Want a function that returns a list, where every element  also in a
# second list is removed.

L1 = [10, 20, 30, 40]

L2 = [10, 20, 50, 60]


remove_dups(L1, L2) 


# L1 is [20,30,40] not [30,40] Why?
# You are mutating a list as you are iterating over it
# Python uses an internal counter. Tracks of index in the loop over list L1
# Mutating changes the list but Python doesn’t update the counter
# Loop never sees element 20

# MUTATION AND ITERATION WITHOUT CLONE

def remove_dups(L1, L2):
    
    for e in L1:
        
        if e in L2:
            
            L1.remove(e)
            
        
            
L1 = [10, 20, 30, 40]
L2 = [10, 20, 50, 60]

remove_dups(L1, L2)




                     ########
                     #  e   #  -------------------
                     ########                    |
#                                                |
#                                                |
#                                                |
#                                                |
#                                                |
#                                                ▼       
    ########                                 ######################   
    #  L1  #    ---------------------->      #  [10, 20, 30, 40]  #   
    ########                                 ######################
    
    
    ########                                 ######################
    #  L2  #    ---------------------->      #  [10, 20, 50, 60]  #     
    ########                                 ######################




# MUTATION AND ITERATION WITHOUT CLONE

def remove_dups(L1, L2):
    
    for e in L1:
        
        if e in L2:
            
            L1.remove(e)
                 
            
L1 = [10, 20, 30, 40]

L2 = [10, 20, 50, 60]

remove_dups(L1, L2)       

     

                     ########
                     #  e   #  -------------------
                     ########                    |
#                                                |
#                                                |
#                                                |
#                                                |
#                                                |
#                                                ▼       
    ########                                 ######################   
    #  L1  #    ---------------------->      #  [20, 30, 40]      #   
    ########                                 ######################
    
    
    ########                                 ######################
    #  L2  #    ---------------------->      #  [10, 20, 50, 60]  #     
    ########                                 ######################



# MUTATION AND ITERATION WITHOUT CLONE


def remove_dups(L1, L2):
    
    for e in L1:
        
        if e in L2:
            
            L1.remove(e)
            
            

L1 = [10, 20, 30, 40]
L2 = [10, 20, 50, 60]
            
      
                     ########
                     #  e   #  ------------------------
                     ########                         |
#                                                     |
#                                                     |
#                                                     |
#                                                     |
#                                                     |
#                                                     ▼       
    ########                                 ######################   
    #  L1  #    ---------------------->      #  [20, 30, 40]      #   
    ########                                 ######################
    
    
    ########                                 ######################
    #  L2  #    ---------------------->      #  [10, 20, 50, 60]  #     
    ########                                 ######################           
            
            
            


# MUTATION AND ITERATION WITHOUT CLONE

def remove_dups(L1, L2):
    
    for e in L1:
        
        if e in L2:
            
            L1.remove(e)
            
            
            
L1 = [10, 20, 30, 40]

L2 = [10, 20, 50, 60]


remove_dups(L1, L2)             



                     ########
                     #  e   #  ---------------------------
                     ########                             |
#                                                         |
#                                                         |
#                                                         |
#                                                         |
#                                                         |
#                                                         ▼       
    ########                                 ######################   
    #  L1  #    ---------------------->      #  [20, 30, 40]      #   
    ########                                 ######################
    
    
    ########                                 ######################
    #  L2  #    ---------------------->      #  [10, 20, 50, 60]  #     
    ########                                 ###################### 


# MUTATION AND ITERATION WITH CLONE

L1_copy = L1[:]


# Make a clone with [:]


    
    #                                        #                                        #
    #                                        #                                        #
    #       def remove_dumps(L1, L2):        #       def remove_dumps(L1, L2):        #
    #                                        #                                        #
    #           for e in L1:                 #           L1_copy = L1[:]              #
    #                                        #                     -----              #      
    #               if e in L2:              #                                        #
    #                                        #           for e in L1_copy:            #
    #     ❌            L1.remove(e)         #                    --------            #
    #                                        #      ✅       if e in L2:              #
    #                                        #                   L1.remove(e)         #
    #                                        #                                        #





def remove_dups(L1, L2):
    
    for e in L1:
        
        if e in L2:
            
            L1.remove(e)
      
    print(L1)



def remove_dups_with_clone(L1, L2):
    
    L1_copy = L1[:]
    
    for e in L1_copy:
        
        if e in L2:
            
            L1.remove(e)
      
    print(L1)
    



L1 = [10, 20, 30, 40]

L2 = [10, 20, 50, 60]


remove_dups(L1, L2)

remove_dups_with_clone(L1, L2)


# New version works!

# Iterate over a copy

# Mutate original list, not the copy

# Indexing is now consistent


def remove_dups(L1, L2):
    
    L1_copy = L1[:]
    
    for e in L1_copy:
        
        if e in L2:
            
            L1.remove(e)
              
            
            
L1 = [10, 20, 30, 40]

L2 = [10, 20, 50, 60]


remove_dups(L1, L2)


                
                            #######
                            #  e  #  --------------------
                            #######                     | 
#                                                       |
#                                                       |
#                                                       |
#                                                       |
#                                                       |
#                                                       ▼
        #############                               ####################        
        #  L1_copy  #  ----------------------->     #  10, 20, 30, 40  #
        #############                               #################### 
        
        
        
        
            ########                                ####################
            #  L1  #   ------------------------>    #  10, 20, 30, 40  #
            ########                                ####################
            
            
            
            
            ########                                #################### 
            #  L2  #   ------------------------->   #  10, 20, 50, 60  #
            ########                                ####################
           



def remove_dups(L1, L2):
    
    L1_copy = L1[:]
    
    for e in L1_copy:
        
        if e in L2:
            
            L1.remove(e)
            
     
            
L1 = [10, 20, 30, 40]

L2 = [10, 20, 50, 60]

remove_dups(L1, L2)



                            #######
                            #  e  #  --------------------
                            #######                     | 
#                                                       |
#                                                       |
#                                                       |
#                                                       |
#                                                       |
#                                                       ▼
        #############                               ####################        
        #  L1_copy  #  ----------------------->     #  10, 20, 30, 40  #
        #############                               #################### 
        
        
        
        
            ########                                ####################
            #  L1  #   ------------------------>    #  20, 30, 40      #
            ########                                ####################
            
            
            
            
            ########                                #################### 
            #  L2  #   ------------------------->   #  10, 20, 50, 60  #
            ########                                ####################




def remove_dups(L1, L2):
    
    L1_copy = L1[:]

    for e in L1_copy:
        
        if e in L2:
            
            L1.remove(e)
            
            
L1 = [10, 20, 30, 40]            
L2 = [10, 20, 50, 60] 


remove_dups(L1, L2)           



            
                            #######
                            #  e  #  ------------------------
                            #######                         | 
#                                                           |
#                                                           |
#                                                           |
#                                                           |
#                                                           |
#                                                           ▼
        #############                               ####################        
        #  L1_copy  #  ----------------------->     #  10, 20, 30, 40  #
        #############                               #################### 
        
        
        
        
            ########                                ####################
            #  L1  #   ------------------------>    #  20, 30, 40      #
            ########                                ####################
            
            
            
            
            ########                                #################### 
            #  L2  #   ------------------------->   #  10, 20, 50, 60  #
            ########                                ####################



     

def remove_dups(L1, L2):

    L1_copy = L1[:]

    for e in L1_copy:

        if e in L2:

            L1.remove(e)


L1 = [10, 20, 30, 40]

L2 = [10, 20, 50, 60]

remove_dups(L1, L2)   


  
                            #######
                            #  e  #  ------------------------
                            #######                         | 
#                                                           |
#                                                           |
#                                                           |
#                                                           |
#                                                           |
#                                                           ▼
        #############                               ####################        
        #  L1_copy  #  ----------------------->     #  10, 20, 30, 40  #
        #############                               #################### 
        
        
        
        
            ########                                ####################
            #  L1  #   ------------------------>    #  30, 40         #
            ########                                ####################
            
            
            
            
            ########                                #################### 
            #  L2  #   ------------------------->   #  10, 20, 50, 60  #
            ########                                ####################       
            
            
            
            

def remove_dups(L1, L2):
    
    L1_copy = L1[:]
    
    for e in L1_copy:
        
        if e in L2:
            
            L1.remove(e)
            
            
            
L1 = [10, 20, 30, 40]

L2 = [10, 20, 50, 60]


remove_dups(L1, L2)



                            #######
                            #  e  #  ---------------------------
                            #######                             | 
#                                                               |
#                                                               |
#                                                               |
#                                                               |
#                                                               |
#                                                               ▼
        #############                               ####################        
        #  L1_copy  #  ----------------------->     #  10, 20, 30, 40  #
        #############                               #################### 
        
        
        
        
            ########                                ####################
            #  L1  #   ------------------------>    #  30, 40         #
            ########                                ####################
            
            
            
            
            ########                                #################### 
            #  L2  #   ------------------------->   #  10, 20, 50, 60  #
            ########                                ####################  


            

def remove_dups(L1, L2):
    
    L1_copy = L1[:]
    
    for e in L1_copy:
        
        if e in L2:
            
            L1.remove(e)
            
    print(L1)


L1 = [10, 20, 30, 40]

L2 = [10, 20, 50, 60]

remove_dups(L1, L2)




                            #######
                            #  e  #  ------------------------------
                            #######                                | 
#                                                                  |
#                                                                  |
#                                                                  |
#                                                                  |
#                                                                  |
#                                                                  ▼
        #############                               ####################        
        #  L1_copy  #  ----------------------->     #  10, 20, 30, 40  #
        #############                               #################### 
        
        
        
        
            ########                                ####################
            #  L1  #   ------------------------>    #  30, 40         #
            ########                                ####################
            
            
            
            
            ########                                #################### 
            #  L2  #   ------------------------->   #  10, 20, 50, 60  #
            ########                                #################### 




# ALIASING


# City may be known by many names

# Attributes of a city                                      Boston
#                                                           The Hub    
    # Small, tech-savvy                                     Beantown
#                                                           Athens of America     


# All nicknames point to the same city

    # Add new attribute to one nickname …

    

#      ------------------  
#     |   ############   |   ############    ################    ###########
#     |   #  Boston  #   |   #  small   #    #  tech-savvy  #    #  snowy  #
#     |   ############   |   ############    ################    ###########  
#     ------------------- 
    
 
# … all the aliases refer to the old attribute and all the new ones

  
#      --------------------  
#     |   #############   |   ############    ################    ###########
#     |   #  The hub  #   |   #  small   #    #  tech-savvy  #    #  snowy  #
#     |   #############   |   ############    ################    ###########  
#     -------------------- 


#      --------------------- 
#     |   ##############   |   ############    ################    ###########
#     |   #  Beantown  #   |   #  small   #    #  tech-savvy  #    #  snowy  #
#     |   ##############   |   ############    ################    ###########  
#     ---------------------   
    
    
 
# MUTATION AND ITERATION WITH ALIAS

# L1_copy = L1

# Assignment (= sign) on mutable obj creates an alias, not a clone


#                                          #                                          #
#                                          #                                          #
#    def remove_dups(L1, L2):              #    def remove_dups(L1, L2):              #
#                                          #                                          #
#                   -----                  #                   --------               # 
#        L1_copy = | L1 |                  #        L1_copy = | L1[:] |               #   
#                  ------                  #                  ---------               #   
#                 ----------               #                 ----------               #
#   ❌  for e in | L1_copy |:              #   ✅  for e in | L1_copy |:             # 
#                ----------                #                -----------               #
#                The same object as L1     #                                          # 
#                                          #            if e in L2:                   #
#            if e in L2:                   #                L1.remove(e)              #
#                                          #                                          #
#                L1.remove(e)              #                                          #
#                                          #                                          #
#                                          #                                          #

L1 = [10, 20, 30, 40]

L2 = [10, 20, 50, 60]




# Note that L1_copy = L1 does NOT clone 

remove_dups(L1, L2) 

# Using a simple assignment without making a copy

    # Makes an alias for list (same list object referenced by another name)
    # It’s like iterating over L itself, it doesn’t work!
    
    


def remove_dups(L1, L2):
    
    L1_copy = L1
    
    for e in L1_copy:
           # --------
           # The same object as L1
           
           if e in L2:
               
               L1.remove(e)
               
    print(L1)

            
               

L1 = [10, 20, 30, 40]

L2 = [10, 20, 50, 60]




# Note that L1_copy = L1 does NOT clone 

remove_dups(L1, L2)    
    

def remove_dups(L1, L2):
    
    L1_copy = L1[:]
            # -----
            
    for e in L1_copy:
          #  --------
          
        if e in L2:
            
            L1.remove(e)
            
    print(L1)
        
            
            
L1 = [10, 20, 30, 40]

L2 = [10, 20, 50, 60]


# Note that L1_copy = L1 does NOT clone        
 
remove_dups(L1, L2)       
    
    
def remove_dups(L1, L2):

    L1_copy = L1

    for e in L1_copy:
        
        if e in L2:
            
            L1.remove(e)
            

L1 = [10, 20, 30, 40]

L2 = [10, 20, 50, 60]

remove_dups(L1, L2)            
    
    
    
    
                        #######
                        #  e  #  ---------------------       
                        #######              |   |   | 
#                                            |   |   |
#                                            |   |   |
#                                            |   |   |
#                                            |   |   |
#                                            |   |   | 
    #############                            |   |   |
    #  L1_copy  # -----------                |   |   |                       
    #############           |                |   |   |
#                           |                |   |   |    
#                           |                ▼   ▼   ▼  
    ########                ---------▶︎  ##################                             
    #  L1  #  ---------------------▶︎    #  [20, 30, 40]  #
    ########                            ##################
    
    
    ########                            ###################### 
    #  L1  #  ----------------------▶︎   #  [10, 20, 50, 60]  #
    ########                            ######################                        
    
    
            

# BIG IDEA

# When you pass a list as a parameter to a function, you are making an alias.            
    
        
# The actual parameter (from the function call) is an alias for 
  
# the formal parameter (from the function definition).


def remove_dups(L1, L2):
              # --  --
              # Alas Alas
              # for  for
              # La   Lb
              
    L1_copy = L1
    
    for e in L1_copy:
        
        if e in L2:
            
            L1.remove(e)
            
  
La = [10, 20, 30, 40]

Lb = [10, 20, 50, 60]

remove_dups(La, Lb)

print(La)
    # ---
    # L1 was mutated, but it's an alias for La





                #######                       
                #  e  #  -----------------------------------
                #######                            |   |   |
#                                                  |   |   |
#                                                  |   |   |
#                                                  |   |   |
    #############                                  |   |   |
    #  L1_copy  #  ------------------              |   |   |
    #############                   |              |   |   |
#                                   |              |   |   |
#                                   |              |   |   |
#                                   |              |   |   |
#                                   |              |   |   |
    ########                        |              |   |   |
    #  La  #  -----------           |              |   |   |
    ########            |           |              |   |   | 
#                       |           |              ▼   ▼   ▼                 
#                       |            ------▶︎  ##################
#                        -----------------▶︎   #  [20, 30, 40]  #
#                                   ------▶︎   ##################
#                                  |  
    ########                       |
    #  L1  #  ---------------------
    ########
    
    
    
    
    
    ########
    #  Lb  #  -----------------
    ########                  |
#                             |
#                             |               ##################
#                             ------------▶︎   #  [20, 30, 40]  #
#                              -----------▶︎   ##################
#                             |
    ########                  |
    #  L2  #  ----------------
    ########
    
    
    
    
print("-----------------")
    
    
    
  
# ALIASES, SHALLOW COPIES, AND DEEP COPIES WITH MUTABLE ELEMENTS    
   

# CONTROL COPYING

# Assignment just creates a new pointer to same object

old_list = [[1, 2], [3, 4], [5, "foo"]]
# -------------------------------------

new_list = old_list
# -----------------
# Assignment creates an alias for an existing data structure


print(old_list)
print(new_list)


new_list[2][1] = 6
# ----------------

print("New list:", new_list)  #  New list: [[1, 2], [3, 4], [5, 6]]
# --------------------------

print("Old list:", old_list)  # old list: [[1, 2], [3, 4], [5, 6]] 
# --------------------------


# So mutating one object changes the other


                                            
#                           -------------▶︎  #######################
#                          |       ------▶︎  #  [  ,   ,  ]        #    
#                          |      |         #######################
#                          |      |             |   |  |
#                          |      |             |   |   ---------------------------
#                          |      |             |   |                             |
#                          |      |             |   --------------                |
#                          |      |              ----            |                |
#                          |      |                 |            |                ▼
    ##############         |      |                 |            | 
    #  old_list  # --------       |                 ▼            ▼              ----- 
    ##############                |         ############  ############  #######|####|##          
#                                 |         #  [1, 2]  #  #  [3, 4]  #  #  [5, | 6] | #
#                                 |         ############  ############  #######|####|##  
#                                 |                                            -----
    ##############                |
    #  new_list  #  --------------
    ##############


# CONTROL COPYING


# Suppose we want to create a copy of a list, not just a shared pointer

# Shallow copying does this at the top level of the list

    # Equivalent to syntax [:]
    # Any mutable elements are NOT copied


# Use this when your list contains immutable objects only

import copy

old_list = [[1, 2], [3, 4], [5, 6]]

new_list = copy.copy(old_list)


print("New list:", new_list)
print("Old list:", old_list)


old_lst = [[1, 2], [3, 4], [5, 6]]
# --------------------------------


new_list = copy.copy(old_list)
# ----------------------------  


# Copy creates a new data structure, but actual elements are shared

print("New List:", new_list)  #  New List: [[1, 2], [3, 4], [5, 6]] 
# --------------------------

print("Old list:", old_list)  #  Old list: [[1, 2], [3, 4], [5, 6]]




#                           -------------▶︎  #######################
#                          |                #  [  ,   ,  ]        #    
#                          |                #######################
#                          |                    |   |  |
#                          |                    |   |   ------------------------
#                          |                    |   |                           |
#                          |                    |   --------------              |
#                          |                     ----            |              |
#                          |                        |            |              | 
    ##############         |                        |            |              |
    #  old_list  # --------                         ▼            ▼              ▼ 
    ##############                          ############  ############  #############          
#                                           #  [1, 2]  #  #  [3, 4]  #  #  [5,  6]  #
#                                           ############  ############  #############  
#                                                ▲             ▲              ▲  
    ##############                               |             |              |
    #  new_list  #  --------------               |   ----------               | 
    ##############               |               |  |                         | 
#                                |               |  |    ----------------------
#                                |               |  |   |
#                                |          #######################
#                                  ------▶︎  #  [  ,   ,  ]        #    
#                                           #######################




# CONTROL COPYING

# Now we mutate the top level structure

import copy

old_list = [[1, 2], [3, 4], [5, 6]]

new_list = copy.copy(old_list)


old_list.append([7, 8])

print("New list:", new_list)

print("Old list:", old_list)


old_list = [[1, 2], [3, 4], [5, 6]]
# ---------------------------------


new_list = copy.copy(old_list) 
# ----------------------------

# Copy creates a new data structure with shared elements, so mutating top
# level structure of one does not affect the clone 

old_list.append([7, 8])

print("New list:", new_list)  #  New list: [[1, 2], [3, 4], [5, 6]]

print("Old list:", old_list)  #  Old list: [[1, 2], [3, 4],[5, 6],[7, 8]]




                                                #######################
#                              ------------▶︎    #  [  ,  ,  ,  ]      #  
#                             |                 #######################
#                             |                     |  |  |  | 
#                             |                     |  |  |  ----------------------------
#                             |                     |  |  |                             |
#                             |                     |  |  ------------------            |
    ##############            |                  ---    -----              |            |
    #  old_list  # ------------                 |           |              |            | 
    ##############                              ▼           ▼              ▼            ▼
                                         ############  ############  ############  ############       
                                         #  [1, 2]  #  #  [3, 4]  #  #  [5, 6]  #  #  [7, 8]  #
#                                        ############  ############  ############  ############ 
#                                             ▲             ▲             ▲
#                                             |             |             |
    ##############                            |             |             |
    #  new_list  #  ------------              --------   ----             |
    ##############             |                     |  |   --------------               
#                              |                     |  |  |
#                              |                #######################
#                               ------------▶︎   #  [  ,  ,  ]         #  
                                                #######################




# CONTROL COPYING

# But if we change an element in one of the sub-structures, they are shared!

# If your elements are not mutable then this is not a problem


import copy

old_list = [[1, 2], [3, 4], [5, 6]]

new_list = copy.copy(old_list)

old_list.append([7, 8])

old_list[1][1] = 9

print("New list:", new_list)

print("Old list:", old_list)


old_list = [[1, 2], [3, 4], [5, 6]]
# ---------------------------------

new_list = copy.copy(old_list)
# ----------------------------

# Shalllow copying creates a new data structure with shared elements;
# so top level are clones, but elements are aliases; mutating an element
# will thus affect the other object

old_list.append([7, 8])

old_list[1][1] = 9


#                                              ---
print("New list:", new_list)  #  [[1, 2], [3, | 9 |], [5, 6]]
print("Old list:", old_list)  #  [[1, 2], [3, | 9 |], [5, 6], [7, 8]]
#                                              ---




                                                #######################
#                              ------------▶︎    #  [  ,  ,  ,  ]      #  
#                             |                 #######################
#                             |                     |  |  |  | 
#                             |                     |  |  |  ---------------------------------
#                             |                     |  |  |                                  |
#                             |                     |  |  ---------------------              |
    ##############            |                  ---    ---------              |             |
    #  old_list  # ------------                 |               |              |             | 
    ##############                              |               ▼              |             |
#                                               ▼              ----            ▼             ▼
                                         ############  #######|####|###  ############  ############       
                                         #  [1, 2]  #  #  [3, | 9] |  #  #  [5, 6]  #  #  [7, 8]  #
#                                        ############  #######|####|###  ############  ############ 
#                                             ▲             ▲  ----       ▲
#                                             |             |             |
    ##############                            |             |             |
    #  new_list  #  ------------              --------   ----             |
    ##############             |                     |  |   --------------               
#                              |                     |  |  |
#                              |                #######################
#                               ------------▶︎   #  [  ,  ,  ]         #  
                                                #######################



# CONTROL COPYING

# If we want all structures to be new copies, we need a deep copy

# Use deep copy when your list might have mutable elements to ensure every
# structure at every level is copied

import copy

old_list = [[1, 2], [3, 4], [5, 6]]

new_list = copy.deepcopy(old_list)
         # -----------------------

old_list.append([7, 8])

old_list[1][1] = 9

print("New li:st", new_list)

print("Old list:", old_list)


old_list = [[1, 2], [3, 4], [5, 6]]

new_list = copy.deepcopy(old_list)
# --------------------------------
# Deep copying creates clones at all levels of structure; thus mutating
# one does not affect the other at any level

old_list.append([7, 8])
# ---------------------

old_list[1][1] = 9
# ----------------

print("New list:", new_list)  # [[1, 2],[3, 4],[5, 6]]
# --------------------------

print("old list:", old_list)  #  [[1, 2], [3, 9], [5, 6], [7, ]]
# -------------------------


 
                                                #######################
#                              ------------▶︎    #  [  ,  ,  ,  ]      #  
#                             |                 #######################
#                             |                     |  |  |  | 
#                             |                     |  |  |  ---------------------------------
#                             |                     |  |  |                                  |
#                             |                     |  |  ---------------------              |
    ##############            |                  ---    ---------              |             |
    #  old_list  # ------------                 |               |              |             | 
    ##############                              |               ▼              |             |
#                                               ▼              ----            ▼             ▼
                                         ############  #######|####|###  ############  ############       
                                         #  [1, 2]  #  #  [3, | 9] |  #  #  [5, 6]  #  #  [7, 8]  #
#                                        ############  #######|####|###  ############  ############ 
#                                                              ----  

                                         ############  ##############  ############       
                                         #  [1, 2]  #  #  [3,  4]   #  #  [5, 6]  #  
#                                        ############  ##############  ############ 

#                                              ▲             ▲              ▲
#                                              |             |              |
    ##############                             |             |              |
    #  new_list  #  ------------               -------   -----              |
    ##############             |                     |  |  -----------------               
#                              |                     |  |  |
#                              |                #######################
#                               ------------▶︎   #  [  ,  ,  ]         #  
                                                #######################



# LISTS in MEMORY


# Separate the idea of the object vs. the name we give an object

# Variable name points to object

# Lists are mutable and behave differently than immutable types

# Using equal sign between mutable objects creates aliases

# Both variables point to the same object in memory

# Any variable pointing to that object is affected by mutation of object,
# even if mutation is by referencing another name

# If you want a copy, you explicitly tell Python to make a copy

# Key phrase to keep in mind when working with lists is side effects,
# especially when dealing with aliases– two names pointing to the same 
# structure in memory

# Python Tutor is your best friend to help sort this out!

# http://www.pythontutor.com/

# WHY LISTS and TUPLES?

# If mutation can cause so many problems, why do we even want to have lists,
# why not just use tuples?


# Efficiency – if processing very large sequences, don’t want to have to copy
# every time we change an element

# If lists basically do everything that tuples do, why not just have lists?

# Immutable structures can be very valuable in context of other object types

# Don’t want to accidentally have other code mutate some important data,
# tuples safeguard against this

# They can be a bit faster

# AT HOME TRACING EXAMPLES SHOWCASING ALIASING AND CLONING


# ALIASES

# hotis an alias for warm– changing one changes the other!

# append()has a side effect

a = 1

b = 1

print(a)

print(b)

warm = ["red", "orange", "yellow"]

hot = "warm"


# ALIASES

# hotis an alias for warm– changing one changes the other!

# append()has a side effect

a = 1

b = a

print(a)
print(b)

warm = ["red", "yellow", "orange"]

hot = warm

hot.append("pink")
print(hot)
print(warm)


    #############################################
    #                                           #
    #  1                                        #
    #  1                                        #
    #                                           #
    #  ["red", "yellow", "orange", "pink"]      #
    #  ["red", "yellow", "orange", "pink"]      #
    #                                           #
    #############################################
    
    
    
# CLONING A LIST

# Create a new list and copy every element using a clone

# chill = cool[:]

    

    #############################################
    #                                           #
    #  cool = ["blue", "green", "grey"]         #
    #                                           #
    #############################################
    
    
    
# CLONING A LIST

# Create a new list and copy every element using a clone

# chill = cool[:]

cool = ["blue", "green", "grey"]

chill = cool[:]

chill.append("black")

print(chill)

print(cool)

 

    #############################################
    #                                           #
    #                                           #
    #                                           #
    #############################################


# CLONING A LIST

# Create a new list and copy every element using a clone

cool = ["blue", "green", "grey"]

chill = cool[:]

chill.append("black")

print(chill)
print(cool)


    #############################################
    #                             ----------    #
    #  ["blue", "green", "grey", | "black" |]   #
    #  ["blue", "green", "grey"] ----------     #
    ############################################# 




# Because chill is a clone, changing chill does not change cool 


# LISTS OF LISTS OF LISTS OF….

# Can have nested lists

# possible after mutation


    #############################################
    #                                           #
    #                                           #
    #                                           #
    #############################################
    

warm = ["yellow", "orange"]

hot = ["red"]

brightcolors = [warm]

brightcolors.append(hot)

print(brightcolors)


# LISTS OF LISTS OF LISTS OF….


# Can have nested lists

# Side effects still

# possible after mutation


    #############################################
    #                                           #
    #                                           #
    #                                           #
    #############################################
    
    
    
    
warm = ["yellow", "orange"]

hot = ["red"]

brightcolors = [warm]

brightcolors.append(hot)

print(brightcolors)


# LISTS OF LISTS OF LISTS OF….

# Can have nested lists

# Side effects still possible after mutation


    #############################################
    #                                           #
    #                                           #
    #                                           #
    #############################################
    
   
    
warm = ["yellow", "orange"]

hot = ["red"]

brightcolors = [warm]

brightcolors.append(hot)

print(brightcolors)


# LISTS OF LISTS OF LISTS OF….

# Can have nested lists

# Side effects still possible after mutation

warm = ["yellow", "orange"]

hot = ["red"]

brightcolors = [warm]

brightcolors.append(hot)

print(brightcolors)



    #############################################
    #                                           #
    #  [["yellow", "orange"], ["red"]]          #
    #                                           #
    #############################################
    
  
    
# LISTS OF LISTS OF LISTS OF….

# Can have nested lists

# Side effects still possible after mutation    
    

    
    #############################################
    #                                           #
    #  [["yellow", "orange"], ["red"]]          #
    #                                           #
    #############################################



warm = ["yellow", "orange"]

hot = ["red"]

brightcolors = [warm]

brightcolors.append(hot)

print(brightcolors)

hot.append("pink")

print(hot)

print(brightcolors)


# LISTS OF LISTS OF LISTS OF….

# Can have nested lists

# Side effects still possible after mutation



    #############################################
    #                                           #
    #  [["yellow", "orange"], ["red"]]          #  ◀︎----------- 
    #  ["red", "pink"]                          # 
    #  [["yellow", "orange"], ["red", "pink"]]  #  ◀︎-----------                                         #
    #                                           #
    #############################################


warm = ["yellow", "orange"]

hot = ["red"]

brightcolors = [warm]

brightcolors.append(hot)

print(brightcolors)  #  ◀︎------

hot.append("pink")

print(hot)

print(brightcolors)  #  ◀︎------






















    















    
    
    



























    
    
    
    
    
    













 
    
    
    
    
    


























    
    


























































































         
         
         





 








    









 
































 















    
    
    
    
    
    












    





            






          
            
            
            
            
            
            
            
            
            
            
            
            
            
            
































         
            
            
            
            
            
            
            
            
        
        














 



            
        
        









            














         







