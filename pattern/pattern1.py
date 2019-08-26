'''Program to print pattern below
  ***
  ***
  ***
  ***
  ***
  ***
 if (N=6) is given by user'''
N= int(input("input:"))
for i in range(0,N):
    for j in range(0,N):
        print("*", end="")
    print()

