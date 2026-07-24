# map 
# numbers = [1, 2, 3]
# result = map(lambda x: x * 10, numbers)

# print(result)
# # Output: <map object at 0x7f8b9c...>








# list
# def add_sales_tax(price):
#     return price * 1.10


# menu_prices = [10.00, 20.00, 5.00]

# # Pass the function by its name (no parentheses!)
# final_prices = list(map(add_sales_tax, menu_prices))

# print(final_prices)
# # Output: [11.0, 22.0, 5.5]






# filter 
words = ["cat", "window", "dog", "python", "sky"]

# The lambda checks: Is the length of the word greater than 4?
long_words = list(filter(lambda w: len(w) > 4, words))

print(long_words)
# Output: ['window', 'python']