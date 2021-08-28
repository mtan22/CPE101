#Michelle Tan
#10/23/2020
#Lab 5

def are_positive(testList):
   #Used list comprehension to iterate through testList and returns a list with all the positive values from testList
   newList=[i for i in testList if i > 0]
   return newList

def are_greater_than(testList,n):
   #Used a for loop to iterate through testList and returns a list of values that are greater than parameter n
   newList=[]
   for i in testList:
       if i > n:
          newList.append(i)
   return newList

def are_in_first_quadrant(testList):
   #Used a while loop to iterate through testList and returns a list of point(s) that are in the first quadrant of the Cartesian plane
   newList=[]
   i=0
   while i in range(len(testList)):
       if testList[i][0] >= 0 and testList[i][1] >= 0:
          newList.append(testList[i])
       i=i+1
   return newList
