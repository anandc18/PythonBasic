language = 'Python'
lst = list(language) # changing the string to list
print(type(lst))     # list
print(lst)           # ['P', 'y', 't', 'h', 'o', 'n']

# Second way: list comprehension
lst = [i for i in language]
print(type(lst)) # list
print(lst)

# Forloop
for x in language:
    print(x)

lst = [i for i in language]
print(lst)

lst = [ i * i for i in range(11) if i % 2 ==0 ]
print(lst)

three_dimen_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [ number for row in three_dimen_list for number in row ]
print(flattened_list)

x = lambda param1, param2, param3: param1 + param2 + param2
print(x(1,2,3))
