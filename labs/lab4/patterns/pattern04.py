import driver

def letter(row,col):
    if row <=1 and col<=10:
       return 'S'
    elif row >1 and row < 5:
       if row >= 2 and col <= 2:
          return 'S'
       elif col>=3 and col <=6:
          return 'M'
       elif col >= 7 and col<=9:
          return 'S'
    else:
       return 'S'


if __name__ == '__main__':
    driver.comparePatterns(letter)
