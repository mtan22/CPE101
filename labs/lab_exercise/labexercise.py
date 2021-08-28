def sortDict():
   d = {'Bob': 3, 'Adam': 62, 'Sebastien': 9, 'Allison': 99, 'Nathan': 42, 'Caitlin': 43}
   d1 = {}
   for key in sorted(d.keys()) :
      d1[key]={d[key]}
   print(d1)

def givenStudent():
   d = {'Bob': 3, 'Adam': 62, 'Sebastien': 9, 'Allison': 99, 'Nathan': 42, 'Caitlin': 43}
   student=input("Name of student? ")
   for i in d:
      if student == i:
          print(d[i])

sortDict()
givenStudent()
