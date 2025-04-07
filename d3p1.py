import re

def solve_puzzle(memory: str):
    # Regular expression to find valid mul instructions in the format mul(X,Y)
    mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

    # Find all matches in the memory
    matches = re.findall(mul_pattern, memory)
    
    # Sum up the multiplication results
    total_sum = sum(int(x) * int(y) for x, y in matches)
    
    return total_sum

# Read the file content
file_path = 'day3.txt'
with open(file_path, 'r') as file:
    memory_content = file.read()

# Process the memory content and calculate the sum of the multiplications
result = solve_puzzle(memory_content)
print(f"The total sum of the multiplications is: {result}")
