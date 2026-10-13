# Define a decorator function
def decorator(func):
    # Wrapper function that adds extra functionality
    def wrapper():
        # Code executed before the original function
        print("Starting function")

        # Call the original function
        func()

        # Code executed after the original function
        print("Function completed")

    # Return the wrapper function (do not call it here)
    return wrapper


# Apply the decorator to the welcome() function
@decorator
def welcome():
    """Display a welcome message."""
    print("Welcome to Python")


# Call the decorated function
welcome()