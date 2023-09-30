 # Sum and multiplication in list

# def sum_and_mult(arr: list):
#     arr_sum = 0
#     arr_mult = 1
#
#     for element in arr:
#         arr_sum += element
#         arr_mult *= element
#
#     print(arr)
#     print([arr_sum, arr_mult])
#
# sum_and_mult([1, 7, 3])


 # Find max item and index in a list for this item

# def find_max_number(arr: list):
#     max_index = 0
#     max_item = arr[0]
#
#     for i in range(1, len(arr)):
#         if arr[i] > max_item:
#             max_item = arr[i]
#             max_index = i
#
#     return [max_index, max_item]
#
# print(find_max_number([1, 45, 33, 76, 9, 10]))


 # Sum between min an max element

# def sum_between_max_and_min(arr: list):
#     min_index = 0
#     max_index = 0
#
#     for i in range(len(arr)):
#         if arr[i] > arr[max_index]:
#             max_index = i
#
#         if arr[i] < arr[min_index]:
#             min_index = i
#
#     return sum(arr[min(min_index, max_index) + 1:max(min_index, max_index)])
#
#     # return [min_index, max_index]
#
# print(sum_between_max_and_min([1, 2, 3, 4, 5]))
# print(sum_between_max_and_min([5, 4, 3, 2, 1]))


 # Given array where price[i] is the price on the ith day.maximaze profit. Return max profit.
 # prices = [7,1,5,3,6,4] Return: 5
 # Buy on day 2 (price=1) sell on day 5(price=6), 6-1=5

# def buy_and_sell_stock(prices: list):
#     curr_profit = max_profit = 0
#
#     for i in range(len(prices) - 1):
#         curr_profit = curr_profit + prices[i + 1] - prices[i]
#         if curr_profit > max_profit:
#             max_profit = curr_profit
#         if curr_profit < 0:
#             curr_profit = 0
#
#     return max_profit
#
# print(buy_and_sell_stock([7, 1, 5, 3, 6, 4]))


 # Best time to Buy and Sell Stock 2. Can Buy and Sell a few times

def buy_and_sel_stock(prices: list):
    profit = 0

    for i in range(len(prices) - 1):
        if prices[i +1] - prices[i] > 0:
            profit += prices[i +1] - prices[i]

    return profit


test_prices = [7, 1, 5, 3, 6, 4]
print(buy_and_sel_stock(test_prices))