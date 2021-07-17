# https://www.hackerrank.com/challenges/30-more-exceptions/problem

class Calculator:
    def power(self,n,p):
        self.n,self.p = n,p
        if(n<0 or p<0): raise ValueError("n and p should be non-negative")
        else: return n**p

myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)