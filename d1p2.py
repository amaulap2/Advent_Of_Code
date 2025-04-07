from collections import Counter

def calculate_similarity_score(file_path):
    # Read the file and process the contents
    with open(file_path, 'r') as file:
        left_list = []
        right_list = []
        
        # Read each line, split the numbers and add them to the respective lists
        for line in file:
            if line.strip():  # Skip empty lines
                parts = line.split()
                if len(parts) == 2:
                    left, right = map(int, parts)
                    left_list.append(left)
                    right_list.append(right)
    
    # Count frequencies of numbers in the right list
    right_count = Counter(right_list)
    
    # Calculate the similarity score
    similarity_score = 0
    for number in left_list:
        similarity_score += number * right_count[number]
    
    return similarity_score

# Example usage
file_path = 'data.txt'  # Replace with your file path
similarity_score = calculate_similarity_score(file_path)
print(f"Similarity score: {similarity_score}")
