#import 
# import pypyjit
import sys
import itertools
# pypyjit.set_param('max_unroll_recursion=-1')
# 再帰上限変更
sys.setrecursionlimit(1000000)
#---------------------------------------#
#input
N,K = map(int,input().split())
S = input()

#--------------------------------------#
#solve

ans = ''
listS = list(S)
nokori = K
for i in listS:
    if i == 'o' and nokori > 0:
        ans += 'o'
        nokori -= 1
    
    elif i == 'x' or nokori == 0:
        ans += 'x'

print(ans)