# https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem

d = {}
for T in range(int(input())):
    a,b = map(str,input().split(" "))
    d[a]=b
while True:
    try:
        query = input()
        if query in d: print("{}={}".format(query,d[query]))
        else: print("Not found")
    except: break
