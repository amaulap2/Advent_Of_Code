def count_xmas(word_search):
    n = len(word_search)
    xmas_count = 0

    # Loop through the grid to find "A"
    for r in range(1, n - 1):  # Skip the borders to avoid out of range errors
        for c in range(1, n - 1):
            if word_search[r][c] == 'A':  # Check if it's an "A"
                # Check the top-left, bottom-right diagonal (S-M)
                if word_search[r - 1][c - 1] == 'S' and word_search[r + 1][c + 1] == 'M':
                    if (word_search[r - 1][c + 1] == 'S' and word_search[r + 1][c - 1] == 'M') or (word_search[r - 1][c + 1] == 'M' and word_search[r + 1][c - 1] == 'S'):
                        xmas_count += 1
                if word_search[r - 1][c - 1] == 'M' and word_search[r + 1][c + 1] == 'S':
                    # Check the top-right, bottom-left diagonal (S-M)
                    if (word_search[r - 1][c + 1] == 'M' and word_search[r + 1][c - 1] == 'S') or (word_search[r - 1][c + 1] == 'S' and word_search[r + 1][c - 1] == 'M'):
                        xmas_count += 1


    return xmas_count

# Read the input grid from a file or predefined text
file_path = 'day4.txt'
with open(file_path, 'r') as file:
    grid = [line.strip() for line in file.readlines()]

# Find how many times "XMAS" appears
result = count_xmas(grid)
print(f"The word XMAS appears {result} times.")
