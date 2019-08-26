'''Program to print pattern below
      0
     101
    21012
   3210123
  432101234
 if (N=4) is given by user
 here three loop of j is running 1st one is printing space
 2nd loop is ruuning from j(i,0,-1) and printing value of left side to zero
 3rd loop is ruuning from j(0,i+1) an dprinting value of right side to zero'''
N= int(input("input:"))
for i in range(0,N+1):
    for j in range(0,N-i-1):
        print(end ="")
    for j in range(i,0,-1):
        print(j,end = "")
    for j in range(0,i+1):
        print(j,end = "")
    print()
