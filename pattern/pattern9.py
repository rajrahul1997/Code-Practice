'''Program to print pattern below
       1
      23
     345
    4567
   56789
if (N=5) is given by user
here one loop of i is running for row in range(0,N)
and 2 loop of j in running ,one in range(0,N-i) to give space and another loop of j in range(0,i+1) to print(i+j+1)'''

N= int(input("input:"))
for i in range(0,N):
    for j in range(0,N-i):
        print(end =" ")
    for j in range(0,i+1):
        print(i+j+1,end="")
    print()
