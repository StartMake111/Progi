import math

a = int(input())
b = int(input())
c = int(input())

if a == 0 :
    print ( 'x ='), (-c/b)

else :
    D = b*b - 4*a*c

    if D < 0 :
        print('TI chavo nadelal')
    else:

      if D == 0 :
          print ( 'x =' ), (-b/2*a)
      else:
          x1 = -b - math.sqrt(D) / 2*a

          x2 = -b - math.sqrt(D) / 2*a

          if x1 == x2:
              print('x ='), (x1)
          else :
              print ('x1 ='), (x1)
              print ('x2 ='), (x2)