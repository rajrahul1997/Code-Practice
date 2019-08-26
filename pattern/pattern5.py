'''Program to print pattern below
      11111
      0000
      111
      00
      1
if (N=5) is given by user
here one loop of  i is running for row in range(0,N-i) and if else condition is checking for (i%2)'''

N= int(input("input:"))

for i in range (0,N):
    if(i%2 ==0):
        for j in range(0, N-i):
            print(end="1")
    elif (i%2!=0):
        for j in range(0,N-i):
            print(end="0")
    print()
