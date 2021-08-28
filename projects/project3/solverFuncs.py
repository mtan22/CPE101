#Michelle Tan
#11/2/2020
#Project 3

def get_cages():
    #Asks user for number of cages and sets up the formatting for each cage as it increments by 1 for each input
    #Appends the cage numbers in a list and returns this list
    numOfCages = int(input("Number of cages: "))
    userInput = []
    for index in range(numOfCages):
        cageNum = input("Cage number {0:d}: ".format(index)).split()
        cageNum = [int(index) for index in cageNum]
        userInput.append(cageNum)
    return userInput

def check_rows_valid(puzzle):
    #Nested loop to return True if the rows are valid
    #.count() is to count how many duplicates there are in a row, if they're are more than 1, then the row is NOT valid
    for index in range(len(puzzle)):
        for index2 in range(len(puzzle)):
            count1 = puzzle[index].count(index2+1)
            if count1 > 1:
                return False
    return True

def check_columns_valid(puzzle):
    #columnPuzzle is to append the column list so it acts as a "row"
    #columnPuzzle is then added as a parameter when check_rows_valid is run, and it returns True or False if the column is valid or not
    columnPuzzle=[]
    for index in range(len(puzzle)):
        col = []
        for index2 in range(len(puzzle)):
            col.append(puzzle[index2][index])
        columnPuzzle.append(col)
    return check_rows_valid(columnPuzzle)

def check_cages_valid(puzzle, cages):
    #Nested for loop to take the sum from each individual cage and stores it in the variable sum1
    #If the value of the cage (v) is less than 0, then it returns True or else there would be an off list index in solver.py
    #Returns True if the cages are valid
    for index in range(len(cages)):
        sum1 = 0
        for index2 in range(cages[index][1]):
            c = cages[index][index2+2] 
            lengthPuzzle=(len(puzzle))
            v = puzzle[(c//(lengthPuzzle))][(c%(lengthPuzzle))]
            sum1+=v
            if v <= 0:
                return True
        if not cages[index][0] == sum1:
            return False
    return True

def check_valid(puzzle, cages):
    #If all functions of validity pass, then the solution is made and is displayed on the screen
    if check_rows_valid(puzzle) and check_columns_valid(puzzle) and check_cages_valid(puzzle,cages):
        return True
    return False

