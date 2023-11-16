def profit_maximization_solution(input_data):
  result = {'answer' : []}
  for i in range(len(input_data)):
    input_data[i] = input_data[i].split()
    input_data[i] = [int(num) for num in input_data[i]]
    num_pred_days = input_data[i][0]
    stock_prices = input_data[i][1:]
    max_profit = maxProfit(stock_prices)
    result['answer'].append(max_profit)
  return result
 
def maxProfit(prices):
    max_profit = 0
    buy = prices[0]
    for sell in prices[1:]:
        if sell > buy:
            max_profit = max(max_profit, sell - buy)
        else:
            buy = sell
    return max_profit
