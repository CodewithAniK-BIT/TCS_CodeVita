from sys import stdin, stdout
import collections

def find_cells_with_score_k(n, m, table, k):
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = 1 
    for i in range(n):
        for j in range(m):
            if dp[i][j] > 0:  
                # Move towards right dp table
                if j + 1 < m and table[i][j + 1] >= table[i][j]:
                    dp[i][j + 1] += dp[i][j]
                # Move towards down dp table
                if i + 1 < n and table[i + 1][j] >= table[i][j]:
                    dp[i + 1][j] += dp[i][j]
    result = []
    for i in range(n):
        for j in range(m):
            if dp[i][j] == k:
                result.append(f"{i} {j}")
    if result:
        stdout.write("\n".join(result) + "\n")
    else:
        stdout.write("NO\n")
        
input = stdin.read().strip().splitlines()
n, m = map(int, input[0].split())
table = [list(map(int, line.split())) for line in input[1:n+1]]
k = int(input[n+1])

find_cells_with_score_k(n, m, table, k)