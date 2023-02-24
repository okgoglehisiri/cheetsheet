#import 
# import pypyjit
import sys
from itertools import product
# pypyjit.set_param('max_unroll_recursion=-1')
# 再帰上限変更
sys.setrecursionlimit(1000000)
#---------------------------------------#
#input

N,M = map(int,input().split())


#--------------------------------------#
#solve

ans = list(range(1,N+1,1))
result = []



if(M > 0):
    x = list(map(int,input().split()))
    tmp = [x[0]]
    for i in range(len(x)-1):

        if x[i+1] - x[i] == 1:

            tmp.append(x[i+1])

        else:

            if len(tmp) > 0:

                result.append(tmp)

            tmp = []

            tmp.append(x[i+1])

    result.append(tmp)



    for i in range(len(result)):
        result[i].append(result[i][-1]+1)
        for j in range(len(result[i])):
            ans[result[i][j]-1] += len(result[i]) - 2 * j - 1


for i in ans:
    print(i, end = ' ')

