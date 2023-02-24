import sys
import itertools
import math
import bisect
import collections
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
inf = 1 << 60
#pypyjit.set_param('max_unroll_recursion=-1')
#再帰上限変更
sys.setrecursionlimit(1000000)

#==============================================================================#
# UnionFind
class UnionFind:
    def __init__(self,n):
        self.n=n
        self.parent_size=[-1]*n

    def leader(self,a):
        if self.parent_size[a]<0: return a
        self.parent_size[a]=self.leader(self.parent_size[a])
        return self.parent_size[a]

    def merge(self,a,b):
        x,y=self.leader(a),self.leader(b)
        if x == y: return 
        if abs(self.parent_size[x])<abs(self.parent_size[y]):x,y=y,x
        self.parent_size[x] += self.parent_size[y]
        self.parent_size[y]=x
        return 

    def same(self,a,b):
        return self.leader(a) == self.leader(b)

    def size(self,a):
        return abs(self.parent_size[self.leader(a)])

    def groups(self):
        result=[[] for _ in range(self.n)]
        for i in range(self.n):
            result[self.leader(i)].append(i)
        return [r for r in result if r != []]

class combination:
    def mcomb(n, k):
        a = 1
        b = 1
        for i in range(k):
            a *= n - i
            a %= 1000000007
            b *= i + 1
            b %= 1000000007
        return a * pow(b, 1000000005, 1000000007) % 1000000007

class inp:
    def n():
        return int(input())
    def m():
        return map(int,input().split())
    def l():
        return list(map(int,input().split()))
    def n1(m):
        A = []
        for _ in range(m):
            A.append(int(input()))
    def n2(m):
        xy = [map(int,input().split()) for _ in range(m)]
        x,y = [list(i) for i in zip(*xy)]
        return x,y
    def nm(m):
        a = [list(map(int, input().split())) for l in range(m)]
        return a        
#==============================================================================#


def main():
    N = inp.n()
    print(1,end='')
    for i in range(N-1):
        print(0,end='')
    print(7)

if __name__ == '__main__':
    main()