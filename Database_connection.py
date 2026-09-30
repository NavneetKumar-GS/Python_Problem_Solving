# Context Managers (Dunder Methods)

# 1.Create a DatabaseConnection class.

# 2.Implement the __enter__ and __exit__ dunder methods so this class can be used in a with block.

# 3.__enter__ should print "Opening connection..." and return the object.

# 4.__exit__ should print "Closing connection...". It must also handle exceptions: if an error occurs inside the with block, catch it, print "Error logged: [error message]", and ensure the connection still closes without crashing the script.


class DatabaseConnection:

    def __enter__(self):
        print("Accessing database...")
        return self

    def __exit__(slef,exc_type,exc_val, exc_tb):
        print("Closing connection...")

        if exc_type is not None:
            print(f"Error logged: {exc_val}")

            return True


print("--- Scenario 1: Everything works ---")
with DatabaseConnection() as db:
    print("Executing SQL query...")

print("\n--- Scenario 2: A crash happens ---")
with DatabaseConnection() as db:
    print("Executing SQL query...")
    raise ValueError("Table 'users' not found!")

print("Script continues running normally because the crash was suppressed.")
