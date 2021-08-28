import driver

def letter(row,col):
    if row == 9:
       if col>=0 and col<9:
          return 'G'
       elif col == 9:
          return 'Z'
       elif col>9:
          return 'G'
    else:
       return 'G'

if __name__ == '__main__':
   driver.comparePatterns(letter)
