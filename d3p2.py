import re

def solve_puzzle(memory: str):
    # Regular expression to find valid mul instructions in the format mul(X,Y)
    mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    # Regular expression to detect "do()" and "don't()" commands
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"
    
    # Initially mul instructions are enabled
    is_mul_enabled = True
    total_sum = 0
    
    # Split the input into tokens, considering mul instructions and commands
    tokens = re.split(r"(\bmul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\))", memory)
    
    # Iterate through the tokens and process the instructions
    for token in tokens:
        if re.match(mul_pattern, token):  # If the token is a mul instruction
            if is_mul_enabled:
                # Extract the numbers and calculate the multiplication
                x, y = map(int, re.findall(r"\d+", token))
                total_sum += x * y
        elif re.match(do_pattern, token):  # If the token is "do()"
            is_mul_enabled = True  # Enable mul instructions
        elif re.match(dont_pattern, token):  # If the token is "don't()"
            is_mul_enabled = False  # Disable mul instructions
    
    return total_sum


# Read the file content
file_path = 'day3.txt'
with open(file_path, 'r') as file:
    memory_content = file.read()

# Process the memory content and calculate the sum of the multiplications
result = solve_puzzle(memory_content)
print(f"The total sum of the multiplications is: {result}")
