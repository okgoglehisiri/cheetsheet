#import 
# import pypyjit
import sys
import itertools
# pypyjit.set_param('max_unroll_recursion=-1')
# 再帰上限変更
sys.setrecursionlimit(1000000)
#---------------------------------------#
#input
N = int(input())
A = list(map(int,input().split()))
M = int(input())
B = list(map(int,input().split()))
X = int(input())
#--------------------------------------#
#solve

table = [0]*(X+1)

table[0] = 1
for i in B:
    table[i] = -1

    


for j in range(X+1):
    for i in A:
        if j >= i:
            if table[j] == 0 and table[j - i] == 1:
                table[j] = 1


if table[-1] == 1:
    print('Yes')

else:
    print('No')