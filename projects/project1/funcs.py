#Project 1
#
#Name: Michelle Tan
#Instructor: Turner
#Section:  01

#Import math module for the math.sqrt() used in the getVelocityObject function
import math

def poundsToKG(pounds): 
   #Computes the input of the skater's weight in pounds to kilograms
   massSkater = pounds*0.453592
   return massSkater

def getMassObject(object):
   #Given the specific input, it will return the corresponding mass of the object
   if object=='t':
      return 0.1
   elif object=='p':
      return 1.0
   elif object=='r':
      return 3.0
   elif object=='g':
      return 5.3
   elif object=='l':
      return 9.07
   else:
      return 0.0

def getVelocityObject(distance):
   #Computes the velocity of the object based on the distance input
   velocityObject = math.sqrt((9.8*distance)/2)
   return velocityObject

def getVelocitySkater(massSkater, massObject, velocityObject):
   #Computes the velocity of the skater using the mass of the skater, mass of the object, and velocity of the object
   #Rounds the final velocity to three decimal places
   velocitySkater = ((massObject*velocityObject)/massSkater)
   velocitySkater = float('{:.3f}'.format(velocitySkater))
   return velocitySkater
