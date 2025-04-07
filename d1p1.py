def calculate_distance_from_file(file_path):
    # Read the file and process the contents
    with open(file_path, 'r') as file:
        left_list = []
        right_list = []
        
        # Read each line, split the numbers and add them to the respective lists
        for line in file:
            # Skip empty lines or lines that don't contain exactly two numbers
            if line.strip():  # Skip empty lines
                parts = line.split()
                if len(parts) == 2:
                    left, right = map(int, parts)
                    left_list.append(left)
                    right_list.append(right)
                else:
                    print(f"Skipping malformed line: {line.strip()}")
    
    # Sort both lists
    left_list.sort()
    right_list.sort()
    
    # Calculate the sum of distances
    total_distance = 0
    for l, r in zip(left_list, right_list):
        total_distance += abs(l - r)
    
    return total_distance

# Example usage
file_path = 'data.txt'  # Replace with your file path
total_distance = calculate_distance_from_file(file_path)
print(f"Total distance: {total_distance}")
