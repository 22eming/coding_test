X = int(input())
dp = [0] * (X+1)

for i in range(2, X+1):
    dp[i] = dp[i-1] + 1
    if not i % 3:
        dp[i] = min(dp[i], dp[i//3] + 1)
    if not i % 2:
        dp[i] = min(dp[i], dp[i//2] + 1)

print(dp[-1])