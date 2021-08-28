#Michelle Tan
#10/27/2020
#Lab 6

def is_lower_101(string):
   #Takes a single character as input and returns True if the character is lowercase and False otherwise
   stringInt = ord(string)
   upperString=chr(stringInt-32)
   if string.upper() == upperString:
       return True
   else:
       return False

def char_rot_13(string):
    #Takes a single character and returns the rot-13 encoding of the character
    rot13 = ''
    alpha = {"a":"n" , "b":"o" ,"c":"p" , "d":"q","e":"r" , "f":"s" , "g":"t" ,"h":"u" , "i":"v",  "j":"w", "k":"x" , "l":"y" , "m":"z" ,"n":"a", "o": "b" ,  "p":"c" ,"q":"d" ,"r":"e" ,"s":"f", "t":"g" ,"u":"h", "v":"i", "w":"j", "x":"k", "y":"l", "z":"m" }
    if string.islower():
       rot13 += alpha.get(string)
       return rot13
    if string.isupper():
       string = string.lower()
       rot13 += alpha.get(string).capitalize()
       return rot13
    if string not in alpha:
       rot13 += string
       return rot13
