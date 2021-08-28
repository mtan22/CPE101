#Michelle Tan
#11/19/2020
#Prof. Turner
#Lab Exercise: Sort Dictionary

def sortDict():
   #Created a list of integer values from the first character of the students/keys of the dictionary in"ordList"
   #Sorted them from minimum to maximum and changed them back to their character values in "charList"
   #Iterated through charList and the original dictionary and put the sorted keys and their values in the new dictionary "newD"
   #Returned the sorted dictionary
   d = {'Bob': 3, 'Adam': 62, 'Sebastien': 9, 'Kathy': 99, 'Nathan': 42, 'Caitlin': 43}
   ordList=[]
   charList=[]
   newD={}
   print("Original Dictionary:\n",d)
   for i in d:
      ordList.append(ord(i[0]))

   for i in range(len(ordList)):
      charList.append(min(ordList))
      ordList.remove(min(ordList))

   for i in range(len(charList)):
      charList[i] = chr(charList[i])

   for i in range(len(charList)):
      for j in d:
          if charList[i] == j[0]:
              newD[j] = d[j]
   
   print("Sorted Dictionary:")
   return(newD)

def givenStudent():
   #Given the user input of a student, I iterated through the dictionary and found the corresponding value of that student
   #Returned the value
   d = {'Bob': 3, 'Adam': 62, 'Sebastien': 9, 'Kathy': 99, 'Nathan': 42, 'Caitlin': 43}
   student=input("Give a name of a student and their integer value will be returned:  ")
   for i in d:
      if student == i:
          return(d[i])
         
print(sortDict())
print(givenStudent())
