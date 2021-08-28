#Michelle Tan
#Instructor: Turner
#Section: 01
#Lab 3

def is_even(x):
    #returns True if even and False if odd
    return x % 2 ==  0

def in_an_interval(x):
    #returns True if the number is in the given intervals
    return (x >= 2 and x < 9) or (x > 47 and x < 92) or (x > 12 and x <= 19) or (x >= 101 and x <= 103)
