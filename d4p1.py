def count_xmas_occurrences(grid):
    # The word we are searching for
    word = "XMAS"
    word_length = len(word)
    num_rows = len(grid)
    num_cols = len(grid[0])

    # Directions to search for: (row_offset, col_offset)
    directions = [
        (-1, 0), # up
        (1, 0),  # down
        (0, -1), # left
        (0, 1),  # right
        (-1, -1), # top-left diagonal
        (1, 1),   # bottom-right diagonal
        (-1, 1),  # top-right diagonal
        (1, -1)   # bottom-left diagonal
    ]
    
    def is_valid(x, y):
        return 0 <= x < num_rows and 0 <= y < num_cols

    def check_word(x, y, dx, dy):
        # Check if the word "XMAS" fits starting from (x, y) in the direction (dx, dy)
        for i in range(word_length):
            new_x = x + i * dx
            new_y = y + i * dy
            if not is_valid(new_x, new_y) or grid[new_x][new_y] != word[i]:
                return False
        return True

    count = 0

    # Iterate over every cell in the grid
    for i in range(num_rows):
        for j in range(num_cols):
            # For each direction, check if "XMAS" can start at grid[i][j]
            for dx, dy in directions:
                if check_word(i, j, dx, dy):
                    count += 1

    return count

# Read the input grid from a file or predefined text
file_path = 'day4.txt'
with open(file_path, 'r') as file:
    grid = [line.strip() for line in file.readlines()]

# Find how many times "XMAS" appears
result = count_xmas_occurrences(grid)
print(f"The word XMAS appears {result} times.")
