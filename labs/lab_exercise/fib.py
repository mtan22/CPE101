def Fibonacci_Sum(list1,n):
   for i in range(2,n):
       list1.append(list1[i-1]+list1[i-2])
   return list1

print(Fibonacci_Sum([0,1],6))
