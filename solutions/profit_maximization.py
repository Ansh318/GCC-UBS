def profit_maximization_solution(input_data):
    result = {'answer': []}
    for i in range(len(input_data)):
        input_data[i] = input_data[i].split()
        input_data[i] = [int(num) for num in input_data[i]]
        stock_prices = input_data[i][1:]
        max_profit_result = max_profit(stock_prices)
        result['answer'].append(max_profit_result)
    return result


def max_profit(prices):
    max_profit_result = 0
    buy = prices[0]
    for sell in prices[1:]:
        if sell > buy:
            spread = sell - buy
            # noinspection PyTypeChecker
            max_profit_result = max(max_profit, spread)
        else:
            buy = sell
    return max_profit_result
