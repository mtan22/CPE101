#Michelle Tan
#11/2/2020
#Project 3

import unittest
from solverFuncs import*

def main():
    #Uses a for loop to create the general format of the puzzle first
    puzzle = []
    cages=get_cages()
    for index in range(5):
        puzzle.append(5*[0])
    index = 0
    checks = 0
    backtracks = 0
    #Uses a while loop to iterate through the check functions in solverFuncs and counts the backtracks and checks in the loop
    while index < 25:
        puzzle[index//5][index%5] += 1
        checks=checks+1
        if check_valid(puzzle,cages) and puzzle[index//5][index%5] <= 5:
            index=index+1
        elif puzzle[index//5][index%5] <= 4:
            pass
        else:
            puzzle[index//5][index%5] = 0
            index=index-1
            backtracks=backtracks+1   
    print()
    print ('---Solution---')
    print()
    #After the checks, the solution is made and the for loop displays the finished solution
    for index in range(len(puzzle)):
        print (' '.join(map(str, puzzle[index])))
    print( '\nchecks: ' + str(checks) +' backtracks: ' + str(backtracks))
 
if __name__ == "__main__":
    main()
