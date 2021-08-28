#MichelleTan
#10/27/2020
#Lab 6

def str_rot_13(string):
    #Returns the rot-13 encoding of the input string
    rot13 = ''
    alpha = {"a":"n" , "b":"o" ,"c":"p" , "d":"q","e":"r" , "f":"s" , "g":"t" ,"h":"u" , "i":"v",  "j":"w", "k":"x" , "l":"y" , "m":"z" ,"n":"a", "o": "b" ,  "p":"c" ,"q":"d" ,"r":"e" ,"s":"f", "t":"g" ,"u":"h", "v":"i", "w":"j", "x":"k", "y":"l", "z":"m" }
    for i in string:
       if i.islower():
          rot13 += alpha.get(i)
       if i.isupper():
          i = i.lower()
          rot13 += alpha.get(i).capitalize()
       if i not in alpha:
          rot13 += i
    return rot13

def str_translate_101(string,old,new):
     #Returns a string where the occurrence of old is replaced with the new
     newString=''
     for i in string:
        if i == old:
           i = new
        newString+=i
     return newString
