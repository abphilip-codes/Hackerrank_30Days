# https://www.hackerrank.com/challenges/30-running-time-and-complexity/problem

for T in range(int(input())):
    n=int(input())
    if(n==1): 
        print("Not prime")
        continue
    if(n==2):
        print("Prime")
        continue
    if(n%2==0):
        print("Not prime")
        continue
    for i in range(3,int(n**(1/2))+1,2):
        if(n%i==0): 
            print("Not prime")
            break
    else: print("Prime")