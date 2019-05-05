
class MyRange:

    def __init__(self, start, end):
        self.value = start
        self.end = end

    # This must be implemented for class to be iterable
    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current

nums = MyRange(1,10)


# # Gerenator iterable: same thing as the range class above
# def my_range(start):
#     current = start
#     while True:
#         yield current
#         current += 1
#
#
# nums = my_range(1, 10)

for num in nums:
    print(num)