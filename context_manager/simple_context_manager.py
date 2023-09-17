class HelloContextManager:
    def __enter__(self):
        print("Entering the context")
        return "Hello world!"

    def __exit__(self, exc_type, exc_value, exc_tb):
        print("Leaving the context")

        # Handle IndexError here
        if isinstance(exc_value, IndexError):
            print(f"An exception occured in your with block: {exc_type}")
            print(f"Exception message: {exc_value}")
            return True

        return False


with HelloContextManager() as word:
    print(word)
    print(word[100])
    