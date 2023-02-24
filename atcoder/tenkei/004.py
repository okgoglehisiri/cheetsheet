#import 
# import pypyjit
import sys
from itertools import product
# pypyjit.set_param('max_unroll_recursion=-1')
# 再帰上限変更
sys.setrecursionlimit(1000000)
#---------------------------------------#
#input

H,W = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(H)]

#--------------------------------------#
#solve

v_sum = []
h_sum = []

for i in range(H):
    temp = 0
    for j in range(W):
        temp += A[i][j]
    v_sum.append(temp)


for i in range(W):
    temp = 0
    for j in range(H):
        temp += A[j][i]
    
    h_sum.append(temp)

for i in range(H):

    for j in range(W):
        print(v_sum[i] + h_sum[j] - A[i][j],end=' ')
    
    print()

