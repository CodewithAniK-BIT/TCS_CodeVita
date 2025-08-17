from collections import defaultdict, deque

def parse_hierarchy(n, hierarchy_info):
    tree = defaultdict(list)
    parent = {}
    levels = {}
    
    for line in hierarchy_info:
        parent_tune, children_tunes = line.split(" : ")
        children = children_tunes.split()
        for child in children:
            parent[child] = parent_tune
            tree[parent_tune].append(child)
    
    queue = deque([(list(tree.keys())[0], 0)])
    while queue:
        tune, level = queue.popleft()
        levels[tune] = level
        for child in tree[tune]:
            queue.append((child, level + 1))
    
    return levels

def max_concordance_score(melody1, melody2, levels, A, B, C):
    len1, len2 = len(melody1), len(melody2)
    dp = [[-float('inf')] * (len2 + 1) for _ in range(len1 + 1)]
    dp[0][0] = 0
    
    for i in range(len1 + 1):
        for j in range(len2 + 1):
            if i < len1:
                dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] - C)
            if j < len2:
                dp[i][j + 1] = max(dp[i][j + 1], dp[i][j] - C)
            if i < len1 and j < len2:
                if melody1[i] == melody2[j] or levels[melody1[i]] == levels[melody2[j]]:
                    dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + A)
                else:
                    dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] - B)
    
    return dp[len1][len2]

n = int(input())
hierarchy_info = [input().strip() for _ in range(n)]
melody1 = input().strip().split('-')
melody2 = input().strip().split('-')
A, B, C = map(int, input().strip().split())

levels = parse_hierarchy(n, hierarchy_info)
print(max_concordance_score(melody1, melody2, levels, A, B, C))
