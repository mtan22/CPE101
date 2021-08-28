# Project 2 - Moonlander
# Author: Michelle Tan
# Version: N/A

def showWelcome():
   #Displays the welcome message as you hop on aboard the Lunar Module Flight Simulator!
   print("\nWelcome aboard the Lunar Module Flight Simulator\n\n   To begin you must specify the LM's initial altitude")
   print("   and fuel level. To simulate the actual LM user\n   values of 1300 meters and 500 liters, respectively.")
   print("\n   Good luck and may the force be with you!\n")


def getFuel():
   #Takes in user input of fuel and makes sure the value is a positive integer
   while True:
      fuel = int(input("Enter the initial amount of fuel on board the LM (in liters): "))
      if fuel <  1:
          print("ERROR: Amount of fuel must be positive, please try again")
      else:
         return fuel
         break

def getAltitude():
   #Takes in user input of altitude and makes sure the value is between 1 and 9999
   while True:
      altitude = int(input("Enter the initial altitude of the LM (in meters): "))
      if altitude < 1 or altitude > 9999:
          print("ERROR: Altitude must be between 1 and 9999, inclusive, please try again")
      else:
         return altitude
         break

def displayLMState(elapseTime, altitude, velocity, fuel, fuelRate):
   #Formats and converts arguments into strings
   #Displays the Lunar Module State with the elapsed time, altitude, velocity, etc...
   elapseTime = f'{elapseTime:9.4f}'
   print("Elapsed Time:",elapseTime.rstrip('0').rstrip('.'),'s')
   fuel=f'{fuel:9.4f}'
   print("        Fuel:",fuel.rstrip('0').rstrip('.'),'l')
   fuelRate=f'{fuelRate:9.4f}'
   print("        Rate:",fuelRate.rstrip('0').rstrip('.'),'l/s')
   altitude=f'{altitude:9.4f}'
   print("    Altitude:",altitude[:-2],'m')
   velocity=f'{velocity:9.4f}'
   print("    Velocity:",velocity[:-2],'m/s')
         
def getFuelRate(fuel):
   #Takes user input of fuel rate
   #Makes sure the value is between 0 and 9
   while True:
      fuelRate = int(input("\nEnter fuel rate (0-9, 0=freefall, 5=constant velocity, 9=max thrust): "))
      if fuelRate >= 0 and fuelRate <= 9:
          return fuelRate
      else: 
          print("ERROR: Fuel rate must be between 0 and 9, inclusive")
 
def updateAcceleration(gravity, fuelRate):
   #Calculates updated acceleration
   acceleration = gravity*((fuelRate/5)-1)
   return acceleration
        
def updateAltitude(altitude, velocity, acceleration):
   #Calculates updated altitude
   altitude = altitude + velocity + (acceleration/2)
   altitude=round(altitude,2)
   return altitude

def updateVelocity(velocity, acceleration):
   #Calculates updated velocity
   velocity = velocity + acceleration
   velocity=round(velocity,2)
   return velocity

def updateFuel(fuel, fuelRate):
   #Calculates updated fuel
   fuel = fuel - fuelRate
   return fuel

def displayLMLandingStatus(velocity):
   #Displays Lunar Module Landing Status based on final velocity
   if velocity <= 0 and velocity >= -1:
      print("Status at landing - The eagle has landed!")
   elif velocity < -1 and velocity > -10:
      print("Status at landing - Enjoy your oxygen while it lasts!")
   elif velocity <= -10:
      print("Status at landing - Ouch - that hurt!")
   else:
      print("ERROR")
