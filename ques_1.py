"""
Use the following functions to add, multiply and divide, taking care of the modulo operation.
Use mod_add to add two numbers taking modulo 1000000007. ex : c=a+b --> c=mod_add(a,b)
Use mod_multiply to multiply two numbers taking modulo 1000000007. ex : c=a*b --> c=mod_multiply(a,b)
Use mod_divide to divide two numbers taking modulo 1000000007. ex : c=a/b --> c=mod_divide(a,b)
"""
import numpy as np
import time
M=1000000007

def mod_add(a, b):
    a=(a%M+M)%M
    b=(b%M+M)%M
    return (a+b)%M

def mod_multiply(a, b):
    a=(a%M+M)%M
    b=(b%M+M)%M
    return (a*b)%M

def mod_divide(a, b):
    a=(a%M+M)%M
    b=(b%M+M)%M
    return mod_multiply(a, pow(b, M-2, M))

# Problem 1a
def calc_prob(alice_wins, bob_wins):
    dp = [[0 for _ in range(bob_wins + 1)] for _ in range(alice_wins + 1)]
    
    # Base Case
    dp[1][1] = 1
    
    for a in range(1, alice_wins + 1):
        for b in range(1, bob_wins + 1):
            if a == 1 and b == 1:
                continue
            if a > 1:
                dp[a][b] = mod_add(dp[a][b], mod_multiply(dp[a-1][b], mod_divide(b, a + b - 1))) # when alice wins in the current game and has already won a-1 games in the past
            if b > 1:
                dp[a][b] = mod_add(dp[a][b], mod_multiply(dp[a][b-1], mod_divide(a, a + b - 1))) # when alice loses the current game and has already won a games in the past

    return dp[alice_wins][bob_wins]


    
# Problem 1b (Expectation)      
def calc_expectation(t):
    """
    Returns:
        The expected value of \sum_{i=1}^{t} Xi will be of the form p/q,
        where p and q are positive integers,
        return p.q^(-1) mod 1000000007.

    """
    ans = 0
    for i in range(-t+2,t-1):
        if (t+i)%2 == 0:
            ans=mod_add(ans,mod_multiply(i,calc_prob((t+i)//2,(t-i)//2))) # when the total points over n games are i 

    return ans


 

# Problem 1b (Variance)
def calc_variance(t):
    """
    Returns:
        The variance of \sum_{i=1}^{t} Xi will be of the form p/q,
        where p and q are positive integers,
        return p.q^(-1) mod 1000000007.

    """
    ans = 0 
    for i in range(-t+2,t-1):
        if (t+i)%2 == 0:
            ans=mod_add(ans,mod_multiply(mod_multiply(i,i),calc_prob((t+i)//2,(t-i)//2)))
    y=calc_expectation(t)
    expectation_squared = mod_multiply(y,y)
    return ans-expectation_squared 
    
   
print(calc_expectation(25))    
print(calc_prob(96,25))
print(calc_variance(25))