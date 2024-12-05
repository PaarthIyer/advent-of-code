import re

def sum_multiplications(file_name):
    # Read the file
    with open(file_name, 'r') as file:
        data = file.read()
    
    # Regular expression to find valid mul(X,Y) patterns
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    
    # Find all matches
    matches = re.findall(pattern, data)
    
    # Calculate the sum of products
    total = sum(int(x) * int(y) for x, y in matches)
    
    return total

# Call the function and print the result
if __name__ == "__main__":
    result = sum_multiplications('input.in')
    print(result)
