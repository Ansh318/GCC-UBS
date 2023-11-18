def portfolio_operations_solution(input_data):
    input_data = convert_to_int(input_data)
    result = {'answer': []}
    for i in range(len(input_data)):
        max_sum = input_data[i][0][2]
        stack_a = input_data[i][1]
        stack_b = input_data[i][2]
        max_selections = max_profit(stack_a, stack_b, max_sum)
        result['answer'].append(max_selections)
    return result


# noinspection DuplicatedCode
def convert_to_int(input_data):
    for i in range(len(input_data)):
        for j in range(len(input_data[i])):
            input_data[i][j] = input_data[i][j].split()
            input_data[i][j] = [int(num) for num in input_data[i][j]]
    return input_data


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
