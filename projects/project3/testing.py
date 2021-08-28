#Name: Michelle Tan
#10/30/2020
#Project 3

def main():
    grid=[]
    for i in range(5):
        grid.append([0][0][0][0][0])
    backtracks = 0
    count = 0
    checkValid = 0
    while count < 25:
       grid[i/5][i%5]+=1
       checkValid=checkValid+1
#

def cage_input():
    userInput=[]
    num_cages=int(input("Number of cages: "))
    for i in range(num_cages):
       cage = input("Cage number {0:d}: ".format(i)).split()
       for i in cage:
          userInput.append(int(i))
    return userInput

def displayGrid():
    for i in range(len(grid)):
        print 
  #

def checkRows(grid):
    
    
