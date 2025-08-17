def lower_cost(string, A, B):
    if not all(c in '01' for c in string):
        return "INVALID"

    orig_cost = 0
    for i in range(len(string) - 1):
        if string[i:i+2] in ['01', '10']:
            orig_cost += A if string[i:i+2] == '01' else B

    min_cost = orig_cost
    minihamdist = len(string)
    for i in range(len(string)):
        if i == 0:
            new_string = string[-1] + string[1:]
        elif i == len(string) - 1:
            new_string = string[:-1] + string[0]
        else:
            new_string = string[:i] + string[i+1] + string[i]
        new_cost = 0
        for j in range(len(new_string) - 1):
            if new_string[j:j+2] in ['01', '10']:
                new_cost += A if new_string[j:j+2] == '01' else B
        if new_cost < min_cost:
            min_cost = new_cost
            minihamdist = sum(1 for a, b in zip(string, new_string) if a != b)
        elif new_cost == min_cost and sum(1 for a, b in zip(string, new_string) if a != b) < minihamdist:
            minihamdist = sum(1 for a, b in zip(string, new_string) if a != b)

    return minihamdist

test_cases = int(input("Enter the number of test cases: "))

for _ in range(num_test_cases):
    string = input("Enter the binary string: ")
    A = int(input("Enter the value of A: "))
    B = int(input("Enter the value of B: "))
    print(lower_cost(string, A, B))
