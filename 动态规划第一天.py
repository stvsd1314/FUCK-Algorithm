#####一.斐波那契数列问题
#1.暴力递归
def baoli_fib(N):
    if N==1 or N==2: return 1
    return baoli_fib(N-1)+baoli_fib(N-2)

#2.带备忘录的递归（不关心执行顺序，Notice:比如N=5,最后一个数就为5，但是memo最后一个为memo[4]）
def Beiwanglu_fib(N):
    if N<1: return 0
    memo = [0 for _ in range(N)]
    return helper(N,memo)
def helper(n,memo):
    if n==1 or n==2: return 1
    if memo[n-1]!=0: return memo[n-1]
    memo[n-1] = helper(n-1,memo)+helper(n-2,memo)
    return memo[n-1]
## Above is "Top 2 floor",Below is "Floor 2 Top"
# 1.中间保存数据为一个list,空间复杂度O(n)
def fib1(N):
    if N==1 or N==2: return 1
    dp =[0 for _ in range(N)]
    dp[0]=1
    dp[1]=1
    for i in range(2,N):
        dp[i] = dp[i-2]+dp[i-1]
    return dp[N-1]
# 2.中间保存2个数，空间复杂度O(1)
def fib2(N):
    if N==1 or N==2: return 1
    pre = 1
    cur = 1
    for i in range(2,N):
        sum = pre+cur
        pre = cur
        cur = sum
    return sum
## Test
print(fib1(6))
print(fib2(6))
print(Beiwanglu_fib(6))
print(baoli_fib(6))

#####二.凑零钱问题
#1.自顶向下
def coinCharge1(coins, amount):
    def dp(n):
        # base case
        if n == 0: return 0
        if n < 0: return -1
        # 求最小值，所以初始化为正无穷
        res = float('INF')
        for coin in coins:
            subproblem = dp(n - coin)
            # 子问题无解，跳过
            if subproblem == -1: continue
            res = min(res, 1 + subproblem)

        return res if res != float('INF') else -1

    return dp(amount)
#2.带备忘录的递归
def coinCharge2(coins,amount):
    memo = dict()
    def dp(n):
    #查备忘录，避免重复计算
        res = float("INF")
        if n in memo:return memo[n]
        if n==0: return 0
        if n<0: return -1
        for coin in coins:
            subproblem = dp(n-coin)
            if subproblem ==-1: continue
            res = min(res,1+subproblem)
        memo[n] =res if res!=float("INF") else -1
        return  memo[n]
    return dp(amount)
print(coinCharge2([1,2,3],0))

############################自底向上
#1.list作为中间存储(这个似乎不能再降低空间复杂度了）
def coinCharge3(coins,amount):
    dp = [amount+1 for _ in range(amount+1)]
    dp[0] = 0
    for i in range(amount+1):
        for coin in coins:
            if i-coin < 0: continue
            dp[i] = min(dp[i],1+dp[i-coin])
    return dp[amount]
print(coinCharge3([1,3,5],10))








