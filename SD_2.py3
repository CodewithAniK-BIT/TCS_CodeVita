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

def find_sequences(start_state, end_state, sequence="", is_overlapping=False):
    if start_state == end_state:
        if "101" in sequence:
            print(f"Sequence: {sequence}")
            print(f"Overlapping: {is_overlapping}")
        else:
            print(f"Sequence: {sequence}")
            print("Non-overlapping")
        return

    for input_val in ["0", "1"]:
        if (start_state, input_val) in transitions:
            next_state, output_val = transitions[(start_state, input_val)]
            new_sequence = sequence + input_val + output_val
            is_new_overlapping = is_overlapping or (new_sequence[-2:] == "11")
            find_sequences(next_state, end_state, new_sequence, is_new_overlapping)

find_sequences("a", "a")
