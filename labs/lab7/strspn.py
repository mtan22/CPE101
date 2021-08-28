#Michelle Tan
#11/3/20
#Lab 7

def my_strspn(str1,str2):
   #Iterates through str1 and counts how many times a character from the string appears in str2 excluding duplicates
   count=0
   countDuplicates=[]
   for i in range(len(str1)):
      if (str1[i] in str2) and (str1[i] not in countDuplicates):
         count+=1
         if str1[i] != str1[i+1]:
            countDuplicates.append(str1[i])
      elif str1[i] not in str2:
         break
   return count

def main():
   #Asks for user input for str1 and str2
   #Runs my_strspn and displays the returned result
   str1=input("Enter string1: ")
   str2=input("Enter string2: ")
   result=my_strspn(str1,str2)
   print("Result: " + str(result))

main()
