import driver

def letter(row,col):
    if row <=1 and col<=19:
       return 'T'
    elif row >1 and row < 4:
       if row >=1 and col <=3:
          return 'T'
       elif col>=3 and col <=9:
          return 'Z'
       elif col>9 and col<=19:
          return 'T'
    elif row >= 4 and row<6:
       if col<=3:
          return 'T'
       elif col >=3 and col <=6:
          return 'Z'
       elif col>6 and col<=9:
          return 'X'
       elif col>9 and col<=12:
          return 'B'
       elif col>12 and col<=19:
          return 'T'
    elif row >=6 and row<7:
       if col <= 6:
          return 'T'
       elif col>6 and col<=12:
          return 'B'
       elif col>12 and col<=19:
          return 'T'
    else:
       return 'T'


if __name__ == '__main__':
    driver.comparePatterns(letter)
