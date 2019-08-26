'''Program to print pattern below
      1
      12
      123
      1234
      12345
if (N=5) is given by user
here one loop of  i is runing for row and one loop of j is running for column to print the value of j recursively '''
N= int(input("input:"))
for i in range(0,N+1):
    for j in range(1,i+1):
        print(j,end ="")
    print()
