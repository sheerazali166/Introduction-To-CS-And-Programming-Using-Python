#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 05:35:44 2024

@author: sheeraz
"""


# FITNESS TRACKER OBJECT ORIENTED PROGRAMMING EXAMPLE



#              IMPLEMENTING                                   USING
#              THE CLASS                  vs                  THE CLASS


#                                         #
#                                         # 
#        Implementing a new               #        Using the new object type in
#        object type with a class         #        code
#                                         #
#        Define the class                 #            Create instances of the
#                                         #            object type
#        Define data attributes           #
#        (WHAT IS the object)             #            Do operations with them
#                                         #
#        Define methods                   #
#        (HOW TO use the object)          #
#                                         #        Instances have specific
#                                         #        values for attributes
#        Class abstractly captures        #
#        common properties and            #
#        behaviors                        #
#                                         #
#                                         #


# Two different coding perspectives


# Workout Tracker Example

# Suppose we are writing a program to track workouts, e.g., for a smart watch


# Fitness Tracker


# Common properties:
  
#   Icon      Kind
#   Date      Start Time
#   End       Time Calories
#   Heart     Rate Distance    
    
    

# Swimming Specific:    
    
#   Swimming Pace    
#   Stroke Type    
#   100 yd Splits


# Running Specific:
    
# Cadence
# Running Pace
# Mile Splits
# Elevation    


# GROUPS OF OBJECTS HAVE ATTRIBUTES (RECAP)


# Data attributes

# How can you represent your object with data?

# What it is

# for a coordinate: x and y values

# for a workout: start time, end time, calories

# Functional attributes (behavior/operations/methods)

# How can someone interact with the object?

# What it does

# for a coordinate: find distance between two

# for a workout: display an information card


# DEFINE A SIMPLE CLASS (RECAP)


class Workout(object):
# --- ------- ------    
# class  name    class parent  
# defnition 

              
       
    def __init__(self, start, end, calories):
#      --------  ----  --------------------
#  "constructor"   variable     Start and end   
#  special method  to refer     time, and calories
#  create an       to an        burned
#  instance        instance
#                  of the 
#                  class          


        self.start = start
        
        self.end = end
        
        self.calories = calories
        
        self.icon = "😓"
      # -----------------
      
        self.kind = "Workout"
      # ---------------------
      
      # Icon and kind are attributes even though an instance is not 
      # initialized with them as a params (And python strings can contain
      # emojis!)   
        
my_workout = Workout("9/30/2021 1:35 PM", "9/30/2021 1:57 PM", 200)
# ----------           --------------------  ------------------  ---
# one instance            Mapped to start, end calories in constructor
        
        

# GETTER AND SETTER METHODS (RECAP)        


class Workout(object):
    
    def __init__(self, start, end, calories):
        
        self.start = start
        
        self.end = end
        
        self.calories = calories
        
        self.icon = "😓"
        
        self.kind = "Workout"
        
    
    def get_calories(self):
  # -----------------------
     
        return self.calories
      # --------------------
   
    def get_start(self):
  # --------------------      
       
        return self.start
      # ----------------- 
   
    def get_end(self):
  # -----------------        
       
        return self.end
      # ---------------
        
      
    # getter    
      
        
      
    
    def set_calories(self, calories):
  # ---------------------------------       
        
        self.calories = calories
      # ------------------------  
        
        
    def set_start(self, start):
  # ---------------------------      
        
        self.start = start
      # ------------------  
        
    def set_end(self, end):
  # -----------------------      
        
        self.end = end
      # --------------    
        
        
    # setter


# Getters and setters used outside of class to access data attributes


# SELF PROVIDES ACCESS TO CLASS STATE        
        
       
my_workout = Workout("9/30/2021 1:35 PM", "9/30/2021 1:57 PM", 200)

        
        
        
#################################################################        #################################################################
#                                                               #        #                                                               #
#                                                               #        #                                                               # 
#               ------------------------------------------------#--------#---------------                                                #
#              |                                                #        #              |                                                #  
#              ▼                                                #        #              |                                                #
#    #####################        ##########################    #        #    #####################        ##########################    #
#    #                   #        #                        #    #        #    #                   #        #                        #    # 
#    #                   #        #                        #    #        #    #                   #        #                        #    #
#    #                   #        #  ####################  #    #        #    #                   #        #  ####################  #    #
#    #      Workout      #        #  #  get_calories()  #  #    #        #    #    my_workout     #        #  #                  #  #    #
#    #                   #        #  ####################  #    #        #    #                   #        #  #      start       #  #    # 
#    #       Class       #        #  ####################  #    #        #    #    an instance    #        #  #                  #  #    # 
#    #                   #        #  #    get_start()   #  #    #        #    #                   #        #  ####################  #    #                                                           
#    #                   #        #  ####################  #    #        #    #                   #        #  ####################  #    #
#    #                   #        #  ####################  #    #        #    #                   #        #  #                  #  #    # 
#    #     ⚫️----        #        #  #     get_end()    #  #    #        #    #         ⚫️---      #        #  #       end        #  #    #
#    #           |       #        #  ####################  #    #        #    #             |     #        #  #                  #  #    #                                                     
#    #           |       #        #                        #    #        #    #             |     #        #  ####################  #    #
#    #           |       #        #  ####################  #    #        #    #             |     #        #  ####################  #    #
#    #           --------#--------#-▶︎#  set_calories()  #  #    #        #    #             |     #        #  #                  #  #    # 
#    #                   #        #  ####################  #    #        #    #             ------#--------#-▶︎#     calories     #  #    # 
#    #                   #        #  ####################  #    #        #    #                   #        #  #                  #  #    #
#    #                   #        #  #    set_start()   #  #    #        #    #                   #        #  ####################  #    #
#    #                   #        #  ####################  #    #        #    #                   #        #  ####################  #    #
#    #                   #        #  ####################  #    #        #    #                   #        #  #                  #  #    #
#    #####################        #  #     set_end()    #  #    #        #    #####################        #  #      icon        #  #    #               
#                                 #  ####################  #    #        #                                 #  #                  #  #    #
#                                 #                        #    #        #                                 #  ####################  #    #
#                                 #                        #    #        #                                 #  ####################  #    #    
#                                 #  ###################   #    #        #                                 #  #                  #  #    #
#                                 #  #    __init__()   #   #    #        #                                 #  #      kind        #  #    #     
#                                 #  ###################   #    #        #                                 #  #                  #  #    # 
#                                 #                        #    #        #                                 #  ####################  #    # 
#                                 #                        #    #        #                                 #                        #    #                                                
#                                 #                        #    #        #                                 #                        #    #                                                                                                    
#                                 ##########################    #        #                                 ##########################    #        
#                                                               #        #                                                               #
#                                                               #        #                                       Instance State          #
#                                                               #        #                                       Dictionary              #
#                                      Class State              #        #                                                               #
#                                      Dictionary               #        #                                                               # 
#                                                               #        #                                       Accessed via            #
#                                                               #        #                                       “self” keyword          #
#                                                               #        #                                                               #
#                                                               #        #                                                               #
#                                                               #        #                                                               #
#                                                               #        #                                                               #
#################################################################        #################################################################


        
# AN INSTANCE and DOT NOTATION (RECAP)
        
 
# Instantiation creates an instance of an object        
        
        
myWorkout = Workout("9/30/2021 1:35 PM", "9/30/2021 1:57 PM", 200)         
        
        

# Dot notation used to access attributes (data and methods)

# It’s better to use getters and setters to access data attributes        
        
print(myWorkout.calories)
# -----------------------
# - access data attribute directly   
# - allowed, but not recommended 


print(myWorkout.get_calories())        
# -----------------------------
# - access attribute via method         
# - better, because it supports         
# information hiding        
        
        
        
# WHY INFORMATION HIDING?

# Keep the interface of your class as simple as possible

# Use getters & setters, not attributes

    # i.e., get_calories() method NOT caloriesattribute
    # Prevents bugs due to changes in implementation


# May seem inconsequential in small programs, but for large programs complex
# interfaces increase the potential for bugs

# If you are writing a class for others to use, you are committing to
# maintaining its interface!


        
# CHANGING THE CLASS IMPLEMENTATION       


# Author of class definition may change internal representation or
# implementation
         
    # Use a class variable
    
    # Now get_calories estimates calories based of workout duration if
    # calories are not passed in


# If accessing data attributes outside the class and class implementation
# changes, may get errors


# CHANGING THE CLASS IMPLEMENTATION

import dateutil, datetime



# class Workout:
    
    # cal_per_hour = 200
  # ------------------
  # Class variable - all instances of Workout can read this  
    
    
    # def __init__(self, start, end, calories = None):
                                 # ---------------
                                 # Defaults to None if not passed in
                                 
        # self.start = datetime.parser.parse(start)
       # -----------------------------------------  
        
        # self.end = datetime.parser.parse(end)
       # -------------------------------------  
      
     # self.start and self.end are objects of type datetime, not strings 
        
        # self.calories = calories # may be None
        
        # self.icon = "😓"
        
        # self.kind = "Workout"
        
        
    # def get_calories(self):

        # if (calories == None):
        # ----------------------    
            
            # return Workout.cal_per_hour * (self.end - self.start).total_seconds() / 3600 
            # ----------------------------------------------------------------------------
                                          # ---------------------------
                                          # Allowed on datetime objects
                                          
        # If calories was not passed in, estimate based on elapsed time

                                   
        # else:
        # -----    
            
            # return self.calories
            # --------------------
            
            
        # If calories was passed in, just use that value    
            
            

# ASIDE: datetime OBJECTS OTHER PYTON LIBRARIES        
        

# Takes the string representing the date and time and converts it to
# a datetimeobject
                                        
  
# from dateutil import parser        
# ---------------------------
#  Brings in a bunch of functions and classes


# start = '9/30/2021 1:35 PM'

# end = '9/30/2021 1:45 PM'


# start_date = parser.parse(start)

# end_date = parser.parse(end)

# type(start_date)
# ----------------
# Type is datetime.datetime 

 
# Why do this? Because it makes operations with dates easy! The datetime
# object takes care of everything   
    
 
# print((end_date-start_date).total_seconds())
# --------------------------------------------    
#   Prints 600    
  
    
  
#################################################################        #################################################################
#                                                               #        #                                                               #
#                                                               #        #                                                               # 
#               ------------------------------------------------#--------#---------------                                                #
#              |                                                #        #              |                                                #  
#              ▼                                                #        #              |                                                #
#    #####################        ##########################    #        #    #####################        ##########################    #
#    #                   #        #                        #    #        #    #                   #        #                        #    # 
#    #                   #        #                        #    #        #    #                   #        #                        #    #
#    #                   #        #  ####################  #    #        #    #                   #        #  ####################  #    #
#    #      Workout      #        #  #  get_calories()  #  #    #        #    #    my_workout     #        #  #                  #  #    #
#    #                   #        #  ####################  #    #        #    #                   #        #  #      start       #  #    # 
#    #       Class       #        #  ####################  #    #        #    #    an instance    #        #  #                  #  #    # 
#    #                   #        #  #    get_start()   #  #    #        #    #                   #        #  ####################  #    #                                                           
#    #                   #        #  ####################  #    #        #    #                   #        #  ####################  #    #
#    #                   #        #  ####################  #    #        #    #                   #        #  #                  #  #    # 
#    #     ⚫️----        #        #  #     get_end()    #  #    #        #    #         ⚫️---      #        #  #       end        #  #    #
#    #           |       #        #  ####################  #    #        #    #             |     #        #  #                  #  #    #                                                     
#    #           |       #        #                        #    #        #    #             |     #        #  ####################  #    #
#    #           |       #        #  ####################  #    #        #    #             |     #        #  ####################  #    #
#    #           --------#--------#-▶︎#  set_calories()  #  #    #        #    #             |     #        #  #                  #  #    # 
#    #                   #        #  ####################  #    #        #    #             ------#--------#-▶︎#     calories     #  #    # 
#    #                   #        #  ####################  #    #        #    #                   #        #  #                  #  #    #
#    #                   #        #  #    set_start()   #  #    #        #    #                   #        #  ####################  #    #
#    #                   #        #  ####################  #    #        #    #                   #        #  ####################  #    #
#    #                   #        #  ####################  #    #        #    #                   #        #  #                  #  #    #
#    #####################        #  #     set_end()    #  #    #        #    #####################        #  #      icon        #  #    #               
#                                 #  ####################  #    #        #                                 #  #                  #  #    #
#                                 #                        #    #        #                                 #  ####################  #    #
#                                 #                        #    #        #                                 #  ####################  #    #    
#                                 #  ###################   #    #        #                                 #  #                  #  #    #
#                                 #  #    __init__()   #   #    #        #                                 #  #      kind        #  #    #     
#                                 #  ###################   #    #        #                                 #  #                  #  #    # 
#                                 #                        #    #        #                                 #  ####################  #    # 
#                                 #                        #    #        #                                 #                        #    #                                                
#                                 #  ###################   #    #        #                                 #                        #    #                                                                                                    
#                                 #  #   cal_per_hour  #   #    #        #                                 ##########################    #        
#                                 #  ###################   #    #        #                                                               #
#                                 #                        #    #        #                                       Instance State          #
#                                 #                        #    #        #                                       Dictionary              #
#                                 ##########################    #        #                                                               #
#                                                               #        #                                                               # 
#                                                               #        #                                       Accessed via            #
#                                                               #        #                                       “self” keyword          #
#                                     Class State               #        #                                                               #
#                                                               #        #                                                               #
#                                     Dictionary                #        #                                                               #
#                                                               #        #                                                               #
#                                                               #        #                                                               #
#                                                               #        #                                                               #
#                                                               #        #                                                               #
#                                                               #        #                                                               #                                                            #
#                                                               #        #                                                               #
#################################################################        #################################################################

 


# CLASS VARIABLES

# Associate a class variable with all instances of a class

# Warning: if an instance changes the class variable, it’s changed for all
# instances


# class Workout:
    
    # cal_per_hr = 200
    # ----------------
    # cal_per_hour is set to 200 for all new instances of Workout
    
    # def __init__(self, start, end, calories):


# print(Workout.cal_per_hr)
# -------------------------
# No instance, required prints 200 

# w = Workout('1/1/2021 2:34', '1/1/2021 3:35', None)


# print(w.cal_per_hr)
# -------------------
# Prints 200

# Workout.cal_per_hr = 250

# print(w.cal_per_hr)
# -------------------
# Prints 250

# Bad style to change the class variable outside the class definition Write
# a method to do it!

# YOU TRY IT!
 
 
# Write lines of code to create two Workout objects.

# One Workout object saved as variable w_one, from Jan 1 2021 at 3:30 PM
# until 4 PM.

# You want to estimate the calories from this workout.
# Print the number of calories for w_one.   
  
# Another Workout object saved as w_two, from Jan 1 2021 at 3:35 PMuntil 4 PM.    
  

# You know you burned 300calories for this workout.
# Print the number of calories for w_two.    
   
  
    
  
    
                              ###################  
                              #     Vehicle     #
                              ###################
#                                 ▲    ▲    ▲ 
#                                 |    |    |
#                                 |    |    |
#              -------------------     |    ---------------------
#             |                        |                        |
#             |                        |                        |
#             |                        |                        | 
#             |                        |                        |
     ###################      ###################      ###################  
     #       Car       #      #      Plane      #      #      Boat       #
     ###################      ###################      ###################
#             ▲
#             |
#             |
#             |
#             |
#             |
#             |
    ######################
    #      Race Car      #  
    ######################
    
  
    
  
    
  

                              ###################  
                              #      Animal     #
                              ###################    
#                                     |   |
#                                     |   |
#                                     |   |
#                          -----------    ----------
#                         |                         |
#                         |                         | 
#                         |                         |
                  ##################        ##################         
                  #      Fish      #        #     Mammal     #
                  ##################        ################## 
#                                                  |    |
#                                                  |    |
#                                                  |    |
#                                           -------     -------------
#                                          |                         |
#                                          |                         |
#                                          |                         |
                                  ##################        ##################         
                                  #       Cat      #        #       Dog      #
                                  ##################        ################## 
                                
  
    
  
    
                      
  
                                             ##
                                            #  #
                                           #    #
                                          #      #
                                         #  King  #
#                                     🚫#          #
                                       #------------#
                                      #              # 
                                     #     Nobles     # 
                                    #       🚫         # 
                                   #------------------- #
                                  #                      #
                                 #         Knights        #                            
                                #                 🚫       #
                               #----------------------------#
                              #                              #  
                             #            Peasants      🚫    #
                            #                                  #
                            ####################################
#                                                             🚫
  
    
  

# HIERARCHIES

# Parent class
# (superclass)  
  
# Child class
# (subclass)

    # Inherits all data and 
    # behaviors of parent
    # class


# Add more info

# Add more behavior

# Override behavior




                            #####################
                            #                   #
                            #                   #
                            #      Workout      #
                            #                   #
                            #                   #
                            #####################
#                                   ▲    ▲ 
#                                   |    |
#                                   |    |
#                       ------------      ------------
#                      |                             |
#                      |                             |
            #####################          #####################
            #                   #          #                   #
            #      Outdoor      #          #      Indoor       #
            #      Workout      #          #      Workout      # 
            #                   #          #                   #
            #                   #          #                   #
            #####################          #####################
#                   ▲   ▲                           ▲    ▲
#                   |   |                           |    |
#                   |   |                           |    |
#                ---     ---------------            |    |
#               |                      |            |    |  
#               |                      |            |    |
      #####################  #####################  |    |
      #                   #  #                   #  |    | 
      #                   #  #                   #  |    |
      #      Running      #  #      Swimming     #  |    |
      #                   #  #                   #  |    |
      #                   #  #                   #  |    |
      #####################  #####################  |    |
#                                                   |    |
#                                                   |    |
#                                             ------     ------------    
#                                            |                      |
#                                            |                      | 
                                   #####################  ##################### 
                                   #                   #  #                   #
                                   #                   #  #                   #
                                   #     Treadmill     #  #       Weights     #
                                   #                   #  #                   #
                                   #                   #  #                   #
                                   #####################  #####################





# Common properties:
  
#   Icon      Kind        
#   Date      Start Time
#   End       Time Calories
#   Heart     Rate Distance    
    
    
    
    
    ##################
    #                #
    #                #
    #    Workout     #
    #                #
    #  "Superclass"  #
    #                #
    #                #
    ##################
    
    
    

# Swimming Specific:    
    
#   Swimming Pace    
#   Stroke Type    
#   100 yd Splits


    ##################
    #                #
    #                #
    #   Swimming     #
    #                #
    #   "Subclass"   #
    #                #
    #                #
    ##################



# Running Specific:
    
# Cadence
# Running Pace
# Mile Splits
# Elevation 


    ##################
    #                #
    #                #
    #    Running     #
    #                #
    #  "Subclass"    #
    #                #
    #                #
    ##################


# INHERITANCE:
# PARENT CLASS


#                ---------
# class Workout(| object |):
#               --------- 
    
    # cal_per_hr = 200
    
    # def __init__(self, start, end, calories=None):
     
        # …
        
        
#  Everything is an object

# Class objectimplements basic operations in Python, e.g., binding variables        
        
        
# INHERITANCE: SUBCLASS        

#                  -----------
# class RunWorkout|(Workout):|
#                 ------------
                # Parent is Workout Inherits all attributes of Workout:
                # start, and, calories, get calories(), get_start()
                # get_end(), ... , __str__()
                
                
      # def __init__(self, start, end, elev=0, calories=None):                

#            --------          ---------------------
          # |super()|.__init__|(start,end,calories)|
#           --------          --------------------- 
#           Parents Accessed    Initialize the parent class
#           via super()         (Workout)
 
    
  
#               ----------------------
            #  |self.icon = '🏃'     | 
            #  |self.kind = 'Running'|
#              ----------------------
            #  Add new instance variables

#               ----------------- 
#              |self.elev = elev|  
#              ------------------
#              Override parent default


#     ------------------------------
#    |  def get_elev(self):         |
#    |                              |
#    |      return self.elev        |    Add new functionality
#    |      def set_elev(self, e):  |
#    |      self.elev = e           |  
#    -------------------------------- 


# Add new functionality e.g., get_elev()

# New methods can be called on instance of type RunWorkout

# __init__ uses super()to setup Workout base instance (can also call
# Workout.__init__(start,end,calories) directly



#################################################################        #################################################################
#                                                               #        #                                                               #
#                                                               #        #                                                               # 
#               ------------------------------------------------#--------#---------------                                                #
#              |                                                #        #              |                                                #  
#              ▼                                                #        #              |                                                #
#    #####################        ##########################    #        #    ############⚫️#########      ##########################    #
#    #                   #        #                        #    #        #    #           |       #        #                        #    # 
#    #                   #        #                        #    #        #    #           |       #        #                        #    #
#    #                   #        #  ####################  #    #        #    #           |       #        #  ####################  #    #
#    #      Workout      #        #  #  get_calories()  #  #    #        #    #    RunWorkout     #        #  #                  #  #    #
#    #                   #        #  ####################  #    #        #    #           |       #        #  #      start       #  #    # 
#    #       Class       #        #  ####################  #    #        #    #    instance       #        #  #                  #  #    # 
#    #                   #        #  #    get_start()   #  #    #        #    #           |       #        #  ####################  #    #                                                           
#    #                   #        #  ####################  #    #        #    #           |       #        #  ####################  #    #
#    #                   #        #  ####################  #    #     ---#----#-----------        #        #  #                  #  #    # 
#    #     ⚫️----        #        #  #     get_end()    #  #    #     |   #    #         ⚫️---      #        #  #       end        #  #    #
#    #           |       #        #  ####################  #    #    |   #    #             |     #        #  #                  #  #    #                                                     
#    #           |       #        #                        #    #    |   #    #             |     #        #  ####################  #    #
#    #           |       #        #  ####################  #    #    |   #    #             |     #        #  ####################  #    #
#    #           --------#----    #  #  set_calories()  #  #    #    |   #    #             |     #        #  #                  #  #    # 
#    #                   #   |    #  ####################  #    #    |   #    #             ------#----    #  #     calories     #  #    # 
#    #                   #   |    #  ####################  #    #    |   #    #                   #   |    #  #                  #  #    #
#    #                   #   -----#-▶︎#    set_start()   #  #    #    |   #    #                   #   |    #  ####################  #    #
#    #                   #        #  ####################  #    #    |   #    #                   #   |    #  ####################  #    #
#    #                   #        #  ####################  #    #    |   #    #                   #   |    #  #                  #  #    #
#    #####################        #  #     set_end()    #  #    #    |   #    #####################   -----#-▶︎#      icon        #  #    #               
#                                 #  ####################  #    #    |   #                                 #  #                  #  #    #
#                                 #                        #    #    |   #                                 #  ####################  #    #
#                                 #                        #    #    |   #                                 #  ####################  #    #    
#                                 #  ###################   #    #    |   #                                 #  #                  #  #    #
#                                 #  #    __init__()   #   #    #    |   #                                 #  #      kind        #  #    #     
#                                 #  ###################   #    #    |   #                                 #  #                  #  #    # 
#                                 #                        #    #    |   #                                 #  ####################  #    # 
#                                 #                        #    #    |   #                                 #  ####################  #    #                                                
#                                 #  ###################   #    #    |   #                                 #  #                  #  #    #                                                                                               
#                                 #  #   cal_per_hour  #   #    #    |   #                                 #  #       elev       #  #    #     
#                                 #  ###################   #    #    |   #                                 #  #                  #  #    #
#                                 #                        #    #    |   #                                 #  ####################  #    #
#                                 #                        #    #    |   #                                 #                        #    #
#                                 ##########################    #    |   #                                 #                        #    #
#                                                               #    |   #                                 #                        #    # 
#                                                               #    |   #                                 ##########################    #
#                                                               #    |   #                                               #
#                                     Class State               #    |   #                                                               #
#                                                               #    |   #                                                               #
#                                     Dictionary                #    |   #                                       Accessed via            #
#                                                               #    |   #                                                               #
#                                                               #    |   #                                       "self" keyword          #
#                                                               #    |   #                                                               #
#                                                               #    |   #                                                               #
#                                                               #    |   #                                                               #                                                            #
#                                                               #    |   #                                                               #
#################################################################    |   #################################################################
#                                                                    |
#                               --------------------------------------
#                              |
###############################|#################################
#                              |                                # 
#                              |                                #
#    ########################  | ##########################     # 
#    #                      #  | #                        #     #
#    #                      #  | #                        #     #
#    #      RunWorkout      #  | #  ####################  #     #
#    #                      #  | #  #    get_elev()    #  #     #
#    #        Class ◀︎-------#--  #  ####################  #     #
#    #          ⚫️           #    #                        #     #
#    #          |           #    #                        #     # 
#    #          |           #    #  ####################  #     #
#    #           -----------#----#-▶︎#    set_elev()    #  #     #
#    #                      #    #  ####################  #     #
#    #                      #    #                        #     #
#    #                      #    #                        #     # 
#    #                      #    #                        #     #
#    #                      #    #                        #     #
#    #                      #    #                        #     #
#    ########################    ##########################     #
#                                                               #
#                                                               #
#                                                               # 
#                                                               # 
#################################################################




# WHY USE INHERITENCE?

# Improve clarity

    # Commonalities are explicit in parent class
    
    # Differences are explicit in subclass


# Reuse code

# Enhance modularity

    # Can pass subclasses to any method that uses parent
    

# SUBCLASSES REUSE PARENT CODE

# Complex print function shared by all subclasses


#                                                       ----------------------------          
#                                                      |       ▲                   |
#                                                      |       |                   | 
#                                         -------------|-------                    |
#                                        |             |                           |
#                                        |   ----------|--▶︎ 😓                     |
#                                        |  |   -------|--▶︎ Workout                |
#                                        |  |  |       |                           |
#                                        |  |  |   --▶︎ |                           |
#                                        |  |  |  |    |                           |
#                                        |  |  |  |    |                           |
#                                        |  |  |  |  --|--▶︎ 0:22:00                |
#                                        |  |  |  | |  |    73 Calories            |
#                                        |  |  |  | |  |    ▲                       |
#                                        |  |  |  | |  |    |                      |
#                                        |  |  |  | |  |    -----                  |
#                                        |  |  |  | |  |        |                  | 
#                                        |  |  |  | |   --------|-------------------
#                                        |  |  |  |  --------   |        ▲ 
#                                        |  |  |  |         |   |        |
# class Workout(object):                 |  |  |  ------    |   |        |
#                                        |  |  |       |    |   |        | 
    # ………                                |  |  ------  |    |   |        ------------------
#                                        |  |       |  |    |   |                         |
    # def __str__(self):                 |  -----   |  |    |   |                         |
#                                        |       |  |  |    |   ------------------        |
        # width = 16                     |output |  |  |    |                     |       |
#                                        |       |  |  |    |                     |       |
        #  -----------------------------------   |  |  |    -----------------     |       |
        # | retstr = f"|{'-' * width} | \n"  |   |  |  |                    |     |       |
        # | retstr += f"|{' ' * width} | \n" |   |--|---                    |     |       |
        # ------------------------------------   |  |                       |     |       |
#                                                |  |                       |     |       |
#                                              --   |                       |     |       |
        # iconLen = 0                         |     -------                 |     |       |
#                                             |           |                 |     |       |
        #  ---------------------------------------------- |                 |     |       |
        # | retstr += f"| {self.icon}{' '*(width-3)}|\n"| |                 |     |       |
        # ----------------------------------------------------------------  |     |       | 
        # | retstr += f"| {self.kind}{' '*(width-len(self.kind)-1)}|\n"  |  |     |       | 
        # ---------------------------------------------------------------   |     |       |
#                                                                           |     |       |
        # retstr += f"|{' ' *width}|\n"                      ----------------     |       |
        # duration_str = str(self.get_duration())           |                     |       | 
#                                                           |                     |       |
        #  --------------------------------------------------------------------   |       |  
        # | retstr += f"| {duration_str}{' '*(width-len(duration_str)-1)}|\n" |   |       |
        # --------------------------------------------------------------------    |       |
        # cal_str = f"{self.get_calories():.0f}"                                  |       | 
#                                                          -----------------------        |
#                                                         |                               |
        #  ---------------------------------------------------------------------          |
        # | retstr += f"| {cal_str} Calories {' '*(width-len(cal_str)-11)}|\n" |          |
        # ---------------------------------------------------------------------           |
#                                                                                         |
#          ---------------------------------                                              |
        # | retstr += f"|{' ' *width}|\n"  | ----------------------------------------------
        # | retstr += f"|{'_'*width}|\n"   |
#          ---------------------------------      
        
        
        
        # return retstr
    
    
    
# SUBCLASSES REUSE PARENT CODE            

# w=Workout(…)

# rw=RunWorkout(…)

# sw=SwimWorkout(…)


# All Workout subclasses can use Workout __str__() method!




# print(w)

# print(rw)

# print(sw)    



#                                        Workout specific icon
#                                        and label
#                                         ▲        ▲    ▲
#                                         |        |    |
#                                         |        |    |  
#                                         |        |    |
#             -----------------------------        |    |
#            |                                 ----     ------------------------
#            |                                |                                |
#            |                                |                                |
#       -----|--------------------      ------|-------------------       ------|-------------------
#      |     |                   |      |     |                   |      |     |                   |
#      |     |                   |      |     |                   |      |     |                   |
#      |    😓                   |      |    🏃‍                  |      |     🏊‍                  |
#      |    Workout              |      |    Running              |      |    Swimming             | 
#      |                         |      |                         |      |                         | 
#      |                         |      |                         |      |                         |      
#      |                         |      |                         |      |                         | 
#      |    0:22:00              |      |    2:22:00              |      |    0:22:00              |
#      |    73 Calories          |      |    1420 Calories        |      |    147 Calories         |
#      |            |            |      |         |               |      |     |                   | 
#      |            |            |      |         |               |      |     |                   |
#      -------------|------------       ----------|---------------       ------|------------------- 
#                   |                             |                            |
#                   |                             |                            |
#                   |                             ------        ---------------
#                   ------------------------------     |        |
#                                                |     |        |
#                                                |     |        |
#                                                ▼     ▼        ▼
#                                            Calories calculated based on
#                                            cal_per_hr for each subclass 


# WHERE CAN I USE AN INSTANCE OF A CLASS?

# We can use an instance of RunWorkoutanywhere Workoutcan be used

# Opposite is not true (cannot use Workoutanywhere RunWorkoutis used)

# Consider two helper functions

def total_calories(workouts):
    
    cals = 0
    
    for w in workouts:
        
        cals += w.get_cals()

    return cals


def total_elevation(run_workouts):
    
    elev = 0

    for w in run_workouts:
        
        elev += w.get_elev()


    return elev


# WHERE CAN I USE AN INSTANCE OF A CLASS?


#                                      |
#                                      | 
#     def total_calories(workouts):    |    def total_elevation(run_workouts):    
#                                      |    
#        cals = 0                      |        elev = 0
#                                      |    
#    for w in workouts:                |        for w in run_workouts:
#                                      |        
#        cals += w.get_calls()         |            elev += w.get_elev()  
#                                      |        
#       return cals                    |        return elev 
#                                      |
#                                      |    




# def total_calories(workouts):
    
    # cals = 0
    
    # for w in workouts:
        
        # cals += w.cals()
        
    # return cals 

    
# def total_elevation(run_workouts):
    
    # elev = 0
    
    # for w in run_workouts:
        
        # elev += w.get_elev()
        
    # return elev


# w1 = Workout("9/30/2021 1:35 PM", "9/30/2021 2:05 PM") # 30 minutes workouts = 100 cals

# w2 = Workout("9/30/2021 4:35 PM", "9/30/2021 5:05 PM") # 2 hr run workouts


# rw1 = RunWorkout("9/30/2021 1:35 PM", "9/30/2021 3:35 PM", 100)
                                                         # ---

# rw2 = RunWorkout("9/30/2021 1:35 PM", "9/30/2021 3:35 PM", 200)
                                                         # ---  
                                                         # elevation val 
                                                         
# total_calories([w1, w2, rw1, rw2])  # (1) # cal = 100+100+400+400

# total_elevation([rw1, rw2])  # (2) # elev = 100+200

# total_elevation([w1, rw1])  # (3) # err! w1 has no elev method


# YOU TRY IT!

# For each line creating on object below, tell me:
    
    # What is the calories val through get_calories()
    
    # What is the elevation val through get_elev()
    
    
# w1 = Workout('9/30/2021 2:20 PM','9/30/2021 2:50 PM')
# w2 = Workout('9/30/2021 2:20 PM','9/30/2021 2:50 PM',450)
# rw1 = RunWorkout('9/30/2021 2:20 PM','9/30/2021 2:50 PM',250)
# rw2 = RunWorkout('9/30/2021 2:20 PM','9/30/2021 2:50 PM',250,300)
# rw3 = RunWorkout('9/30/2021 2:20 PM','9/30/2021 2:50 PM',calories=300)    
 

# OVERRIDING SUPERCLASSES

# Overriding superclass – add calorie calculation w/ distance

# class RunWorkout(Workout):
   
#   --------------------
#  | cals_per_km = 100 |
#   -------------------
#   Add another class var
  
#    ------------------------
#   | def get_calories(self)|: 
#   ------------------------

#        -------------------------
#    if | (self.route_gps_points | != None):
#       -------------------------
#        get_calories() overriden since it is defined in both   
#        sub and superclass     
   

#         ----------------------------------    
#        |lastP = self.routeGpsPoints[0]    | 
#        |for p in self.routeGpsPoints[1:]: |
#        -----------------------------------
#        Iterate through all pairs of GPS points

#             -------------------------------
#            | dist += gpsDistance(lastP,p) |
#            | lastP = p                    |
#            --------------------------------
#            Summing up their distance

#         return dist * RunWorkout.cals_per_km

#    -----------------------------------
#   | else:                            | 
#   |    return super().get_calories() |   
#   -----------------------------------
#   Didn't pass in gps coords, so just do whatever superclass does  



#################################################################        #################################################################
#                                                               #        #                                                               #
#                                                               #        #                                                               # 
#               ------------------------------------------------#--------#---------------                                                #
#              |                                                #        #              |                                                #  
#              ▼                                                #        #              |                                                #
#    #####################        ##########################    #        #    ############⚫️#########      ##########################    #
#    #                   #        #                        #    #        #    #           |       #        #                        #    # 
#    #                   #        #                        #    #        #    #           |       #        #                        #    #
#    #                   #        #  ####################  #    #        #    #           |       #        #  ####################  #    #
#    #      Workout      #        #  #  get_calories()  #  #    #        #    #    RunWorkout     #        #  #                  #  #    #
#    #                   #        #  ####################  #    #        #    #           |       #        #  #      start       #  #    # 
#    #       Class       #        #  ####################  #    #        #    #    instance       #        #  #                  #  #    # 
#    #                   #        #  #    get_start()   #  #    #        #    #           |       #        #  ####################  #    #                                                           
#    #                   #        #  ####################  #    #        #    #           |       #        #  ####################  #    #
#    #                   #        #  ####################  #    #     ---#----#-----------        #        #  #                  #  #    # 
#    #     ⚫️----        #        #  #     get_end()    #  #    #     |   #    #         ⚫️---      #        #  #       end        #  #    #
#    #           |       #        #  ####################  #    #    |   #    #             |     #        #  #                  #  #    #                                                     
#    #           |       #        #                        #    #    |   #    #             |     #        #  ####################  #    #
#    #           |       #        #  ####################  #    #    |   #    #             |     #        #  ####################  #    #
#    #           --------#----    #  #  set_calories()  #  #    #    |   #    #             |     #        #  #                  #  #    # 
#    #                   #   |    #  ####################  #    #    |   #    #             ------#----    #  #     calories     #  #    # 
#    #                   #   |    #  ####################  #    #    |   #    #                   #   |    #  #                  #  #    #
#    #                   #   -----#-▶︎#    set_start()   #  #    #    |   #    #                   #   |    #  ####################  #    #
#    #                   #        #  ####################  #    #    |   #    #                   #   |    #  ####################  #    #
#    #                   #        #  ####################  #    #    |   #    #                   #   |    #  #                  #  #    #
#    #####################        #  #     set_end()    #  #    #    |   #    #####################   -----#-▶︎#      icon        #  #    #               
#                                 #  ####################  #    #    |   #                                 #  #                  #  #    #
#                                 #                        #    #    |   #                                 #  ####################  #    #
#                                 #                        #    #    |   #                                 #  ####################  #    #    
#                                 #  ###################   #    #    |   #                                 #  #                  #  #    #
#                                 #  #    __init__()   #   #    #    |   #                                 #  #      kind        #  #    #     
#                                 #  ###################   #    #    |   #                                 #  #                  #  #    # 
#                                 #                        #    #    |   #                                 #  ####################  #    # 
#                                 #                        #    #    |   #                                 #  ####################  #    #                                                
#                                 #  ###################   #    #    |   #                                 #  #                  #  #    #                                                                                               
#    super()                      #  #   cal_per_hour  #   #    #    |   #                                 #  #       elev       #  #    #     
#                                 #  ###################   #    #    |   #                                 #  #                  #  #    #
#                                 #                        #    #    |   #                                 #  ####################  #    #
#                                 #                        #    #    |   #                                 #                        #    #
#                                 ##########################    #    |   #                                 #                        #    #
#                                                               #    |   #                                 #                        #    # 
#                                                               #    |   #                                 ##########################    #
#                                                               #    |   #                                               #
#                                     Class State               #    |   #                                                               #
#                                                               #    |   #                                                               #
#                                     Dictionary                #    |   #                                       Accessed via            #
#                                                               #    |   #                                                               #
#                                                               #    |   #                                       "self" keyword          #
#                                                               #    |   #                                                               #
#                                                               #    |   #                                                               #
#                                                               #    |   #                                                               #                                                            #
#                                                               #    |   #                                                               #
#################################################################    |   #################################################################
#                                                                    |
#                               --------------------------------------
#                              |
###############################|#################################
#                              |                                # 
#                              |                                #
#    ########################  | ##########################     # 
#    #                      #  | #                        #     #
#    #                      #  | #                        #     #
#    #      RunWorkout      #  | #  ####################  #     #
#    #                      #  | #  #    get_elev()    #  #     #
#    #    ⚫️  Class ◀︎-------#--  #  ####################  #     #
#    #    |                 #    #  ####################  #     #
#    #    |                 #    #  #    set_elev()   #   #     # 
#    #    |                 #    #  ####################  #     #
#    #    |                 #    #  ####################  #     #
#    #    ------------------#----#-▶︎#  get_calories()  #  #     #
#    #                      #    #  ####################  #     #
#    #                      #    #  ####################  #     # 
#    #                      #    #  #  cals_per_km     #  #     #
#    #                      #    #  ####################  #     #
#    #                      #    #                        #     #
#    ########################    ##########################     #
#                                                               #
#                                                               #
#                                                               # 
#                                                               # 
#################################################################
    


# WHICH METHOD WILL BE CALLED?


# Overriding: subclass methods with same name as superclass

# For an instance of a class, look for a method name in current 
# class definition

# If not found, look for method name up the hierarchy (in parent, then
# grand parent, and so on)

# Use first method up the hierarchy that you found with that method name
    
   
    
#                                      get_calories()
        
                                    #####################
                                    #                   #
                                    #                   #
                                    #      Workout      #
                                    #                   #
                                    #                   #
                                    #####################
#                                           ▲    ▲ 
#                                           |    |
#                                           |    |
#                               ------------      ------------
#                              |                             |
#                              |                             |
                    #####################          #####################
                    #                   #          #                   #
                    #      Outdoor      #          #      Indoor       #
#  get_calories()?  #      Workout      #          #      Workout      # 
                    #                   #          #                   #
                    #                   #          #                   #
                    #####################          #####################
#                           ▲   ▲                           ▲    ▲
#                           |   |                           |    |
#                           |   |                           |    |
#                        ---     ---------------            |    |
#                       |                      |            |    |  
#                       |                      |            |    |
              #####################  #####################  |    |
              #                   #  #                   #  |    | 
              #                   #  #                   #  |    |
              #      Running      #  #      Swimming     #  |    |
              #                   #  #                   #  |    |
              #                   #  #                   #  |    |
              #####################  #####################  |    |
#                                                           |    |
#                                                           |    |
#                                                     ------     ------------    
#                                                    |                      |
#                                                    |                      | 
                                           #####################  ##################### 
                                           #                   #  #                   #
#            get_calories()?               #                   #  #                   #
                                           #     Treadmill     #  #       Weights     #
                                           #                   #  #                   #
                                           #                   #  #                   #
                                           #####################  #####################

    
    
# TESTING EQUALITY WITH SUBCLASSES    
    
# With subclasses, often want to ensure base class is equal, in addition to
# new properties in the subclass    
    
    
    
# class Workout(object):
    
# ……                           Types must be the same    
#                                     ▲ 
#                                     | 
    # def __eq__(self, other):        |
        # return type(self) == type(other) and \
        # self.startDate == other.startDate and \          And all the other properties
        # self.endDate == other.endDate and \              equal too
        # self.kind == other.kind and \
        # self.get_calories() == other.get_calories()    
    
    
    

# class RunWorkout(Workout):
    
# ……


    # Workout properties are equal
    
    # And new properties from RunWorkout are equal


    # def __eq__(self,other):
        # return super().__eq__(other) and self.elev == other.elev




# OBJECT ORIENTED DESIGN:
# MORE ART THAN SCIENCE
    
# OOP is a powerful tool for modularizing your code and grouping state and
# functions together


#                                   BUT


# It’s possible to overdo it

    # New OOP programmers often create elaborate class hierarchies
    
    # Not necessarily a good idea
    
    # Think about the users of your code

        # Will your decomposition make sense to them?




   # Because the function that is invoked is implicit in the class hierarchy,
   # it can sometimes be difficult to reason about control flow


# The Internet is full of opinions OOP and “good software design” – you have
# to develop your own taste through experience!


