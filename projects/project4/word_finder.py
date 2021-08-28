# Michelle Tan
#Instructor: Prof. Turner
#Nov. 8, 2020
#Project 4: Word Search

import unittest
from funcs import*

def main():
    #Takes in initial file inputs and builds a list of search words and maps the puzzle
    #Calls all the functions and stores the returned lists in the value variables
    #Iterates through the list of search words (searchStrings) and prints out the search words, directions, and positions
    puzzleInput = input()
    searchStrings = input()
    searchStrings = searchStrings.split()
    print("Puzzle:\n")
    for i in range(0,len(puzzleInput),10):
      print(''.join(map(str, puzzleInput[i:i+10])))
    print("\n")
    upValue=checkUp(puzzleInput,searchStrings)
    downValue=checkDown(puzzleInput,searchStrings)
    forwardValue=checkForward(puzzleInput,searchStrings)
    backwardValue=checkBackward(puzzleInput,searchStrings)
    j = 0
    while j < len(searchStrings):
       if searchStrings[j] in upValue:
          p=upValue.index(searchStrings[j])
          print(searchStrings[j] + ": (UP) row: " + str(upValue[p+1]) + " column: " + str(upValue[p+2]))
       elif searchStrings[j] in downValue:
          p=downValue.index(searchStrings[j])
          print(searchStrings[j] + ": (DOWN) row: " + str(downValue[p+1]) + " column: " + str(downValue[p+2]))
       elif searchStrings[j] in forwardValue:
          p=forwardValue.index(searchStrings[j])
          print(searchStrings[j] + ": (FORWARD) row: " + str(forwardValue[p+1]) + " column: " + str(forwardValue[p+2]))
       elif searchStrings[j] in backwardValue:
          p = backwardValue.index(searchStrings[j])
          print(searchStrings[j] + ": (BACKWARD) row: " + str(backwardValue[p+1]) + " column: " + str(backwardValue[p+2]))
       else:
          print(searchStrings[j] + ": word not found")
       j+=1

if __name__ == "__main__":
    main()
