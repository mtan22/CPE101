#Michelle Tan
#Instructor: Turner
#Section: 01
#Lab 3

def max_101(x,y):
    #Returns the largest of the two values of x and y; if x and y are the same number, it will return that number
    if x > y:
       return x
    elif y > x:
       return y
    else:
       return x or y

def max_of_three(x,y,z):
    #Returns the largest of the three values of x, y, and z; if x, y, and z are the same number, it will return that number 
    if max_101(x,y) > z:
       return max_101(x,y)
    elif z == y == z:
       return x or y or z
    else:
       return(z)

def rental_late_fee(x):
    #Returns the number of dollars for the assessed late fee based on the input of late days
    if x <= 0:
       return 0
    elif x > 0 and  x <= 9:
       return 5
    elif x > 9 and x <= 15:
       return 7
    elif x > 15 and  x <= 24:
       return 19
    else:
       return 100
