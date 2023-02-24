#import pypyjit
import sys
import itertools
import math
from bisect import bisect_left
import collections
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
inf = 1 << 60
#pypyjit.set_param('max_unroll_recursion=-1')
#再帰上限変更
sys.setrecursionlimit(1000000)
#S = []
#for _ in range (X)
#	S.append(input()) # X回入力がある文字列を配列に追加する(数値ならint())
#	S = [input() for _ in range(X)]　# 内包表記のパターン(数値ならint())
#S = int(input())
#x = [0] * S
#y = [0] * S
#z = [0] * S
#for i in range(S)
#	x[i], y[i], z[i] = map(int, input().split()) # 複数行＋複数列
#S = int(input())
#for _ in range(S):
#	x, y = map(int, input().split()) # 複数行＋複数列（行ごと）
#---------------------------------------#
#input
# N = int(input())


# A = list(map(int,input().split()))
#--------------------------------------#
#solve
def main():

    N,K = map(int,input().split())
    C = list(map(int,input().split()))
    counter = Counter(C[0:K])
    ans = len(counter)
    for i in range(K,N):
        forward = C[i-K]
        back = C[i]
        counter[forward] -= 1
        counter[back] += 1
        if counter[forward] == 0:
            del counter[forward]
        ans = max(ans,len(counter))
    
    print(ans)
        

if __name__ == '__main__':
    main()