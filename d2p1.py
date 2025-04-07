def is_safe_report(report):
    # Check if the report is either increasing or decreasing
    is_increasing = True
    is_decreasing = True
    
    # Check the difference between adjacent numbers and if the report is strictly increasing or decreasing
    for i in range(1, len(report)):
        diff = abs(report[i] - report[i - 1])
        if diff < 1 or diff > 3:  # Check if the difference is out of allowed range
            return False
        if report[i] < report[i - 1]:
            is_increasing = False
        elif report[i] > report[i - 1]:
            is_decreasing = False
    
    # The report is safe if it's either strictly increasing or strictly decreasing
    return is_increasing or is_decreasing

def count_safe_reports(file_path):
    safe_count = 0
    
    # Read the file and process each line
    with open(file_path, 'r') as f:
        for line in f:
            # Strip any leading/trailing whitespace and check for empty lines
            line = line.strip()
            if not line:
                continue
            
            # Try to convert the line to a list of integers
            try:
                report = list(map(int, line.split()))
            except ValueError:
                # If the line contains non-numeric values, skip it
                print(f"Skipping invalid line: {line}")
                continue
            
            # Check if the report is safe
            if is_safe_report(report):
                safe_count += 1
    
    return safe_count

# Count how many reports are safe
file_path = 'day2.txt'  # Replace with your file path
safe_reports = count_safe_reports(file_path)
print(f"Number of safe reports: {safe_reports}")
