#Project 2 - Moonlander
#Michelle Tan
#Instructor: Turner
#Section: 01

import unittest
from landerFuncs import *

def main():
   #Calls functions that run the Lunar Module Flight Simulator
   showWelcome()
   altitude = getAltitude()
   fuel=getFuel()
   elapseTime=0
   velocity=0.00
   fuelRate=0
   print("\nLM state at retrorocket cutoff")
   while True:
      #If the fuel value is greater than the user input of fuel rate, the user will be asked for the fuel rate continuously until the fuel is less than the fuel rate or equal to 0
      if fuel>=fuelRate:
         displayLMState(elapseTime, altitude, velocity, fuel, fuelRate)
         fuelRate=getFuelRate(fuel)
         acceleration=updateAcceleration(1.62,fuelRate)
         altitude=updateAltitude(altitude,velocity,acceleration)
         velocity=updateVelocity(velocity,acceleration)
         fuel=updateFuel(fuel,fuelRate)
         elapseTime=elapseTime+1
      else:
         while True:
             #I encountered an error here that said my altitude was a string, which I didn't think was possible since I returned the value as a float
             #Unfortunately, I could not fix this error in the time given; I tried type casting a lot and removing the formatting of the altitude on the display, but it did not work
             elapseTime=elapseTime+1
             altitude=updateAltitude(altitude,velocity,acceleration)
             altitude=round(altitude,2)
             altitude=f'{altitude:9.4f}'
             velocity=updateVelocity(velocity,acceleration)
             velocity=round(velocity,2)
             velocity=f'{velocity:9.4f}'
             print("OUT OF FUEL - Elapsed Time:",elapseTime,"Altitude:",altitude[:-2],"Velocity:",velocity[:-2])
             print("\nLM state at impact")
             displayLMState(elapseTime,altitude,velocity,fuel,fuelRate)
             displayLMLandingStatus(velocity)
             break      
   
if __name__ == '__main__':
   main()
