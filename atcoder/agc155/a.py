#import 
# import pypyjit
import sys
import itertools
from functools import lru_cache
# pypyjit.set_param('max_unroll_recursion=-1')
# 再帰上限変更
sys.setrecursionlimit(1000000)
#---------------------------------------#
#input

#--------------------------------------#
#solve

import sys

testcase = int(input())
from collections import Counter

def isPalindrome(s):
    
    ns = len(s)
    for i in range(ns//2):
        if s[i] != s[-i-1]:
            return False
    return True

from math import gcd
for _ in range(testcase):
    n,k = map(int,input().split())
    s = input()
    
    if k <= n:
        t = s[:k][::-1]
        
        if isPalindrome("".join[s]+[t]) and isPalindrome("".join())