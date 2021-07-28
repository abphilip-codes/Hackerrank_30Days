# https://www.hackerrank.com/challenges/30-regex-patterns/problem

#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input().strip())
    a=[]
    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()
        firstName = first_multiple_input[0]
        emailID = first_multiple_input[1]
        if '@gmail.com' in emailID: a.append(firstName)
    print(*sorted(a), sep='\n')