def climbStairs1(n):
    dp = [1,1]

    for i in range(2,n+1):
        dp.append(dp[i-1]+dp[i-2])

    return dp[-1]


def climbStairs2(n):
    first, second=1,1

    for i in range(2,n+1):
        temp = second
        second = first+second
        first = temp

    return second