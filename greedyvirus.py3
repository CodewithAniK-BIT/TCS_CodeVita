from sys import setrecursionlimit
from collections import defaultdict

setrecursionlimit(10**6)

def min_fudge_data(m, n, matrix, virus_pos, dummy_pos):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    visited = set()
    min_data_fudge = defaultdict(lambda: float('inf'))

    def dfs(x, y, total_fudged_data):
        if (x, y) == (dummy_pos[0] - 1, dummy_pos[1] - 1):
            return total_fudged_data
        visited.add((x, y))
        current_data = matrix[x][y]
        min_cost = float('inf')
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                neighbor_data = matrix[nx][ny]
                if neighbor_data > current_data:
                    min_cost = min(min_cost, dfs(nx, ny, total_fudged_data))
                elif neighbor_data < current_data:
                    fudge_needed = (current_data + 1) - neighbor_data
                    if total_fudged_data + fudge_needed < min_data_fudge[(nx, ny)]:
                        min_data_fudge[(nx, ny)] = total_fudged_data + fudge_needed
                        matrix[nx][ny] += fudge_needed
                        min_cost = min(min_cost, dfs(nx, ny, total_fudged_data + fudge_needed))
                        matrix[nx][ny] -= fudge_needed
        visited.remove((x, y))
        return min_cost

    result = dfs(virus_pos[0] - 1, virus_pos[1] - 1, 0)
    return result if result != float('inf') else -1

m, n = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(m)]
virus_pos = list(map(int, input().split()))
dummy_pos = list(map(int, input().split()))

print(min_fudge_data(m, n, matrix, virus_pos, dummy_pos))
