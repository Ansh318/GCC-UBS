
def coin_change_solution(input_data):
    input_data = convert_to_int(input_data)
    result = {'answer': []}
    for i in range(len(input_data)):
        amount = input_data[i][0][0]
        n = input_data[i][0][1]
        coins = input_data[i][1]
        max_selections = count_change(coins, n, amount)
        result['answer'].append(max_selections)
    return result


# noinspection DuplicatedCode
def convert_to_int(input_data):
    for i in range(len(input_data)):
        for j in range(len(input_data[i])):
            input_data[i][j] = input_data[i][j].split()
            input_data[i][j] = [int(num) for num in input_data[i][j]]
    return input_data


def count_change(coins, n, amount):
    # If amount is 0 then we have a valid solution
    if amount == 0:
        return 1

    # If amount is less than 0 then no solution exists
    if amount < 0:
        return 0

    # If there are no coins and amount is greater than 0, then no solution exists
    if n <= 0:
        return 0

    return count_change(coins, n - 1, amount) + count_change(coins, n, amount - coins[n - 1])
