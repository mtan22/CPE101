#Michelle Tan
#Instructor: Prof. Turner
#Nov. 8, 2020
#Project 4: Word Search

def checkUp(puzzle,searchWords):
    #Reverses the puzzle and uses the backwards list to iterate through and get the indices of the words that are in the up direction
    #Stores the up words in a string and then appends them in a list
    #In the list, I find the column index and find the exact index of the searchWord and row; these are returned in the finalList
    puzzle = puzzle[::-1]
    up=[]
    backward=[]
    validWords=[]
    for i in range(0,len(puzzle),10):
        backward.append(puzzle[i:i+10])
    for m in range(len(backward)-1):      
        upWord=''
        for n in range(len(backward)-1):
            upWord+=backward[n][m]
        up.append(upWord)
    for s in range(len(up)):
        for v in range(len(searchWords)):
            col=up[s]
            col=col.find(searchWords[v])
            if col>=0:
                validWords.append([searchWords[v],(9-col),(10-s)])
    finalList=[]
    for lista in validWords:
        for a in lista:
           finalList.append(a)
    return finalList

def checkDown(puzzle,searchWords):
    #Uses the forward list to iterate through the down list
    #Stores the down words in a string and appends them in a list
    #In the list, I find the column index and finds the exact index of the searchWord and row; these are returned in the finalList
    forward=[]
    down=[]
    validWords=[]
    for i in range(0,len(puzzle),10):
        forward.append(puzzle[i:i+10])
    for m in range(len(forward)-1): # -1 because forward_list returns a \r at the end...       
        downWord = ''
        for n in range(len(forward)-1):
            downWord+=forward[n][m]
        down.append(downWord)
    for s in range(len(down)):
        for v in range(len(searchWords)):
            col = down[s]
            col = col.find(searchWords[v])
            if col>= 0:
                validWords.append([searchWords[v],col,s])
    finalList=[]
    for lista in validWords:
        for a in lista:
           finalList.append(a)
    return finalList

def checkForward(puzzle,searchWords):
    #Makes a list of the puzzle lines that go from left to right
    #Iterates through each row (m)  and looks for the searchWord (n)
    #Finds the column index and the index of the searchWord and row; these are returned in the finalList
    validWords=[]
    forward=[]
    for i in range(0,len(puzzle),10):
        forward.append(puzzle[i:i+10])
    for m in range(len(forward)):
        for n in range(len(searchWords)):
            col = forward[m]
            col=col.find(searchWords[n])
            if col>=0:
                validWords.append([searchWords[n],m,col])
    finalList=[]
    for lista in validWords:
        for a in lista:
           finalList.append(a)
    return finalList

def checkBackward(puzzle,searchWords):
    #Reverses the puzzle and creates a list with the reversed lines
    #Iterates through the puzzle and finds the backward words
    #Gets the column index and the index of the searchWord and row; these are returned in the finalList
    puzzle = puzzle[::-1]
    validWords=[]
    backward=[]
    for i in range(0,len(puzzle),10): # rewrite the list with the reversed strings
        backward.append(puzzle[i:i+10])
    for m in range(len(backward)):
        for n in range(len(searchWords)):
            col=backward[m]
            col = col.find(searchWords[n])
            if col>=0:
                validWords.append([searchWords[n],(9-m),(10-col)])
    finalList=[]
    for lista in validWords:
        for a in lista:
           finalList.append(a)
    return finalList

#Diagonal function doesn't do its intended purpose
#I tried fixing the indexes to make the index move a space right on the next line
"""
def checkDiagonal(puzzle,searchWords):
    forward=[]
    down=[]
    validWords=[]
    for i in range(0,len(puzzle),10):
        forward.append(puzzle[i:i+10])
    for m in range(len(forward)-1):     
        downWord=''
        for n in range(len(forward)):
            downWord+=forward[n][m]
        down.append(downWord)
    for s in range(len(down)):
        for v in range(len(searchWords)):
            col=down[s]
            col=col.find(searchWords[v])
            if col>=0:
                validWords.append([searchWords[v],col,s])
    finalList=[]
    for lista in validWords:
        for a in lista:
           finalList.append(a)
    return finalList
"""

if __name__ == "__main__":
    main()
