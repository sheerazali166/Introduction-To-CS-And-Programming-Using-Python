#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 10:02:49 2024

@author: sheeraz
"""

# INHERITANCE

# WHY USE OOP AND CLASSES OF OBJECTS?

# Mimic real life

# Group different objects part of the same type

# Instance: Jelly 1 year old brown

# Instance: 5 years old brown

# Instance: Tiger 2 years old brown

# Instance: Bean 0 years old black

# Instance: 2 years old white 

# Instance: 1 year old b/w


# WHY USE OOP AND CLASSES OF OBJECTS?

# Mimic real life

# Group different objects part of the same type

# All instances of a type have the same data abstration and behaviors

# GROUPS OF OBJECTS HAVE ATTRIBUTES (RECAP)

# Data attributes

    # How can you represent your object with data?

    # What it is

        # for a coordinate: x and y values

        # for an animal: age
        
        
# Procedural attributes (behavior/operations/methods)        
        
# How can someone interact with the object?

# What it does
        
    # for a coordinate: find distance between two

   # for an animal: print how long it’s been alive
   

# HOW TO DEFINE A CLASS (RECAP)

#              name
#  --------  --------  ---------
# | class | | Anmal |(| object |):
# --------  --------  ---------- 
# class definition    class parent 
 

#                       variable to refer to
#                       an instance of the class
    #      -----------  -------   ------
    # def | __init__ |(| self |, | age |):
    #     -----------  -------   ------ 
#         Special method to      What data initializes      
#         create an instance     an animal type
    
        # self.age = age

#       -------------------
#      | self.name = None |
#      --------------------
#      Specal method to create
#      an instance  

 
#  ----------         ------   
# | myAnmal | = Anmal| (3) |
# ----------         ------
# One instance       Mapped to
#                    self.age in
#                    class def
   

# GETTER AND SETTER METHODS

class Animal(object):
    
    def __init__(self, age):
        
        self.age = age
        
        self.name = None
        
    def __str__(self):
        
        return "animal:" + str(self.name) + ":" + str(self.age)
    
    
# Getters and setters should be used outside of class to access
# data attributes


# GETTER AND SETTER METHODS

class Animal(object):

    def __init__(self, age):
        
        self.age = age
        
        self.name = None
        
        
    def __str__(self):
        
        return "animal:" + str(self.name) + ":" + str(self.age)
    
    
    def get_age(self):
  # -----------------      
        
        return self.age
      # ---------------
    
    def get_name(self):
  # ------------------- 
        
        return self.name
      # ----------------
      
      
  # getter


    def set_age(self, newage):
  # -------------------------  
        
        self.age = newage
      # -----------------  
        
    def set_name(self, newname = ""):
  # ---------------------------------      
        
        self.name = newname
      # -------------------  
        
     
   # setter     


# Getters and setters should be used outside of class to access
# data attributes


# AN INSTANCE and DOT NOTATION (RECAP)


# Instantiation creates an instance of an object

a = Animal(3)

# Dot notation used to access attributes (data and methods) though it is
# better to use getters and setters to access data attributes

a.age
# ---
# - access data attribute allowed, but not recommended

a.get_age()
# ---------
# - access method - best to getters and setters


# INFORMATION HIDING


# Author of class definition may change data attribute variable names


class Animal(object):
    
    def __init__(self, age):
        
        self.years = age
      # ----------  
      # Replaced age data attrbute by years 


    def get_age(self):
        
        return self.years
    
    
# If you are accessing data attributes outside the class and class definition
# changes, may get errors    

# Outside of class, use getters and setters instead

# Use a.get_age() NOT a.age

# good style

# easy to maintain code

# prevents bugs


# CHANGING INTERNAL REPRESENTATION

class Animal(object):
    
    def __init__(self, age):
        
        self.years = age
      # ----------------  
      # Change internal rep from self.age = age
      
        self.name = None
        
        
    def __str__(self):
        
        return "animal:" + str(self.name) + ":" + str(self.age)
           
    
    def get_age(self):
        
        return self.years
    
    def set_age(self, newage):
        
        self.years = newage
    

# a = Animal(3)
    
# a.get_age()  # works        
# ---------        

# a.age   error
# -----


# Accessing methods works correctly, but accessing data attributes
# no longer works.
    

# Getters and setters should be used outside of class to access
# data attributes


# PYTHON NOT GREAT AT INFORMATION HIDING

# Allows you to access data from outside class definition

print(a.age)


# Allows you to write to data from outside class definition
a.age = "infinite"


print(a.age)


# Allows you to create data attributes for an instance from outside
# class definition

a.size = "tiny"


print(a.size)


# It’s not good style to do any of these!

# USE OUR NEW CLASS

def animal_dict(L):
    
    """ L is a list
        Returns a dict, d, mapping an int to an Animal object.
        A key in d is all non-negetive ints, n, in L. A value
        corresponding to a key is an Animal object with n as its age. """
        
       
    d = {}

    for n in L:
        
        if type(n) == int and n >= 0:
            
            d[n] = Animal(n)
          # ----------------
          # Invoke the name of the class with parameter n
          # (i.e. the age of that animal) 
            
    return d


#       ----   ----            ----
# L = [| 2 |, | 5 |, "a", -5, | 0 |]        
#      ----   ----            ----


# USE OUR NEW CLASS

# Python doesn’t know how to call print recursively

def animal_dict(L):
    
    """ L is a list
        Returns a dict, d, mapping an int to an Animal object.
        A key in d is all non-negetive ints n L. A value corresponding
        to a key is an Animal object with n as its age. """
        
     
    d = {}

    for n in L:
        
        if type(n) == int and n >= 0:
            
            d[n] = Animal(n)
            
    return d



L = [2, 5, "a", -5, 0]        


animals = animal_dict(L)
        # --------------
        # Return is a dict mapping int: Animal 
        
print(animals)        
# ------------
# {2: <__main__.Animal object at 0x137e031d0>,
# 5: <__main__.Animal object at 0x137e01c10>, 
# 0: <__main__.Animal object at 0x137e02750>}


# USE OUR NEW CLASS

class Animal(object):
    
    def __init__(self, age):
        
        self.age = age
      # ----------------  
      # Change internal rep from self.age = age
      
        self.name = None
        
        
    def __str__(self):
        
        return "animal:" + str(self.name) + ":" + str(self.age)
           
    
    def get_age(self):
        
        return self.years
    
    def set_age(self, newage):
        
        self.years = newage



def animal_dict(L):
    
    """ L is a list
        Returns a dict, d, mappping an int to an Animal object.
        A key in d is all non-negative ints n L. A value corresponding
        to a key is an Animal object with n as its age. """


    d = {}
    
    for n in L:
        
        if type(n) == int and n >= 0:
            
            d[n] = Animal(n)
            
    return d


L = [2, 5, "a", -5, 0]

animals = animal_dict(L)


for n, a in animals.items():
# --------------------------
    
    print(f"key {n} with val {a}")
  # ------------------------------
  
# Manually loop over animal objects and process ther data attr through
# getter methods 
  
# key 2 with val animal:None:2
# key 5 with val animal:None:5
# key 0 with val animal:None:0


# YOU TRY IT!


# Write a function that meets this spec.

def make_animals(L1, L2):
    
    """ L1 is a list of ints and L2 is a list of str L1 and L2 have the same
        length Creates a list of Animals the same length as L1 and L2. An
        animal object at index i has the age and name corresponding to the
        same index in L1 and L2, respectively. """

     
    

# For example:

L1 = [2, 5, 1]

L2 = ["blobfish", "crazyant", "parafox"]

animals = make_animals(L1, L2)  

print(animals)  # note this prints a list of animal objects   

# for i in animals: # this loop prints the individual animals
    
     # print(i)
     
     
# BIG IDEA


# Access data attributes (stuff defined by self.xxx) through methods – it’s
# better style.


# HIERARCHIES

# Parent class (superclass)

# Child class

# (subclass)

# Inherits all data and behaviors of parent class

# Add more info

# Add more behavior

# Override behavior 




                                    ###################
                                    #                 #
                                    #                 #
                                    #                 #◀︎-----------------
#                  ----------------▶︎#      Anmal      #                  |   
#                 |                 #                 #                  |      
#                 |                 #                 #                  |
#                 |                 #                 #                  |
#                 |                 ###################                  |             
#                 |                          ▲                           |
#                 |                          |                           |
#                 |                          |                           |
#                 |                          |                           |
#                 |                          |                           |
         ###################        ###################        ###################
         #                 #        #                 #        #                 #
         #                 #        #                 #        #                 #
         #                 #        #                 #        #                 #
         #     Person      #        #       Cat       #        #      Rabbit     #  
         #                 #        #                 #        #                 #
         #                 #        #                 #        #                 #
         #                 #        #                 #        #                 #
         ###################        ###################        ################### 
#                ▲
#                | 
#                |
#                |
#                -----------------------------
#                                            |
#                                            |
#                                            |
                                    ###################
                                    #                 #
                                    #                 #
                                    #                 #
                                    #     Student     #    
                                    #                 #
                                    #                 #
                                    #                 #
                                    ################### 
        
    
    
    
# INHERITANCE: PARENT CLASS    
    

class Animal(object):
          # --------
          # - everythng is an object - class object implements basic 
          # operations in Python, like binding variables, etc 
    
    def __init__(self, age):
        
        self.age = age
        
        self.name = None
        
    def get_age(self):
        
        return self.age
    
    def get_name(self):
        
        return self.name

    def set_age(self, newage):
        
        self.age = newage
        
    def set_name(self, newname = ""):
        
        self.name = newname
        
    def __str__(self):
        
        return "animal:" + str(self.name) + ":" + str(self.age)
    
    
# SUBCLASS CAT

# INHERITANCE: SUBCLASS 

 
class Cat(Animal):
       # -------
       # Inherits all attributes of Animal:
       # __init__()
       # age, name
       # get_age(), get_name()
       # set_age(), set_name()
       # __str__()
       
       def speak(self):
     # ----------------
     # Add new functionality via speak method     
           
           print("meow")
           
       def __str__(self):
     # ------------------
     # Overrides __str__
     
           return "cat:" + str(self.name) + ":" + str(self.age)
       
        
# Add new functionality with speak()

    # Instance of type Catcan be called with new methods

    # Instance of type Animal throws error if called with Cat’s new method           
           
    
# __init__ is not missing, uses the Animalversion

# WHICH METHOD TO USE?

# Subclass can have methods with same name as superclass

# For an instance of a class, look for a method name in current class
# definition

# If not found, look for method name up the hierarchy (in parent, then
# grandparent, and so on)

# Use first method up the hierarchy that you found with that method name

# SUBCLASS PERSON

class Person(Animal):
          # --------
          # Parent class is Animal
    
    
    def __init__(self, name, age):
        
        Animal.__init__(self, age)
      # --------------------------
      # Call Animal constructor to run lines of code in Animal's init
        
        self.set_name(name)
      # -------------------
      # Call Animal's method
        
        self.friends = []
      # -----------------
      # Add a new data attributes
   
    
    def get_frends(self):         ################
  # ---------------------                        # 
                                                 #
        return self.friends.copy()               #
      # --------------------------               #
                                                 #
                                                 #
    def add_friend(self, fname):                 #
  # ----------------------------                 #    
                                                 #
        if fname not in self.friends:            #-----------> new methods
                                                 #
            self.friends.append(fname)           #
                                                 #
    def speak(self):                             #
  # ----------------                             #  
                                                 #
        print("hello")                           # 
                                                 #
                                                 #
    def age_diff(self, other):                   #
  # --------------------------     ###############
        
        diff = self.age - other.age

        print(abs(diff), "year difference")

     
    def __str__(self):
  # ------------------
  # Override Animal's __str__ method    
        
        return "person:" + str(self.name) + ":" + str(self.age)
    
    
# YOU TRY IT!

# Write a function according to this spec.

def make_pets(d):
    
    """ d is a dict mapping a Person obj to a Cat obj Prints, on each line,
        the name of a person, a colon, and the name of that person's cat """

    pass

p1 = Person("ana", 86)
p2 = Person("james", 7)
c1 = Cat(1)
c1.set_name("furball")
c2 = Cat(1)
c2.set_name("fluffsphere")
  
d = {p1:c1, p2:c2}
make_pets(d) # prints ana:furball

# james:fluffsphere  


# BIG IDEA

# A subclass can use a parent’s attributes, override a parent’s attributes, 
# or define new attributes.

# Attributes are either data or methods.

# SUBCLASS STUDENT

import random
# -----------
# Bring in functions from random library


class Student(Person):
            # -------- 
            # Inherits Person and Animal attributes 
            
    def __init__(self, name, age, major = None):

        Person.__init__(self, name, age)
      # --------------------------------
      # Person __init__ takes care of all initializations
      
        self.major = major
      # ------------------  
      # Adds new data
      
    def change_major(self, major):
        
        self.major = major
        
    def speak(self):
        
        r = random.random()
          # ---------------
          # - I looked up how to use the random library in the python docs
          # - random() method gives back float in [0, 1]
         
        if r < 0.25:
             
            print("i have homework")
             
        elif 0.25 <= r < 0.5:
             
            print("i need sleep")
          
        elif 0.5 <= r < 0.75:
            
            print("i should eat")
            
        else:
            
            print("i'm still zooming")
            
    def __str__(self):

        return "student:" + str(self.name) + ":" + str(self.age) + ":" + str(self.major)
    
    
# SUBCLASS RABBIT

# CLASS VARIABLES AND THE Rabbit SUBCLASS

# Class variables and their values are shared between all instances of
# a class         
            
class Rabbit(Animal):
           # -------
           # parent class
           
    tag = 1
  # ---
  # Shared class variable           
                
    def __init__(self, age, parent1 = None, parent2 = None):

        Animal.__init__(self, age)

        self.parent1 = parent1
        
        self.parent2 = parent2
        
        self.rid = Rabbit.tag
      # --------   ----------
      # instance   Access shared class variable
      # variable
        
        Rabbit.tag += 1
      # ---------------
      # Incrementing class variable changes it for all instances that may
      # reference it
      
      
# tagused to give unique id to each new rabbit instance      
        
# RECALL THE __init__ OF Rabbit        
         
      
def __init__(self, age, parent1 = None, parent2 = None):

    Animal.__init__(self, age)

    self.parent1 = parent1
    
    self.parent2 = parent2
 
    self.rid = Rabbit.tag
    
    Rabbit.tag += 1

r1 = Rabbit(8)



                                                ###########
#                          -----▶︎  Rabbit.tag   #    2    #
#                         |                     ###########
#                         |                       
#                         |                             
#                         |                     ################### 
#  Shared across all      |                     #  Age: 8         #
#  instances         ------                     #  Parent1: None  #
#                                       r1      #  Parent2: None  #
                                                #  Rid: 1         #
                                                ###################     
      
      
   
# RECALL THE init OF Rabbit      
        

def __init__(self, age, parent1 = None, parent2 = None):

    Animal.__init__(self, age) 

    self.parent1 = parent1       
        
    self.parent2 = parent2        
            
    self.rid = Rabbit.tag
    
    Rabbit.tag += 1
    
    
r1 = Rabbit(8)

r2 = Rabbit(6)

    

                                                ###########
#                          -----▶︎  Rabbit.tag   #    3    #
#                         |                     ###########
#                         |                       
#                         |                             
#                         |                     ################### 
#  Shared across all      |                     #  Age: 8         #
#  instances         ------            r1       #  Parent1: None  #
                                                #  Parent2: None  #
                                                #  Rid: 1         #
                                                ################### 
                                                
                                                
                                                ################### 
                                                #  Age: 6         #
#                                       r2      #  Parent1: None  #
                                                #  Parent2: None  #
                                                #  Rid: 2         #
                                                ################### 
    
    
    
 
# RECALL THE init OF Rabbit    
    

def __init__(self, age, parent1 = None, parent2 = None):
    
    Animal.__init__(self, age)
    
    self.parent1 = parent1
    
    self.parent2 = parent2
    
    self.rid = Rabbit.tag
    
    Rabbit.tag += 1
    
    
    

                                                ###########
#                          -----▶︎  Rabbit.tag   #    4    #
#                         |                     ###########
#                         |                       
#                         |                             
#                         |                     ################### 
#  Shared across all      |                     #  Age: 8         #
#  instances         ------            r1       #  Parent1: None  #
                                                #  Parent2: None  #
                                                #  Rid: 1         #
r1 = Rabbit(8)                                  ################### 
                                                
r2 = Rabbit(6)                                                
                                                ################### 
r3 = Rabbit(10)                                 #  Age: 6         #
#                                       r2      #  Parent1: None  #
                                                #  Parent2: None  #
                                                #  Rid: 2         #
                                                ################### 
                                                
                                                
                                                ################### 
                                                #  Age: 10        #
#                                       r3      #  Parent1: None  #
                                                #  Parent2: None  #
                                                #  Rid: 3         #
                                                ################### 
    
    
# RabbitGETTER METHODS

class Rabbit(Animal):

    tag = 1

    def __init__(self, age, parent1 = None, parent2 = None):
        
        Animal.__init__(self, age)
        
        self.parent1 = parent1
        
        self.parent2 = parent2
    
        self.rid = Rabbit.tag
        
        Rabbit.tag += 1
    
    def get_rid(self):
  # ------------------  
        
        return str(self.rid).zfill(5)
      # -----------------------------
      #                      --------
      #                      Method on a string to pad the beginning with
      #                      zeros for example, 00001 not 1
    
    
    
    def get_parent1(self):
  # ----------------------    
        
        return self.parent1
      # -------------------
      
    
    def get_parent2(self):
  # ---------------------     
        
        return self.get_parent2
      # -----------------------
      # - getter methods specfic for a Rabbit class - there are also getters
      # get_name and get_age inherited from Animal
        
    
      
# WORKING WITH YOUR OWN TYPES    
    
    
def __add__(self, other):

    # returning object of same type as this class
    
    return Rabbit(0, self, other) 
#                 ▲   ▲      ▲ 
#                 |   |      |
#                 |   |      |
#                 |   |      --------------------------
#                 |   |                                |
#                 |   -------------------              |
#                 |                      |             |
#                  ---------------       |             | 
#                                 |      |             | 
#                                 |      |             |
# recall Rabbit’s __init__(self, age, parent1=None, parent2=None)         
          
         
        
# Define + operator between two Rabbitinstances


# Define what something like this does: r4 = r1 + r2

    # where r1and r2are Rabbitinstances

        
# r4is a new Rabbitinstance with age 0

# r4has selfas one parent and otheras the other parent

# In __init__, parent1and parent2are of type Rabbit


# RECALL THE init OF Rabbit

def __init__(self, age, parent1 = None, parent2 = None):
    
    Animal.__init__(self, age)
    
    self.parent1 = parent1
    
    self.parent2 = parent2
    
    self.rid = Rabbit.tag
    
    Rabbit.tag += 1

        

                                                ###########
#                          -----▶︎  Rabbit.tag   #    5    #
#                         |                     ###########
#                         |                       
#                         |                             
#                         |                     ################### 
#  Shared across all      |                     #  Age: 8         #
#  instances         ------            r1       #  Parent1: None  #
                                                #  Parent2: None  #
                                                #  Rid: 1         #
r1 = Rabbit(8)                                  ################### 
                                                
r2 = Rabbit(6)                                                
                                                ################### 
r3 = Rabbit(10)                                 #  Age: 6         #
#                                       r2      #  Parent1: None  #
                                                #  Parent2: None  #
                                                #  Rid: 2         #
r4 = r1 + r2                                    ################### 
   # -------                                                  
   # Rabbit(0, r1, r2)                                                
                                                
                                                ################### 
                                                #  Age: 10        #
#                                       r3      #  Parent1: None  #
                                                #  Parent2: None  #
                                                #  Rid: 3         #
                                                ################### 
                                                
                                                
                                                
                                                ############################## 
                                                #  Age: 0                    #
#                                       r4      #  Parent1: obj bound to r1  #
                                                #  Parent2: obj bound to r2  #
                                                #  Rid: 3                    #
                                                ############################## 
        
         

# SPECIAL METHOD TO COMPARE TWO Rabbits         
      
# Decide that two rabbits are equal if they have the same two parents

# def __eq__(self, other):

    # parents_same = (self.p1.rid == oth.p1.rid and self.p2.rid == oth.p2.rid)       
    # ------------  
    
    # parents_opp = (self.p2.rid == oth.p1.rid and self.p1.rid == oth.p2.rid)       
    # -----------  
    # Booleans checking r1 + r2 or r2 + r1    
        
        
# Compare ids of parents since ids are unique (due to class var)

# Note you can’t compare objects directly

           
    # For ex. with self.parent1 == other.parent1       
       
    # This calls the __eq__method over and over until call it on Noneand    
    
    # gives an AttributeErrorwhen it tries to do None.parent1 
    
    
# BIG IDEA    
    
# Class variables are shared between all instances.    
    
# If one instance changes it, it’s changed for every instance.        
        
        
# OBJECT ORIENTED PROGRAMMING        
    

# Create your own collections of data

# Organize information

# Division of work        
        
# Access information in a consistent manner    
    

# Add layers of complexity

# Hierarchies

# Child classes inherit data and methods from parent classes

# Like functions, classes are a mechanism for decomposition and abstraction
# in programming
