# https://www.hackerrank.com/challenges/30-sorting/problem

#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    num = 0
    for i in range(0,n):
        for j in range(0,n-1):
            if (a[j]>a[j+1]): a[j],a[j+1],num=a[j+1],a[j],num+1
    print("Array is sorted in {} swaps.\nFirst Element: {}\nLast Element: {}".format(num,a[0],a[-1]))