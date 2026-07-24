def my_decorator(func):
    def wrapper():
        print("[Before] Something is happening before the function runs.")
        func()  # Execute the original function
        print("[After] Something is happening after the function runs.")

    return wrapper


# Standard syntactic sugar using the '@' symbol
@my_decorator
def say_hello():
    print("   Hello World!")


say_hello()
# Output:
# [Before] Something is happening before the function runs.
#    Hello World!
# [After] Something is happening after the function runs.





# decorator wih arg
from functools import wraps


def repeat(num_times):
    # This layer accepts the decorator's configurations
    def actual_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Run the targeted function as many times as requested
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return actual_decorator


@repeat(num_times=3)
def greet(name):
    print(f"Hi {name}!")


greet("Alex")
# Output:
# Hi Alex!
# Hi Alex!
# Hi Alex!