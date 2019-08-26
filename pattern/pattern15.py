'''Program to print pattern below
        R
        R A
        R A H
        R A H U
        R A H U L
if (string) is given by user'''
word= input("input:")
N = len(word)
for i in range(0,N+1):
    for j in range(0,i):
        print(word[j],end ="")
    print()
