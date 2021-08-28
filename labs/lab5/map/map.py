#Michelle Tan
#10/23/2020
#Lab 5

import math

def square_all(testList):
   #Used list comprehension to iterate through testList and returns a list with the squared values of testList
   newList=[(i**2) for i in testList]
   return newList

def add_n_all(testList,n):
   #Used a for loop to iterate through testList and returns a list with the sum of n and the corresponding value from testList
   newList=[]
   for i in testList:
      sum1 = n+i
      newList.append(sum1)
   return newList

def distance_all(testList):
   #Used a while loop to iterate through testList and returns a list with the distance value from the origin to the corresponding point on testList
   newList=[]
   index=0
   while index in range(len(testList)):
      distance=math.sqrt((testList[index][0]**2 + testList[index][1]**2))
      distance=round(distance,2)
      newList.append(distance)
      index=index+1
   return newList
