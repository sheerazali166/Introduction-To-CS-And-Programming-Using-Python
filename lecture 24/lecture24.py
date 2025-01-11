#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 21:21:16 2025

@author: sheeraz
"""


# SORTING ALGORITHMS


# SEARCHING A SORTED LIST

# -- n is len(L)

# Using linear search, search for an element is Θ(n)


# Using binary search, can search for an element in Θ(logn)

    # assumes the list is sorted!
    
    
# When does it make sense to sort first then search?


#  Time to sort              Time for linear search  
         
#  -------    -----------    ------
# | SORT | + | Θ(log n) | < | Θ(n) | implies SORT < Θ(n) – Θ(log n)    
# -------    -----------    ------- 

#            Time for bnary search 



# When sorting is less than Θ(n)!?!? This is never true!


# AMORTIZED COST

# -- n is len(L)


# Why bother sorting first?

# Sort a list once then do many searches

# AMORTIZE cost of the sort over many searches

#  Only once!    Do K searches    

#  -------    ----               ----
# | SORT | + | K | * Θ(log n) < | K | * Θ(n)
# -------    ----               -----

        # --> for large K, SORT time becomes irrelevant



# SORTING ALGORITHMS


# BOGO/RANDOM/MONKEY SORT


# aka bogosort, stupidsort, slowsort, randomsort, shotgunsort


# To sort a deck of cards

    # throw them in the air
    # pick them up
    # are they sorted?
    # repeat if not sorted


import random


# COMPLEXITY OF BOGO SORT

# def bogo_sort(L):
    
    # while not is_sorted(L):
        
        # random.shuffle(L)
        
        
# Best case: Θ(n) where n is len(L) to check if sorted

# Worst case: Θ(?) it is unbounded if really unlucky


# BUBBLE SORT


# Compare consecutive pairs of elements   
     
# Swap elements in pair such that smaller is first        
        
# When reach end of list, start over again
        
# Stop when no more swaps have been made

# COMPLEXITY OF BUBBLE SORT

def bubble_sort(L):
    
    did_swap = True
    
    while did_swap:
  # ---------------
  
  # Θ(len(L)) 


        did_swap = False
        
        for j in range(1, len(L)):
      # --------------------------
      
      # Θ(len(L))

            if L[j-1] > L[j]:
                
                did_swap = True
                
                L[j], L[j-1] = L[j-1], L[j]
                
                
# Inner for loop is for doing the comparisons

# Outer while loop is for doing multiple passes until no more swaps                
                
# Θ(n^2) where n is len(L)                

    # to do len(L)-1 comparisons and len(L)-1 passes
    
    
# SELECTION SORT


# First step

    # Extract minimum element

    # Swap it with element at index 0


# Second step

    # In remaining sublist, extract minimum element
    
    # Swap it with the element at index 1
    
    
# Keep the left portion of the list sorted

    # At ith step, first i elements in list are sorted

    # All other elements are bigger than first i elements
    
    
# COMPLEXITY OF SELECTION SORT

def selecton_sort(L):

    for i in range(len(L)):
  # -----------------------

  # len(L) times --> Θ(len(L)) 
      
        
        for j in range(i, len(L)):
      # --------------------------
      
      # len(L) - i times Θ(len(L))        
            
    
             
            if L[j] < L[i]:
                
                L[i], L[j] = L[j], L[i]
                
                
# Complexity of selection sort is 𝚯(n^2) where n is len(L) 

    # Outer loop executes len(L) times
    
    # Inner loop executes len(L) – i times, on avg len(L)/2               
                
          
# Can also think about how many times the comparison happens over
# both loops: say n = len(L)    


# Approx 1+2+3+…+n = (n)(n+1)/2 = n^2/2+n/2 = Θ(n^2)


# VARIATION ON SELECTION SORT: don’t swap every time


# MERGE SORT

# Use a divide-and-conquer approach:

    # If list is of length 0 or 1, already sorted

    # If list has more than one element, split into two lists, and sort each


    # Merge sorted sublists

        # Look at first element of each, move smaller to end of the result            
                
        # When one list empty, just copy rest of other list          
                
 
# MERGE SORT

    # Divide and conquer


    ####################################################################################################################
    #                                                                                                                  #
    #                                                unsorted                                                          #
    #                                                                                                                  #
    ####################################################################################################################
    
    
    ######################################################       #######################################################
    #                                                    #       #                                                     #
    #                      unsorted                      #       #                        unsorted                     #
    #                                                    #       #                                                     #
    ######################################################       #######################################################
    
    
    ##########################   #########################       ##########################   ##########################
    #                        #   #                       #       #                        #   #                        #
    #       unsorted         #   #        unsorted       #       #        unsorted        #   #         unsorted       #
    #                        #   #                       #       #                        #   #                        # 
    ##########################   #########################       ##########################   ##########################
    
    
    
    ############  ############   ############  ############      ############  ############   ############  ############   
    #          #  #          #   #          #  #          #      #          #  #          #   #          #  #          #                        
    #   unso   #  #   unso   #   #   unso   #  #   unso   #      #   unso   #  #   unso   #   #   unso   #  #   unso   #                 
    #   rted   #  #   rted   #   #   rted   #  #   rted   #      #   rted   #  #   rted   #   #   rted   #  #   rted   #                            
    #          #  #          #   #          #  #          #      #          #  #          #   #          #  #          #
    ############  ############   ############  ############      ############  ############   ############  ############           
    
    
    
    #####  #####   ##### #####    #####  #####  #####  #####     #####  #####   ##### #####    #####  #####  #####  #####
    #   #  #   #   #   # #   #    #   #  #   #  #   #  #   #     #   #  #   #   #   # #   #    #   #  #   #  #   #  #   # 
    #   #  #   #   #   # #   #    #   #  #   #  #   #  #   #     #   #  #   #   #   # #   #    #   #  #   #  #   #  #   # 
    #   #  #   #   #   # #   #    #   #  #   #  #   #  #   #     #   #  #   #   #   # #   #    #   #  #   #  #   #  #   # 
    #   #  #   #   #   # #   #    #   #  #   #  #   #  #   #     #   #  #   #   #   # #   #    #   #  #   #  #   #  #   # 
    #####  #####   ##### #####    #####  #####  #####  #####     #####  #####   ##### #####    #####  #####  #####  ##### 
   
#    |        |    |        |      |        |    |        |      |        |    |        |      |        |    |        |
#    |        |    |        |      |        |    |        |      |        |    |        |      |        |    |        | 
#    ----------    ----------      ----------    ----------      ----------    ----------      ----------    ----------
 
#      merge         merge            merge        merge            merge        merge            merge         merge          


# Split list in half until have sublists of only 1 element


# MERGE SORT


# Divide and conquer


    ####################################################################################################
    #                                                                                                  #
    #                                           unsorted                                               #
    #                                                                                                  #
    ####################################################################################################
    
    
    ##############################################       ###############################################
    #                                            #       #                                             #
    #                  unsorted                  #       #                   unsorted                  #
    #                                            #       #                                             #
    ##############################################       ###############################################
    
    
    ######################   #####################       ######################   ######################
    #                    #   #                   #       #                    #   #                    #
    #       unsorted     #   #     unsorted      #       #      unsorted      #   #       unsorted     #
    #                    #   #                   #       #                    #   #                    # 
    ######################   #####################       ######################   ######################



    ########## ##########    ########## ##########       ########## ##########    ########## ##########
    #        # #        #    #        # #        #       #        # #        #    #        # #        #
    #  sort  # #  sort  #    #  sort  # #  sort  #       #  sort  # #  sort  #    #  sort  # #  sort  #
    #        # #        #    #        # #        #       #        # #        #    #        # #        #
    ########## ##########    ########## ##########       ########## ##########    ########## ##########

#     |               |        |               |           |               |        |               |
#     |               |        |               |           |               |        |               | 
#     ----------------         ----------------            ----------------         ---------------- 

#          merge                     merge                      merge                     merge 
    
    


# Merge such that sublists will be sorted after merge


# MERGE SORT

# Divide and conquer


    ####################################################################################################
    #                                                                                                  #
    #                                           unsorted                                               #
    #                                                                                                  #
    ####################################################################################################
    
    
    ##############################################       ###############################################
    #                                            #       #                                             #
    #                  unsorted                  #       #                   unsorted                  #
    #                                            #       #                                             #
    ##############################################       ###############################################
    
    
    ######################   #####################       ######################   ######################
    #                    #   #                   #       #                    #   #                    #
    #        sorted      #   #      sorted       #       #       sorted       #   #        sorted      #
    #                    #   #                   #       #                    #   #                    # 
    ######################   #####################       ######################   ######################

#      |                                     |              |                                      | 
#      |                                     |              |                                      |
#      |                                     |              |                                      |
#      --------------------------------------               ---------------------------------------

#                      merge                                                 merge
                

# Merge sorted sublists

# Sublists will be sorted after merge                
                
                
# MERGE SORT

# Divide and conquer    
    
    
    ####################################################################################################
    #                                                                                                  #
    #                                           unsorted                                               #
    #                                                                                                  #
    ####################################################################################################
    
    
    ##############################################       ###############################################
    #                                            #       #                                             #
    #                   sorted                   #       #                    sorted                   #
    #                                            #       #                                             #
    ##############################################       ###############################################

#                                   |                                 |       
#                                   |                                 |
#                                   |                                 |
#                                   ----------------------------------   
    
#                                                 merge   



# Merge sorted sublists    

# Sublists will be sorted after merge


# MERGE SORT


# Divide and conquer – done!


    ####################################################################################################
    #                                                                                                  #
    #                                            sorted                                                #
    #                                                                                                  #
    ####################################################################################################


# MERGE SORT DEMO

# 1. Recursively divide into subproblems

# 2. Sort each subproblem using linear merge

# 3. Merge (sorted) subproblems into output list


# CLOSER LOOK AT THE MERGE STEP (EXAMPLE)


#          Left in list 1          Left in list 2          Compare          Result



#           -----                   ----                    ----  
#         [| 1, |5,12,18,19,20]   [| 2 |,3,4,17]           | 1 |, 2        []   ⃝ 
#          -----                   ----                    ----                ▲ 
#                                                           |                  |
#                                                           -------------------


#           -----                    -----                      ----
#         [| 5, |12,18,19,20]      [| 2, |3,4,17]           5, | 2 |        [1]   ⃝
#          -----                    -----                      -----            ▲ 
#                                                               |               |
#                                                               ----------------                   

                                                                       
#          ----                        ----                       ---- 
#        [| 5, |12,18,19,20]         [| 3, |4,17]            5,  | 3 |      [1,2]   ⃝
#         -----                       -----                      -----            ▲ 
#                                                                 |               |
#                                                               -  --------------- 



#        [5,12,18,19,20]            [4,17]                   5, 4           [1,2,3]

#        [5,12,18,19,20]            [17]                     5, 17          [1,2,3,4]

#        [12,18,19,20]              [17]                     12, 17         [1,2,3,4,5]

#        [18,19,20]                 [17]                     8, 17          [1,2,3,4,5,12]

#       [18,19,20]                  []                       18, --         [1,2,3,4,5,12,17]

#       []                          []




# [1,2,3,4,5,12,17,18,19,20]


# MERGING SUBLISTS STEP

def merge(left, right):
    
    result = []
    
    i, j, = 0, 0

    while i < len(left) and j < len(right):
    
        if left[i] < right[j]:
      # ----------------------      
            
            result.append(left[i])
          # ----------------------  
            
            i += 1
          # ------
          
            
        else:
     # ------       
           
            result.append(right[j])
          # -----------------------  
            
            j += 1
          # ------
          
      # - Left and right sublists are ordered           
            
      # - Move indices for sublists depending on whch sublist holds next
      
      # smallest element      


    while (i < len(left)):
  # ----------------------

        result.append(left[i])
      # ---------------------   
        
        i += 1
      # ------  

    # When right sublist is empty
    

    while (j < len(right)):
  # -----------------------      
        
        result.append(right[j])
      # -----------------------  
        
        j += 1
      # ------  
        
    # When left sublist is empty        
        
        
    return result


# COMPLEXITY OF MERGING STEP


# Go through two lists, only one pass

# Compare only smallest elements in each sublist

# Θ(len(left) + len(right)) copied elements

# Worst case Θ(len(longer list)) comparisons

# Linear in length of the lists


# FULL MERGE SORT ALGORITHM

# -- RECURSIVE


def merge_sort(L):
    
    if len(L) < 2:
  # --------------      
        
        return L[:]
      # -----------

  # base case

    else:
        
        middle = len(L) // 2
        
        
        left = merge_sort(L[:middle])
      # -----------------------------  

        right = merge_sort(L[middle:])
      # ------------------------------
      # divide
      
        return merge_sort(left, right)
      # ------------------------------
      # conquer with the merge step
        
        
# Divide list successively into halves


# Depth-first such that conquer smallest pieces down one branch first before
# moving to larger pieces


#
#
#                                          -------------------------------------
#                                          |      |   8 4 1 6 | 5 9 2 0  |     | 
#                                          |     --------------------------    |
#                                          |    |                         |    |
#                                          |    |          Merge          |    |
#                                          |    |                         |    |
#                          ----------------|----|    1 4 6 8 & 0 2 5 9    |----|-----------------
#                         |                |    |                         |    |                | 
#                         |                |    |    0 1 2 4 5 6 8 9      |    |                |
#                         |                |    |          ▲ ▲            |    |                |
#                         |                |    -----------|-|------------     |                |
#                         |                ----------------|-|-----------------                 |
#                         |                                | |                                  |
#                         |                                | |                                  |
#                         |                                | |                                  |
#                         |                                | |                                  |
#                         |                                | |                                  | 
#                         ▼                                | |                                  ▼
#           ----------------------------                   | |                     ----------------------------
#           |        ------------       |                  | |                    |        ------------       |
#       ----|------ | 8 4 | 1 6 | ------|-----------       | |            --------|-----  | 5 9 | 2 0 | ------|------------
#      |    |    ---------|---------    |           |      | |           |        |     --------|---------    |           | 
#      |    |    |        ---------|----|-----------|------  ------------|--------|----|---------        |    |           |
#      |    |    |      Merge      |    |           |                    |        |    |      Merge      |    |           |
#      |    |    |                 |    |           |                    |        |    |                 |    |           |
#      |    |    |     4 8 & 1 6   |    |           |                    |        |    |    5 9 & 0 2    |    |           |
#      |    |    |                 |    |           |                    |        |    |                 |    |           | 
#      |    |    |     1 4 6 8     |    |           |                    |        |    |     0 2 5 9     |    |           |
#      |    |    |                 |    |           |                    |        |    |                 |    |           |
#      |    |    --------▲-▲--------    |           |                    |        |    --------▲-▲--------     |          |
#      |    -------------|-|------------            |                    |        -------------|-|------------            |
#      |                 | --------                 |                    |                     --|-----                   |
#      -------------     --------  |                |                    -----------------        ----|---                |
#                  |            |  |                |                                    |            |  |                |
#                  |            |  |                |                                    |            |  |                |
#    --------------|----------  |  |  --------------|----------            --------------|----------  |  |   -------------|---------
#    |         ----▼----     |  |  |  |         ----▼----     |            |         ----▼---      |  |  |  |         ----▼---      |
#    |        | 8 | 4  |     |  |  |  |        | 1 | 6 |      |         ---|-----   | 5 | 9 |------|--|- | -|-----   | 2 | 0 |  ----|----
#    |        ---------      |  |  |  |        ---------      |        |   |        --------       |  || || |        --------       |   |   
#    |          |  --|-------|---  ---|----------|-  |        |        |   |             ----------|---|  |-|-------------          |   | 
#  --|-----------  | --------|--    --|---------- |  ---------|---     |   |            |          |   |  | |            |          |   |
# |  |     -------------     | |   |  |     --------------    |  |     |   |     --------------    |   |  | |     --------------    |   | 
# |  |    |             |    | |   |  |    |             |    |  |     |   |    |             |    |   |  | |    |             |    |   |
# |  |    |    Merge    |    | |   |  |    |    Merge    |    |  |     |   |    |    Merge    |    |   |  | |    |    Merge    |    |   |
# |  |    |             |    | |   |  |    |             |    |  |     |   |    |             |    |   |  | |    |             |    |   |
# |  |    |     4 8     |    | |   |  |    |     1 6     |    |  |     |   |    |     5 9     |    |   |  | |    |     0 2     |    |   | 
# |  |    |             |    | |   |  |    |             |    |  |     |   |    |             |    |   |  | |    |             |    |   |
# |  |    -----▲--▲------    | |   |  |    -----▲--▲------    |  |     |   |    ------▲-▲------    |   |  | |    ------▲-▲------    |   |
# |  |         |  |          | |   |  |         |  |          |  |     |   |          | |          |   |  | |          | |          |   | 
# |  ----------|--|----------  |   |  ----------|--|----------   |     |   -----------|-|-----------   |  | -----------|-|----------    |
# |            |  |            |   |            |  |             |     |              | |              |  |            | |              |
# |          --   -------      |   |            |  ----------    |     -----  ---------  ---           |  |   ---------   -----         |
# |         |            |     |   |       ------            |   |         | |              | ---------   -  |                 | -------
# |         |            |  ---    |      |                  |   |         | |              | |            | |                 | |
# --------- |            | |       -----  |                  |  -          | |              | |            | |                 | |
#         | |            | |            | |                  | |           | |              | |            | |                 | |
#         | |            | |            | |                  | |           | |              | |            | |                 | | 
#         | |            | |            | |                  | |           | |              | ▼            ▼ |                 | ▼
#    -----▼------    ------▼-----  -----▼-------          -----▼----- ------------      ------------  ------------          ------------         
#    |          |    |          |  |          |          |          | |          |      |          |  |          |          |          | 
#    |    8     |    |    4     |  |    1     |          |    6     | |    5     |      |    9     |  |    2     |          |    0     |          
#    |          |    |          |  |          |          |          | |          |      |          |  |          |          |          |  
#    |          |    |          |  |          |          |          | |          |      |          |  |          |          |          | 
#    |          |    |          |  |          |          |          | |          |      |          |  |          |          |          |
#    |  base    |    |  base    |  |  base    |          |  base    | |  base    |      |  base    |  |  base    |          |   base   |
#    |          |    |          |  |          |          |          | |          |      |          |  |          |          |          |  
#    |  case    |    |  case    |  |  case    |          |  case    | |  case    |      |  case    |  |  case    |          |   case   | 
#    |          |    |          |  |          |          |          | |          |      |          |  |          |          |          |    
#    -----------     -----------   -----------           -----------  -----------       -----------   ------------          -----------
#


# COMPLEXITY OF MERGE SORT


# Each level

    # At first recursion level
    
        # n/2 elements in each list, 2 lists
        
        # One merge --> Θ(n) + Θ(n) = Θ(n) where n is len(L)


    # At second recursion level

        # n/4 elements in each list, 4 lists
        
        # Two merges --> Θ(n) where n is len(L)


    # And so on…
    
  
# Dividing list in half with each recursive call gives our levels

    # Θ(log n) where n is len(L)

    # Like bisection search: 1 = n/2^i tells us how many splits to ge
    # t to one element    

# Each recursion level does Θ(n) work and there are Θ(log n) levels, where
# n is len(L)


# Overall complexity is 𝚯(n log n) where n is len(L)


# SORTING SUMMARY

# -- n is len(L)


# Bogo sort

    # Randomness, unbounded Θ()
    
    
# Bubble sort

    # Θ(n^2)

    
# Selection sort

    # Θ(n^2)
    
    # Guaranteed the first i elements were sorted


# Merge sort

    # Θ(n log n)

# 𝚯(n log n) is the fastest a sort can be        
        
# COMPLEXITY SUMMARY

# Compare efficiency of algorithms

    # Describe asymptotic order of growth with Big Theta
    
    # Worst case analysis



    # Saw different classes of complexity
    
        # Constant
        
        # Log
        
        # Linear
        
        # Log linear
        
        # Polynomial
        
        # Exponential


    # A priori evaluation (before writing or running code)

    # Assesses algorithm independently of machine and implementation.
    

    # Provides direct insight to the design of efficient algorithms    
    
    