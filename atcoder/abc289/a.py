#import 
# import pypyjit
import sys
from itertools import product
# pypyjit.set_param('max_unroll_recursion=-1')
# 再帰上限変更
sys.setrecursionlimit(1000000)
#---------------------------------------#
#input

s = input()

#--------------------------------------#
#solve
ans = ''

for i in range(len(s)):
    if s[i] == '1':
        ans += '0'
    else:
        ans += '1'

print(ans)