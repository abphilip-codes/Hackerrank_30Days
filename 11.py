# https://www.hackerrank.com/challenges/30-2d-arrays/problem

#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    arr,summ = [],[]
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    for j in range(0,4):
        for i in range(0,4):
            summ.append(sum(arr[i][j:j+3])+arr[i+1][j+1]+sum(arr[i+2][j:j+3]))
    print(max(summ))
