for string in input_string:

input_string = ['abccccdd', 'a']
output_list = [] 


for string in input_string:
    length = palindrome_length_test(string)
    output_list.append(length)
print(output_list)

    
def palindrome_length_test(input_string):
    # Count the occurrences of each letter in the input string
    letter_counts = Counter(input_string)

    # Initialize the length of the palindrome
    palindrome_length = 0

    # Iterate through the letter counts
    for count in letter_counts.values():
        # Add the even count directly to the palindrome length
        palindrome_length += (count // 2) * 2

        # If the count is odd and greater than 0, add 1 to the palindrome length
        if count % 2 == 1 and palindrome_length % 2 == 0:
            palindrome_length += 1

    return palindrome_length

longest_palindrome_length("abccccdd")

input_list = ["5 4 10", "4 2 4 6 1", "2 1 8 5"]

for i in range(len(input_list)):
    input_list[i] = input_list[i].split()
    input_list[i] = [int(num) for num in input_list[i]]
    
print(input_list)
    
max_sum = input_list[0][2]
a_length = input_list[0][0]
b_length = input_list[0][1]

stack_a = sorted(input_list[1])
stack_b = sorted(input_list[2])

def max_integers_for_sum(stack_a, stack_b, max_sum):
    running_sum = 0 
    i = 0
    j = 0
    counter = 0

    while i < a_length or j < b_length:
        if ((j == b_length) or (i < a_length and stack_a[i] <= stack_b[j])) and (stack_a[i] + running_sum <= max_sum):
                counter += 1
                i += 1
                running_sum += stack_a[i]
        elif ((i == a_length) or (j < b_length and stack_b[j] <= stack_a[i])) and (stack_b[j] + running_sum <= max_sum):
                counter += 1
                j += 1
                running_sum += stack_b[j]
        else:
            break
            
    return counter
           
output =  max_integers_for_sum(stack_a, stack_b, max_sum)   
print(output)
        
