import json 
from collections import Counter

#QUESTION 1 - FILE REORGANIZATION

# Open the JSON file for reading
with open('sample_data.json', 'r') as json_file:
    # Load the JSON data from the file
    data = json.load(json_file)
    
def palindrome_length_test(data):
    result = {'answer' : []}
    for file_name in data['inputs']:
        # Count the occurrences of each letter in the input string
        letter_counts = Counter(file_name)
        # Initialize the length of the palindrome
        palindrome_length = 0
        # Iterate through the letter counts
        for count in letter_counts.values():
            # Add the even count directly to the palindrome length
            palindrome_length += (count // 2) * 2
            # If the count is odd and greater than 0, add 1 to the palindrome length
            if count % 2 == 1 and palindrome_length % 2 == 0:
                palindrome_length += 1
        result['answer'].append(palindrome_length)
    print(result)
    return result
palindrome_length_test(data)


#QUESTION 2 - PORTFOLIO OPERATIONS

with open('sample_data_2.json', 'r') as json_file:
    # Load the JSON data from the file
    data2 = json.load(json_file)

input_ls = data2['inputs']

def convert_to_int(input_data):
    for i in range(len(input_data)):
        for j in range(len(input_data[i])):
            input_data[i][j] = input_data[i][j].split()
            input_data[i][j] = [int(num) for num in input_data[i][j]]
    return input_data
input_data = convert_to_int(input_ls)

def max_profit(stack_a, stack_b, max_sum):
    # Initialize variables
    current_sum = 0
    total_removed = 0

    while stack_a or stack_b:
        # Determine which stack to pop from
        if not stack_a:
            popped = stack_b.pop(0)
        elif not stack_b:
            popped = stack_a.pop(0)
        else:
            # Choose the stack that minimizes the increase in the running sum
            if stack_a[0] <= stack_b[0]:
                popped = stack_a.pop(0)
            else:
                popped = stack_b.pop(0)   
        # Check if the running sum exceeds maxSum
        if popped + current_sum <= max_sum:
            total_removed += 1
            current_sum += popped
        else:
            break

    return total_removed
        
def calculate(input_data):
    result = {'answer' : []}
    for i in range(len(input_data)):
        max_sum = input_data[i][0][2]
        stack_a = input_data[i][1]
        stack_b = input_data[i][2]
        max_selections = max_profit(stack_a, stack_b, max_sum)
        result['answer'].append(max_selections)
    print(result)
    return result
calculate(input_data)


        