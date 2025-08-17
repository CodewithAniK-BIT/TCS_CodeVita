def lower_cost(bstring, A, B):
    if not all(c in '01' for c in bstring):
        return "INVALID"
    n = len(bstring)
    cost = [0] * n
    min_cost = float('inf')
    min_hamming_distance = n
    for i in range(n - 1):
        cost[i] = A if bstring[i:i+2] == '01' else B if bstring[i:i+2] == '10' else 0
    for i in range(n):
        new_cost = sum(cost[i:] + cost[:i])
        new_string = bstring[i:] + bstring[:i]
        hamming_distance = sum(1 for a, b in zip(bstring, new_string) if a != b)
        if new_cost < min_cost:
            min_cost = new_cost
            min_hamming_distance = hamming_distance
        elif new_cost == min_cost and hamming_distance < min_hamming_distance:
            min_hamming_distance = hamming_distance
    return min_hamming_distance
testcases = int(input("Enter the number of test cases: "))

for _ in range(testcases):
    bstring = input("Enter binary string: ")
    A = int(input("Enter cost A: "))
    B = int(input("Enter cost B: "))
    print(lower_cost(bstring, A, B))
