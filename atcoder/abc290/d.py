#import 
# import pypyjit
import sys
import itertools
import math
# pypyjit.set_param('max_unroll_recursion=-1')
# 再帰上限変更
sys.setrecursionlimit(1000000)
#---------------------------------------#
#input
T = int(input())

#--------------------------------------#
#solve




def solve(N,D,K):

    gcd_ND = math.gcd(N,D)
    
    lcd_ND = N * D / gcd_ND
    lcm = int(lcd_ND)
    count = (K-1) * D // lcm

    num = count + (K-1) * D
    print(num)
    ans = num % N
    
    
    return ans




for _ in range(T):
    
    N,D,K = map(int,input().split())
    #print(solve(N,D,K))
    solve(N,D,K)