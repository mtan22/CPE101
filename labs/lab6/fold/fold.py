#Michelle Tan
#10/27/2020
#Lab 6

def sum(testList):
   #Returns the sum of all values in the test list
   totalSum=0
   for i in testList:
      totalSum=totalSum+i
   return totalSum

def index_of_smallest(testList):
   #Returns the index of the smallest value in the test list
   #Returns the index of the first occurrence if there are multiple minimum values
   #Returns -1 if the list is empty
   if len(testList) <= 0:
      return -1
   else:
      for i in range(len(testList)):
         if testList[i] < testList[i-1]:
             minValue=testList[i]
             minIndex=i
      for i in range(len(testList)):
          if testList[i]==minValue:
             return i
             break
          else:
             return minIndex
