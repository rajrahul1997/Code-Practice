'''Program to print pattern below
             *
           *  *
          *  *  *
         *  *  *  *
        *  *  *  *  *
       *  *  *  *  *  *
      *  *  *  *  *  *  *
 if (N=7) is given by user'''
N= int(input("input:"))
m = (2 * N) - 2
for i in range(0, N):
    for j in range(0, m):
        print(end=" ")
    m = m - 1 # decrementing m after each loop
    for j in range(0, i + 1):
        # printing full Triangle pyramid using stars
        print("* ", end=' ')
    print(" ")