def fib_recursive(n, counts):
    """
    Return the nth Fibonacci number. 
    counts is a list of n+1 elements, where counts[i] is incremented
    each time fib_recursive(i, counts) is called.
    """    
    if n == 0:
        return 0
    if n == 1:
        return 1
    counts[n] += 1
    return fib_recursive(n-1,counts) +fib_recursive(n-2,counts)
    

    
def fib_top_down(n, fibs):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_top_down(n - 1, memo) + fib_top_down(n - 2, memo)
    return memo[n]



def fib_bottom_up(n):
    if n <= 1:
            return n
        dp = [0] * (n + 1)
        dp[0]= 0
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
counts  = [0,0,0,0,0,0,0,0,0]
print(fib_recursive(8,counts))
print(counts)
