#Project 1
#
#Name: Michelle Tan
#Instructor: Turner
#Section: 01

import unittest
import funcs

def main():
    #Takes the input of the skater's weight, the professor's distance, and the object
    pounds =int(input('How much do you weigh (pounds)? '))
    distance = int(input('How far away is your professor (meters)? '))
    object = input('Will you throw a rotten (t)omato, banana cream (p)ie, (r)ock, (l)ight saber, or lawn (g)nome? ')
    #Calls functions from funcs.py to compute the final velocity
    massSkater = funcs.poundsToKG(pounds)
    massObject = funcs.getMassObject(object)
    velObject = funcs.getVelocityObject(distance)
    velSkater = funcs.getVelocitySkater(massSkater,massObject,velObject)
    print("\nNice throw!", end = " ")
    #Runs conditionals to display certain statements based on the object's mass and the skater's velocity
    if massObject <= 0.1:
       print("You're going to get an F!")
    elif massObject >  0.1 and massObject <= 1.0:
       print("Make sure your professor is OK.")
    elif massObject > 1.0:
       if distance < 20.0:
          print("How far away is the hospital?")
       else:
          print("RIP professor.")
    print("Velocity of skater:",velSkater,"m/s")
    if velSkater < 0.2:
       print("My grandmother skates faster than you!")
    elif velSkater >= 0.2 and velSkater < 1.0:
       pass
    elif velSkater >= 1.0:
       print("Look out for that railing!!!")


if __name__ == '__main__':
   main()
