def sol(n):
    if n==0:
        return 0
    elif n==2:
        return 2
    a = 0
    b = 1
    for i in range(2,n+1):
        c= a + b
        a = b
        b = c
    return a + b
class Solution:
    def climbStairs(self, n: int) -> int:
        return sol(n)