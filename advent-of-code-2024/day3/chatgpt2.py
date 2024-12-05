import re


def sum_multiplications_with_conditions(file_name):
    # Read the file
    with open(file_name, "r") as file:
        data = file.read()

    # Regular expressions for valid mul(X,Y) and control instructions
    mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    control_pattern = r"do\(\)|don't\(\)"

    # Find all matches for mul and control instructions
    mul_matches = [
        (match.start(), "mul", match.groups()) for match in re.finditer(mul_pattern, data)
    ]
    control_matches = [
        (match.start(), match.group(), None) for match in re.finditer(control_pattern, data)
    ]

    # Merge and sort the matches by position
    instructions = sorted(mul_matches + control_matches, key=lambda x: x[0])

    # Initialize state and sum
    enabled = True
    total = 0

    # Process each instruction in order
    for instruction in instructions:
        _, inst_type, payload = instruction

        if inst_type == "mul" and payload:  # This is a mul instruction
            if enabled:
                x, y = map(int, payload)
                total += x * y
        elif inst_type == "do()":  # This is a do() instruction
            enabled = True
        elif inst_type == "don't()":  # This is a don't() instruction
            enabled = False

    return total


# Call the function and print the result
if __name__ == "__main__":
    result = sum_multiplications_with_conditions("input.in")
    print(result)
