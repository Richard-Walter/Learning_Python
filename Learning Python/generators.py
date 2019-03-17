'''Old typical way of looping through'''


# def square_numbers(nums):
#     result = []
#     for i in nums:
#         result.append(i*i)
#     return result


'''Generators allows for more readable code-and is better for performance with very large lists'''
# Using generators instead of the above


def square_numbers(nums):
    for i in nums:
        yield (i*i)     # Generator one number at a time - need to ask for the next result


# Run the generator
my_nums = square_numbers([1, 2, 3, 4, 5])

print(next(my_nums)) # ask for the next result
print(next(my_nums)) # ask for the next result
print(next(my_nums)) # ask for the next result
print(next(my_nums)) # ask for the next result
print(next(my_nums)) # ask for the next result
# print(next(my_nums)) # ask for the next result  # This would product a StopIteration Exception

#  Use for loop to get all results of the generator
for num in my_nums:
    print(num)


'''Creating generator using round brackets from list comprehension'''
my_nums = (x*x for x in [1, 2, 3, 4, 5])
print(my_nums)

for num in my_nums:
    print(num)



