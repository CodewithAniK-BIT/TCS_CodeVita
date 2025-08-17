num_lines = int(input("Enter the number of input lines (between 4 and 20): "))

# Validate the input
while num_lines < 4 or num_lines > 20:
    num_lines = int(input("Invalid input. Enter the number of input lines (between 4 and 20): "))

states = set()
transitions = {}
for _ in range(num_lines):
    present_state, next_state, input_val, output_val = input("Enter present state, next state, input (0/1), and output (0/1) separated by spaces: ").split()
    
    # Add states and transitions to the dictionaries
    states.add(present_state)
    states.add(next_state)
    transitions[(present_state, input_val)] = (next_state, output_val)