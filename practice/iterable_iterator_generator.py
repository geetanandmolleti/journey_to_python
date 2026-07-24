# iterable
numbers = [10, 20, 30]  # This is an ITERABLE

# ❌ You cannot call next() on an iterable directly!
# next(numbers)
# TypeError: 'list' object is not an iterator

#  You must convert it into an ITERATOR first
engine = iter(numbers)
print(next(engine))  # Output: 10
print(next(engine))  # Output: 20







class StepCounter:
    """An iterable that counts up by a specific step size."""

    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        # Using 'yield' automatically makes this return an iterator object
        current = self.start
        while current < self.stop:
            yield current
            current += self.step


# Using our custom iterable
counting_by_tens = StepCounter(start=0, stop=31, step=10)

for num in counting_by_tens:
    print(num)
# Output:
# 0
# 10
# 20
# 30
























# iterator
fruits = ["apple", "banana"]
fruit_iterator = iter(fruits)  # Create an iterator

# Consume the entire iterator
print(list(fruit_iterator))  # Output: ['apple', 'banana']

# Try to look at it again
print(list(fruit_iterator))  # Output: []  (It's completely exhausted!)







class SquareIterator:
    """An iterator that generates squares up to a maximum number."""
    def __init__(self, max_limit):
        self.max_limit = max_limit
        self.current = 1

    def __iter__(self):
        return self  # The protocol requires an iterator to return itself

    def __next__(self):
        if self.current > self.max_limit:
            raise StopIteration  # Signal that we are out of items
        
        result = self.current ** 2
        self.current += 1
        return result

# Using the custom iterator
squares = SquareIterator(3)

print(next(squares))  # Output: 1
print(next(squares))  # Output: 4
print(next(squares))  # Output: 9
# next(squares)      # This would raise StopIteration

























# generator 
def simple_generator():
    print("Starting...")
    yield "First Stop"

    print("Resuming...")
    yield "Second Stop"

    print("Ending...")


# 1. Get the generator object
gen = simple_generator()

# 2. Step through it manually
print(next(gen))
# Prints: Starting...
# Output: First Stop

print(next(gen))
# Prints: Resuming...
# Output: Second Stop

# next(gen) -> Prints: Ending... then raises StopIteration











# note case 
def infinite_even_numbers():
    num = 0
    while True:
        yield num
        num += 2


evens = infinite_even_numbers()

print(next(evens))  # Output: 0
print(next(evens))  # Output: 2
print(next(evens))  # Output: 4
# We can do this forever without a MemoryError.