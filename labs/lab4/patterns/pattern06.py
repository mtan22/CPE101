import driver

def letter(row,col):
    if row == 0 or row == 6:
        if col>=0 and col<1:
          return 'X'
        elif col>=1 and col<=5:
          return 'O'
        elif col>5 and col<=6:
          return 'X'
    elif row == 1 or row == 5:
        if col==0:
          return 'O'
        elif col==1:
          return 'X'
        elif col>1 and col<=4:
          return 'O'
        elif col==5:
          return 'X'
        elif col>5 and col<=6:
          return 'O'
    elif row == 2 or row == 4:
        if col>=0 and col<2:
          return 'O'
        elif col>=2 and col<3:
          return 'X'
        elif col==3:
          return 'O'
        elif col==4:
          return 'X'
        elif col>4 and col<=6:
          return 'O'
    elif row == 3:
        if col>=0 and col<3:
          return 'O'
        elif col==3:
          return 'X'
        elif col>3 and col<=6:
          return 'O'
    else:
        return 'O'

if __name__ == '__main__':
    driver.comparePatterns(letter)
