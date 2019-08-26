'''Program to print pattern below
      *
     **
    ***
   ****
  *****
 if (N=5) is given by user'''
N= int(input("input:"))
for i in range(0,N):
    for j in range(0,N-i-1):
        print(end =" ")
    for j in range(0,i+1):
        print("*",end ="")
    print()

