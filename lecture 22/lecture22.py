#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 15:35:43 2025

@author: sheeraz
"""

# BIG OH and THETA

# TIMING

# TIMING A PROGRAM

# Use time module

# Importing means bringing collection of functions into your own file

import time

def convert_to_km(m):
    
    return m * 1.609

t0 = time.perf_counter()
#|   -------------------
#|   More accurate timer, meaningful when used to get a time diff 
# ----
#    |
#    ▼ 
# Start clock

# Call function

convert_to_km(100000)


#  ----▶︎ Stop clock
# |
dt = time.perf_counter() - t0

print("t =", dt, "s,")


# EXAMPLE: convert_to_km, compound

def convert_to_km(m):
    
    return m * 1.609

def compound(invest, interest, n_months):
    
    total = 0
    
    for i in range(n_months):
        
        total = total * interest + invest
        
    return total


# How long does it take to compute these functions?

# Does the time depend on the input parameters?

# Are the times noticeably different for these two functions?


# CREATING AN INPUT LIST

L_N = [1]
# -------

for i in range(7):
# ----------------

    L_N.append(L_N[-1]*10)
  # ----------------------
  
# Create a set of input sizes, each of which is 10 times larger than the
# previous one [1, 10, 100, 1000, ...]


for N in L_N:
    
    t = time.perf_counter()
  # -----------------------
  
    km = convert_to_km(N)
  # ---------------------
  
    dt = time.perf_counter() - t
  # ----------------------------
  # Measure time to compute (aka run function) for each input
  
    print(f"convert_to_km({N}) took {dt} seconds ({ 1 / dt} / sec)")
                                  # ----         ----------------- 
                                  
# Report time and how many times the fcn can run per sec   


# RUN IT!

# convert_to_km OBSERVATIONS


# Observation: average time seems independent of size of argument


# MEASURE TIME:
    
# compoundwith a variable number of months

def compound(invest, interest, n_months):

    total = 0

    for i in range(n_months):
        
        total = total * interest + invest
        
    return total     


# Observation 1: Time grows with the input only when n_months changes

# Observation 2: average time seems to increase by 10 as size of argument
# increases by 10

# Observation 3: relationship between size and time only predictable for
# large sizes

# MEASURE TIME: sum over L

def sum_of(L):
    
    total = 0.0
    
    for elt in L:
        
        total = total + elt
        
    return total

L_N = [1]     

for i in range(7):
    
    L_N.append(L_N[-1]*10)
    
    
for N in L_N:

    L = list(range(N))    
      # --------------
      # [0,1,2,...9] then [0,1,2,...99] etc
      
    t = time.perf_counter()    
    s = sum_of(L)
    dt = time.perf_counter() - t

    print(f"sum_of({N}) took {dt} seconds ({1 / dt} / sec) ")


# Observation 1: Size of the input is now the length of the list, not how big
# the element numbers are.

# Observation 2: average time seems to increase by 10 as size of argument
# increases by 10
  
# Observation 3: relationship between size and time only predictable for
# large sizes    

# Observation 4: Time seems comparable to computation of compound

# MEASURE TIME: find element in a list

# search each element one-by-one    
def is_in(L, x):
    
    for elt in L:
        
        if elt == x:
            
            return True
        
    return False     
        
 
# search by bisecting the list (list should be sorted!)
def binary_search(L, x):
    
    lo = 0
    
    hi = len(L)
    
    while hi-lo > 1:
        
        mid = (hi + lo) // 2
                      # --
                      # Integer division, round down
                      
        if L[mid] <= x:

            lo = mid

        else:
            
            hi = mid
            
    return L[lo] == x


# Measure "average" time. Search for the first, middle, and last element
# of sorted list, and average these 3 times.    

# search using built-in operator

# x in L

# MEASURE TIME: find element in a list

# is_in(10000000) took 1.62e-01 seconds (6.16/sec)
# 9.57 times more than for 10 times fewer elements
# binary(10000000) took 9.37e-06 seconds (106,761.64/sec)
# 1.40 times more than for 10 times fewer elements
# builtin(10000000) took 5.64e-02 seconds (17.72/sec)
# 9.63 times more than for 10 times fewer elements

# is_in(100000000) took 1.64e+00 seconds (0.61/sec)
# 10.12 times more than for 10 times fewer elements
# binary(100000000) took 1.18e-05 seconds (84,507.09/sec)
# 1.26 times more than for 10 times fewer elements
# builtin(100000000) took 5.70e-01 seconds (1.75/sec)
# 10.11 times more than for 10 times fewer elements
      
# Observation 1: searching one-by-one grows by factor of 10, when L
# increases by 10
        
# MEASURE TIME: find element in a list

# is_in(10000000) took 1.62e-01 seconds (6.16/sec)
# 9.57 times more than for 10 times fewer elements
# binary(10000000) took 9.37e-06 seconds (106,761.64/sec)
# 1.40 times more than for 10 times fewer elements
# builtin(10000000) took 5.64e-02 seconds (17.72/sec)
# 9.63 times more than for 10 times fewer elements

# is_in(100000000) took 1.64e+00 seconds (0.61/sec)
# 10.12 times more than for 10 times fewer elements
# binary(100000000) took 1.18e-05 seconds (84,507.09/sec)
# 1.26 times more than for 10 times fewer elements
# builtin(100000000) took 5.70e-01 seconds (1.75/sec)
# 10.11 times more than for 10 times fewer elements

# Observation 1: searching one-by-one grows by factor of 10, when L increases
# by 10

# Observation 2: built-in function grows by factor of 10, when L increases
# by 10


# MEASURE TIME: find element in a list

# is_in(10000000) took 1.62e-01 seconds (6.16/sec)
# 9.57 times more than for 10 times fewer elements
# binary(10000000) took 9.37e-06 seconds (106,761.64/sec)
# 1.40 times more than for 10 times fewer elements
# builtin(10000000) took 5.64e-02 seconds (17.72/sec)
# 9.63 times more than for 10 times fewer elements


# is_in(100000000) took 1.64e+00 seconds (0.61/sec)
# 10.12 times more than for 10 times fewer elements
# binary(100000000) took 1.18e-05 seconds (84,507.09/sec)
# 1.26 times more than for 10 times fewer elements
# builtin(100000000) took 5.70e-01 seconds (1.75/sec)
# 10.11 times more than for 10 times fewer elements


# Observation 1: searching one-by-one grows by factor of 10, when L
# increases by 10

# Observation 2: built-in function grows by factor of 10, when L increases
# by 10

# Observation 3: binary search time seems almost independent of size


# MEASURE TIME: find element in a list

# is_in(10000000) took 1.62e-01 seconds (6.16/sec)
# 9.57 times more than for 10 times fewer elements
# binary(10000000) took 9.37e-06 seconds (106,761.64/sec)
# 1.40 times more than for 10 times fewer elements
# builtin(10000000) took 5.64e-02 seconds (17.72/sec)
# 9.63 times more than for 10 times fewer elements


# is_in(100000000) took 1.64e+00 seconds (0.61/sec)
# 10.12 times more than for 10 times fewer elements
# binary(100000000) took 1.18e-05 seconds (84,507.09/sec)
# 1.26 times more than for 10 times fewer elements
# builtin(100000000) took 5.70e-01 seconds (1.75/sec)
# 10.11 times more than for 10 times fewer elements

# Observation 1: searching one-by-one grows by factor of 10, when L
# increases by 10

# Observation 2: built-in function grows by factor of 10, when L increases
# by 10

# Observation 3: binary search time seems almost independent of size

# Observation 4: binary search much faster than is_in, especially on
# larger problems

# MEASURE TIME: find element in a list

# is_in(10000000) took 1.62e-01 seconds (6.16/sec)
# 9.57 times more than for 10 times fewer elements
# binary(10000000) took 9.37e-06 seconds (106,761.64/sec)
# 1.40 times more than for 10 times fewer elements
# builtin(10000000) took 5.64e-02 seconds (17.72/sec)
# 9.63 times more than for 10 times fewer elements

# is_in(100000000) took 1.64e+00 seconds (0.61/sec)
# 10.12 times more than for 10 times fewer elements
# binary(100000000) took 1.18e-05 seconds (84,507.09/sec)
# 1.26 times more than for 10 times fewer elements
# builtin(100000000) took 5.70e-01 seconds (1.75/sec)
# 10.11 times more than for 10 times fewer elements

# Observation 1: searching one-by-one grows by factor of 10, when L
# increases by 10

# Observation 2: built-in function grows by factor of 10, when L increases
# by 10

# Observation 3: binary search time seems almost independent of size

# Observation 4: binary search much faster than is_in, especially on
# larger problems

# Observation 5: is_in is slightly slower than using Python’s “in” capability

# MEASURE TIME: find element in a list

def is_in(L, x):
    
    for elt in L:
        
        if elt == x:
            
            return True                               # So we have seen
#                   ▲  
    return False  # |                                 # computations where
#                   -------------------------
#                                           |         # time seems very
#                                           |           
def binary_search(L, x): #                  |         # different
#                                           |
    lo = 0                      #           |             # Constant time
#                                           |
    hi = len(L)                 #           -----------   # Linear in size of
    
    while hi-lo > 1: # ◀︎-----------                       # argument
#                                 |
        mid = (hi +lo) // 2  #    ---------------------   # Something less than
        
        if L[mid] <= x:                                   # linear?
            
            lo = mid
            
        else:
            
            hi = mid
            
    return L[lo] == x


import math

# MEASURE TIME: diameter function

# L=[(cos(0), sin(0)), (cos(1), sin(1)), (cos(2), sin(2)), ... ] # example numbers

def diameter(L):
           # --
    
    farthest_dist = 0
    
    for i in range(len(L)):
           # -------------
           
         for j in range(i + 1, len(L)):
                # --------------------
                
             # 1st iter: len(L) - 1 passes
             # 2nd iter: len(L) - 2 passes ...
             # On average, len(L) / 2 passes
           
             p1 = L[i]
             
             p2 = L[j]
             
             dist = math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
             
             if dist > farthest_dist:
                 
                 farthest_dist = dist
                 
    return farthest_dist          
        
    
    
L = [(math.cos(0), math.sin(0)), (math.cos(1), math.sin(1)), (math.cos(2),
                            math.sin(2)), (math.cos(3), math.sin(3))]    
    
    
    
print("-------------------")

print(diameter(L))

 
# MEASURE TIME: diameter function

def diameter(L):
    
    farthest_dist = 0
    
    for i in range(len(L)):
           # -------------
    
        for j in range(i + 1, len(L)):
               # --------------------
               
            # 1st iter: len(L) - 1 passes
            # 2nd iter: len(L) - 2 passes ...
            # On average, len(L) / 2 passes
            
            
             p1 = L[i]
             p2 = L[j]
             dist = math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
             
             if dist > farthest_dist:
                 
                 farthest_dist = dist
                 
    return farthest_dist            
        
    
L = [(math.cos(0), math.sin(0)),(math.cos(1), math.sin(1)),(math.cos(2),
                   math.sin(2)), (math.cos(3), math.sin(3))]



print("-------------------")

print(diameter(L))


# MEASURE TIME: diameter function

def diameter(L):

    farthest_dist = 0

    for i in range(len(L)):
           # --------------
           
        for j in range(i + 1, len(L)):
               # --------------------
               
            # 1st iter: len(L) - 1 passes         
            # 2nd iter: len(L) - 2 passes ...
            # On average, len(L) / 2 passes
            
            p1 = L[i]      
            p2 = L[j]
            
            dist = math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)  
            
            if dist > farthest_dist:
                
                farthest_dist = dist
                
    return farthest_dist

L = [(math.cos(0), math.sin(0)),(math.cos(1), math.sin(1)),(math.cos(2),
            math.sin(2)),(math.cos(3), math.sin(3))]                
            
            
print("-------------------")

print(diameter(L))            
            
            
# MEASURE TIME: diameter function

def diameter(L):

    farthest_dist = 0

    for i in range(len(L)):
           # --------------
           
        for j in range(i + 1, len(L)):
               # ---------------------
               
            # 1st iter: len(L) - 1 passes
            # 2nd iter: len(L) - 2 passes ...
            # On averages, len(L) / 2 passes
          
            p1 = L[i]    
            p2 = L[j]
            
            dist = math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
            
            if dist > farthest_dist:
                
                farthest_dist = dist
                
    return farthest_dist


L = [(math.cos(0), math.sin(0)),(math.cos(1), math.sin(1)),
         (math.cos(2), math.sin(2)),(math.cos(3), math.sin(3))]                
            
            
print("-------------------")

print(diameter(L))


# MEASURE TIME: diameter function

def diameter(L):
    
    farthest_dist = 0
    
    for i in range(len(L)):
           # -------------
           
        for j in range(i + 1, len(L)):
               # --------------------
               
            # 1st iter: len(L) - 1 passes
            # 2nd iter: len(L) - 2 passes ...
            # On average, len(L) / 2 passes
            
           p1 = L[i]
           
           p2 = L[j]
           
           dist = math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
           
           if dist > farthest_dist:
               
               farthest_dist = dist
               
    return farthest_dist


L = [(math.cos(0), math.sin(0)),(math.cos(1), math.sin(1)),(math.cos(2),
                   math.sin(2)),(math.cos(3), math.sin(3))]



print("-------------------")

print(diameter(L))

# MEASURE TIME: diameter function

def diameter(L):
    
    farthest_dist = 0
    
    for i in range(len(L)):
           # -------------
           
        for j in range(i + 1, len(L)):
               # --------------------
               
            # 1st iter: len(L) - 1 passes
            # 2nd iter: len(L) - 2 passes ...
            # On average, len(L) / 2 passes
            
           p1 = L[i]
           
           p2 = L[j]
           
           dist = math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
           
           if dist > farthest_dist:
               
               farthest_dist = dist
               
    return farthest_dist


L = [(math.cos(0), math.sin(0)),(math.cos(1), math.sin(1)),(math.cos(2),
                   math.sin(2)),(math.cos(3), math.sin(3))]



print("-------------------")

print(diameter(L))

# MEASURE TIME: diameter function

def diameter(L):
    
    farthest_dist = 0
    
    for i in range(len(L)):
           # -------------
           
        for j in range(i + 1, len(L)):
               # --------------------
               
            # 1st iter: len(L) - 1 passes
            # 2nd iter: len(L) - 2 passes ...
            # On average, len(L) / 2 passes
            
           p1 = L[i]
           
           p2 = L[j]
           
           dist = math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
           
           if dist > farthest_dist:
               
               farthest_dist = dist
               
    return farthest_dist


L = [(math.cos(0), math.sin(0)),(math.cos(1), math.sin(1)),(math.cos(2),
                   math.sin(2)),(math.cos(3), math.sin(3))]



print("-------------------")

print(diameter(L))

# MEASURE TIME: diameter function

def diameter(L):
    
    farthest_dist = 0
    
    for i in range(len(L)):
           
        for j in range(i + 1, len(L)):
            
            p1 = L[i]
            p2 = L[j]
            
            dist = math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
            
            if dist > farthest_dist:
                
                farthest_dist = dist
         
    return farthest_dist


# Gets much slower as size of input grows

# Quadratic: for list of size len(L), does len(L)/2 operations per element
# on average

# len(L) x len(L)/2 operations — worse than linear growth


# TWO DIFFERENT MACHINES

# Observation 1: even for the same code, the actual machine may affect speed.

# Observation 2: Looking only at the relative increase in run time from
# a prev run, if input is n times as big, the run time is approx. n times
# as long.

# DON’T GET ME WRONG!

# Timing is a critical tool to assess the performance of programs

    # At the end of the day, it is irreplaceable for real-world assessment

# But we will see a complementary tool (asymptotic complexity) that has
# other advantages

# A priori evaluation (before writing or running code)

# Assesses algorithm independent of machine and implementation (what is
# intrinsic efficiency of algorithm?)

# Provides direct insight into the design of efficient algorithms

# COUNTING

# COUNT OPERATIONS
                
        
# Assume these steps take
# constant time:
    
# Mathematical operations
# Comparisons
# Assignments
# Accessing objects in memory    
               
# Count number of these operations executed as function of size of input            
            

# convert_to_km --> 2 ops            
            
def convert_to_km(m):

    return m * 1.609
  # ----------------
  # 2 op
            
# sum_of --> 1+len(L)*3+1 = 3*len(L)+2 ops                    
            
def sum_of(L):

    total = 0
  # ---------
  # 1 op
  
    for i in L: # 1 op
  # -----------
  # loop len(L) times

        total += i
      # ----------
      # 2 op
      
    return total
  # ------------
  # 1 op   
        
        
# COUNT OPERATIONS: is_in

def is_in_counter(L, x):
    
    for elt in L:
        
        if elt == x:
            
            return True
        
    return False


# COUNT OPERATIONS: is_in

def is_in_counter(L, x):
    
    global count
  # ------------
    
    count += 1
  # ----------
  # Return value  
    
    for elt in L:
        
        count += 2
      # ----------
      # Set elt as val from L, Check elt == x 
        
        if elt == x:
            
            return True
        
    return False


# Global let us reference and change an external variable inside a function
# - OK for debugging / timing but not good practice in real programs

# COUNT OPERATIONS: binary search

def binary_search_count(L, x):
    
    global count
    
    lo = 0
    
    hi = len(L)
    
    count += 3
  # ----------
  # Set lo, hi, len

    while hi-lo > 1:
        
        count += 2
      # ----------
      # While test and the subtraction
      
        mid = (hi + lo) // 2
        
        count += 3
      # ----------
      # Addition, //, and assign mid  
        
        if L[mid] <= x:
            
            lo = mid
        
        else:
             
            hi = mid
             
        count += 3 
      # ----------
      # Access mid, if test and assign mid
        
        
        
    count += 3
  # ----------
  # Access lo, == test, return
  
    return L[lo] == x

    
        
# COUNT OPERATIONS        
             
# is_in testing
# for 1 element, is_in used 9 operations
# for 10 element, is_in used 37 operations
# for 100 element, is_in used 307 operations
# for 1000 element, is_in used 3007 operations
# for 10000 element, is_in used 30007 operations
# for 100000 element, is_in used 300007 operations
# for 1000000 element, is_in used 3000007 operations             
   

# Observation 1: number of
# operations for is_in increases by
# 10 as size increases by 10     
        
        
# binary_search testing
# for 1 element, binary search used 15 operations
# for 10 element, binary search used 85 operations
# for 100 element, binary search used 148 operations
# for 1000 element, binary search used 211 operations
# for 10000 element, binary search used 295 operations
# for 100000 element, binary search used 358 operations
# for 1000000 element, binary search used 421 operations        
        

# Observation 2: but number
# of operations for binary
# search grows much more
# slowly. Unclear at what rate.        
        
        
# PLOT OF INPUT SIZE vs. OPERATION COUNT


# PROBLEMS WITH TIMING AND COUNTING

# Timing the exact running time of the program

    # Depends on machine
    
    # Depends on implementation
    
    # Small inputs don’t show growth
    
# Counting the exact number of steps    
    
    # Gets us a formula!
    
    # Machine independent, which is good
    
    # Depends on implementation
    
    # Multiplicative/additive constants are irrelevant for large inputs
    
# Want to:

    # evaluate algorithm

    # evaluate scalability

    # evaluate in terms of input size

# EFFICIENCY IN TERMS OF INPUT: BIG-PICTURE RECALL mysum(one loop) and
# square(nested loops)

# mysum(x)

    # What happened to the program efficiency as x increased?

    # 10 times bigger x meant the program

        # Took approx. 10 times as long to run
        
        # Did approx. 10 times as many ops
        
        
   # Express it in an “order of” way vs. the input variable:
   # efficiency = Order of x     
        
        
# square(x)

    # What happened to the program efficiency as x increased?
    
    # 2 times bigger x meant the program        
    
        # Took approx. 4 times as long to run
    
        # Did approx. 4 times as many ops

    # 10 times bigger x meant the program
    
        # Took approx. 100 times as long to run
        
        # Did approx. 100 times as many ops
        
    # Express it in an “order of” way vs. the input variable:
    # efficiency = Order of x^2    
    
    
# ORDER of GROWTH

# ORDERS OF GROWTH

# It’s a notation

# Evaluates programs when input is very big

# Expresses the growth of program’s run time

# Puts an upper bound on growth

# Do not need to be precise: “order of” not “exact” growth


# Focus on the largest factors in run time (which section of the program will
# take the longest to run?)


# A BETTER WAY

# A GENERALIZED WAY WITH APPROXIMATIONS

# Use the idea of counting operations in an algorithm, but not worry about
# small variations in implementation

    # When x is big, 3x+4 and 3x and x are pretty much the same!
    
    # Don’t care about exact value: ops = 1+x(2+1)
    
    # Express it in an “order of” way vs. the input: ops = Order of x
    

# Focus on how algorithm performs when size of problem gets arbitrarily large    
    

# Relate time needed to complete a computation against the size of the input
# to the problem
    
# Need to decide what to measure. What is the input?

# WHICH INPUT TO USE TO MEASURE EFFICIENCY

# Want to express efficiency in terms of input, so need to decide what is
# your input


# Could be an integer

    # -- convert_to_km(x)
    
# Could be length of list

    # -- list_sum(L)


# You decide when multiple parameters to a function

    # -- is_in(L, e)
    
        # Might be different depending on which input you consider
        
        
# DIFFERENT INPUTS CHANGE HOW THE PROGRAM RUNS 
       
        
# A function that searches for an element in a list        
        

def is_in(L, e):
    
    for i in L:
        
        if i == e:
            
            return True

    return False


# Does the program take longer to run as eincreases?

    # No
    
    
    # is_in([1, 2, 3], 0) vs.
    # is_in([1, 2, 3], 1000)
    

print("---------------------")

print(is_in([1, 2, 3], 0))

print(is_in([1, 2, 3], 1000))



# DIFFERENT INPUTS CHANGE HOW THE PROGRAM RUNS

# A function that searches for an element in a list

def is_in(L, e):
    
    for i in L:
        
        if i == e:
        
            return True
        
    return False


# is_in([1, 2, 3], 0) vs.
# is_in([1000, 2000, 3000], 0)

print(is_in([1, 2, 3], 0))    
print(is_in([1000, 2000, 3000], 0))

# Does the program take longer to run as Lincreases?

    # What if L has a fixed length and its elements are big numbers?

       # No

    # What if L has different lengths?            

        # Yes!

# is_in([1, 2, 3], 0) vs.        
        
# is_in([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0)         
        

print(is_in([1, 2, 3], 0))

print(is_in([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0))        
        
        
# DIFFERENT INPUTS CHANGE HOW
# THE PROGRAM RUNS    
    
# A function that searches for an element in a list

def is_in(L, e):

    for i in L:
        
        if i == e:
            
            return True
        
    return False        
    

# When e is first element in the list

# --> BEST CASE

# When look through about half of the elements in list

# --> AVERAGE CASE

# When e is not in list

#  -----------------------------------------------------
# | --> WORST CASE                                     |
# |                                                    | 
# |   # Want to measure this behavior in a general way |           
# -----------------------------------------------------


# ASYMPTOTIC GROWTH

# Goal: describe how time grows as size of input grows

    # Formula relating input to number of operations
    
    
# Given an expression for the number of operations needed to compute an
# algorithm, want to know asymptotic behavior as size of problem gets large    

    # Want to put a bound on growth
    
    # Do not need to be precise: “order of” not “exact” growth
    
# Will focus on term that grows most rapidly

    # Ignore additive and multiplicative constants, since want to know how
    # rapidly time required increases as we increase size of input    

# This is called order of growth

    # Use mathematical notions of “big O” and “big Θ” Big Oh and Big Theta    
    
    
# BIG O Definition


#  --------------------------
# | 3𝑥^2 + 20𝑥 + 1 = 𝑂(𝑥^2) |    
# --------------------------    


# Suppose some code runs in

# 𝑓(𝑥) = 3x^2 + 20x + 1 steps
    
    # Think of this as the formula from counting the number of ops.

    
# Big OH is a way to upper bound the growth of any function
    
#  -----------------    
# | f(x) = O(g(x)) | means that g(x) times some constant eventually always
# -----------------
# exceeds f(x)

#                                  -----------------------
    # Eventually means above some | threshold value of x |
#                                 -----------------------


#  -------                       --------
# | 4x^2 | > 3x^2 + 20x + 1∀x > | 20.04 |    
# -------                       --------   
    
    
# BIG O FORMALLY

# A big Oh bound is an upper bound on the growth of some function

#  -----------------
# | 𝑓(𝑥) = 𝑂(𝒈(𝒙)) | means there exist
# -----------------


#                             ------------   -------              ------
# constants 𝒄𝟎, 𝒙𝟎 for which | 𝒄𝟎 | 𝒈(𝒙) | ≥ | 𝒇(𝒙) | for all 𝑥 > | 𝒙𝟎 |
#                            ------------    -------             ------


# Example: 𝑓(𝑥) = 3x^2 + 20x + 1

#  ----------------           ---------    -----------------       ----  
# | 𝑓(𝑥) = 𝑂(𝒙^𝟐) | ,because | 𝟒 | x^𝟐 | > | 𝟑𝒙^𝟐 + 𝟐𝟎𝒙 + 𝟏 | ∀𝑥 ≥ | 𝟐𝟏 |
# ----------------           ----------    ----------------       -----
#                                                   (𝒄𝟎 = 𝟒, 𝒙𝟎 = 𝟐𝟎 𝟎𝟒)


# BIG Θ Definition
    
# 3𝑥^2 − 20𝑥 − 1 = 𝜃(𝑥^2)

# A big Θ bound is a lower and upper bound on the growth of some function

# Suppose 𝑓(𝑥) = 3𝑥^2 − 20𝑥 − 1

# 𝒇(𝒙) = Θ(𝒈(𝒙)) means:


#                                        ------------------------------- 
# there exist constants 𝒄𝟎, 𝑥0 for which | 𝒄𝟎𝒈(𝒙) ≥ 𝒇(𝒙) for all 𝑥 > 𝒙𝟎 |
#                                        -------------------------------
#                                           Big O definition                                     

# and constants 𝒄𝟏, 𝑥1 for which 𝒄𝟏𝒈(𝒙) ≤ 𝒇(𝒙) for all 𝑥 > 𝒙𝟏
        

#                                 ------------------------------------------
# Example, 𝒇(𝒙) = Θ(^𝟐𝟐) because | 𝟒𝒙^𝟐 > 𝟑𝒙^𝟐 - 20x ∀𝑥 ≥ 𝟎 (𝒄𝟎 = 𝟒, 𝒙𝟎 = 𝟎) |
#                                -------------------------------------------

# and 𝟐𝒙^2 < 𝟑𝒙^𝟐 − 𝟐𝟎𝒙 − 𝟏 ∀𝑥 ≥ 21 (𝒄1 = 2, 𝒙1 = 20.04)


# Θ vs O

# In practice, Θ bounds are preferred, because they are “tight”
            
# For example: 𝑓(𝑥) = 3𝑥^2 − 20𝑥 − 1            
            

# 𝑓(𝑥) = 𝑂(𝑥^2) = 𝑂(𝑥^3) = 𝑂(2^𝑥) and anything higher order because they
# all upper bound it           
            
  
# 𝒇(𝒙) = 𝜣(𝒙^𝟐)

# ≠ Θ(𝑥^3) ≠ Θ(2^𝑥) and anything higher order because they upper bound but
# not lower bound it          
            
# SIMPLIFICATION EXAMPLES

# Drop constants and multiplicative factors

# Focus on dominant term

#            ------ 
# Θ(n^2)  : | n^2 | + 2n + 2
#           ------

#           -------      
# Θ(x^2) : | 3x^2 | + 100000x + 3^1000
#          ------- 
        
#                  ----
# Θ(a) : log(a) + | a | + 4    
#                 ----  
    
    
# BIG IDEA

# Express Theta in terms of the input.    

# Don’t just use n all the time!

        
# YOU TRY IT!

# Θ(x) : 1000*log(x) + x

# Θ(n^3) : n^2log(n) + n^3

# Θ(y) : log(y) + 0.000001y


# Θ(2^ b) : 2^b + 1000a^2 + 100*b^2 + 0.0001a^3


# Θ(a^3)

# Θ(2^b+a^3)

# All could be ok, depends on the input we care about


# USING Θ TO EVALUATE YOUR ALGORITHM


def fact_iter(n):
    
    """ assumes n an int >= 0 """
    
    answer = 1

    while n > 1:
  # -----------
      
        answer *= n
     # ------------   
        
        n -= 1
      # ------  
        
      
    return answer     


print("---------------")

print(fact_iter(6))
print(fact_iter(7))


# 5 steps inside loop

# 1. compare,
# 2. multiply,
# 3. assign,
# 4. subtract,
# 5. assign


# Number of steps: 5n + 2

# Worst case asymptotic complexity: Θ(n)

    # Ignore additive constants
    
        # 2 doesn’t matter when n is big
        
    # Ignore multiplicative constants    
        
    # 5 doesn’t matter if just want to know how increasing n changes time
    # needed    
        
        
 
# COMBINING COMPLEXITY CLASSES LOOPS IN SERIES        
        
# Analyze statements inside functions to get order of growth

# Apply some rules, focus on dominant term

# Law of Addition for Θ():
    
    # Used with sequential statements
    
    # Θ(𝑓(𝑛)) + Θ(𝑔(𝑛)) = Θ(𝑓(𝑛) + 𝑔(𝑛𝑛))
    
    
# For example,

n = 10


for i in range(n):          # Θ(n)

    print("a")
    
for j in range(n * n):      # Θ(n2)

    print("b")


# is Θ(𝑛) + Θ(𝑛 ∗ 𝑛) = Θ(𝑛 + 𝑛^2) = Θ(𝑛^2) because of dominant 𝑛^2 term
        
 
# COMBINING COMPLEXITY CLASSES NESTED LOOPS    
    
# Analyze statements inside functions to get order of growth

# Apply some rules, focus on dominant term

#  Law of Multiplication for Θ():    
    
    # Used with nested statements/loops

    # Θ(𝑓(𝑛)) ∗ Θ(𝑔(𝑛)) = Θ(𝑓(𝑛) ∗ 𝑔(𝑛))    


print("----------------")

# For example,

for i in range(n):  # Θ(n)

    for j in range(n // 2):    # Θ(n) for each outer loop iteration

        print("a")
        
        
# Θ(𝑛) × Θ(𝑛) = Θ(𝑛 × 𝑛) = Θ(𝑛^2)

# Outer loop runs n times and the inner loop runs n times for every outer
# loop iteration.        

# ANALYZE COMPLEXITY

# What is the Theta complexity of this program?

def f(x):
   # --
   # Always note the input parameter!
   
    answer = 1
    
    for i in range(x):
  # ------------------      
        
        for j in range(i, x):
      # ---------------------      
            
            answer += 2
          # -----------  
            
    return answer        
  # -------------
  
  
# Outer loop is Θ(x)  

# Inner loop is Θ(x)

# Everything else is Θ(1)

 
#  -------    --------------------------   
# | Θ(1) | + | Θ(x)* Θ(x)* Θ(1) + Θ(1) |  
# -------    --------------------------- 
   
    
# Overall complexity is Θ(x^2) by rules of addition and multiplication
        
    
# YOU TRY IT!

# What is the Theta complexity of this program? Careful to describe in
# terms of input    
    
# (hint: what matters with a list, size of elems of length?)    
   
    
def f(L):
    
    Lnew = []
    
    for i in L:
        
        Lnew.append(i ** 2)
        
    return Lnew


# ANSWER:
    
# Loop: Θ(len(L))

# f is Θ(len(L))

# YOU TRY IT!

# What is the Theta complexity of this program?

def f(L, L1, L2):
    
    """ L, L1, L2 are the same length """
    
    inL1 = False
    
    for i in range(len(L)):
        
        if L[i] == L1[i]:
            
            inL1 = True
            
    inL2 = False

    for i in range(len(L)):

        if L[i] == L2[i]:
            
            inL2 = True
            
    return L1 and L2


# ANSWER:

# Loop: Θ(len(L)) + Θ(len(L))

# f is Θ(len(L)) or Θ(len(L1)) or Θ(len(L2))

# COMPLEXITY CLASSES

# We want to design algorithms that are as close to top of this hierarchy
# as possible



#       --
#      |  \
#     |    \         
#    |      \
#   ----------  
#      |  |  
#      |  |
#      |  |
#      |  |        Θ(1) denotes constant running time 
#      |  |
#      |  |        Θ(log n) denotes logarithmic running time
#      |  | 
#      |  |        Θ(n) denotes linear running time
#      |  |
#      |  |        Θ(n log n) denotes log-linear running time
#      |  |
#      |  |        Θ(n^c) denotes polynomial running time (c is a constant)
#      |  | 
#      |  |        Θ(c^n) denotes exponential running time
#      |  |       
#      |  |            (c is a constant raised to a power based on input size)   



# COMPLEXITY GROWTH


    ###############################################################################################         
    #    Class        #    N = 10       #    N = 100       #    N = 1000      #    N = 1000000    #
    ############################################################################################### 
    #  Logarithmic    #      1          #        2         #        3         #          6        #
    ###############################################################################################
    #    Linear       #      10         #        100       #        1000      #       1000000     #
    ###############################################################################################
    #   Log-linear    #      10         #        200       #        3000      #       6000000     #
    ###############################################################################################
    #  Polynomial     #      100        #       10000      #      1000000     #   1000000000000   #
    ###############################################################################################
    #  Exponential    #      1024       #      12676506    #  10715086071862  #                   #
    #                 #                 #      00228229    #  67320948425049  #    Good Luck!!    #
    #                 #                 #      40149670    #  06000181056140  #                   #
    #                 #                 #      3205376     #  48117055336074  #                   #
    #                 #                 #                  #  43750388370351  #                   # 
    #                 #                 #                  #  05112493612249  #                   #
    #                 #                 #                  #  31983788156958  #                   #
    #                 #                 #                  #  58127594672917  #                   #
    #                 #                 #                  #  55314682518714  #                   #
    #                 #                 #                  #  52856923140435  #                   #
    #                 #                 #                  #  98457757469857  #                   #  
    #                 #                 #                  #  48039345677748  #                   #
    #                 #                 #                  #  24230985421074  #                   #
    #                 #                 #                  #  60506237114187  #                   #
    #                 #                 #                  #  79541821530464  #                   #
    #                 #                 #                  #  74983581941267  #                   #
    #                 #                 #                  #  39876755916554  #                   # 
    #                 #                 #                  #  39460770629145  #                   #  
    #                 #                 #                  #  71196477686542  #                   # 
    #                 #                 #                  #  16766042983165  #                   #
    #                 #                 #                  #  26243868372056  #                   # 
    #                 #                 #                  #  68069376        #                   # 
    ###############################################################################################



# SUMMARY

# Timing is machine/implementation/algorithm dependent

# Counting ops is implementation/algorithm dependent

# Order of growth is algorithm dependent

# Compare efficiency of algorithms

    # Notation that describes growth
    
    # Lower order of growth is better
    
    # Independent of machine or specific implementation
    

# Using Theta

    # Describe asymptotic order of growth

    # Asymptotic notation

    # Upper bound and a lower bound


