# Class Methods & Static Methods:
# Build a User class.

# 1. Track the active_users_count at the class level, not the instance level. Increment it when a user is created.

# 2. Write a @staticmethod called is_valid_password(password) that returns True only if the password is at least 8 characters long and contains a number.

# 3. Write a @classmethod called from_csv_string(cls, csv_string) that acts as an alternative constructor. It should take a string like "Navneet,navneet@email.com,Pass1234" and return a new User object.


class User:
    active_users_count = 0

    def __init__(self,name,email,password):
        self.name = name
        self.password = password
        self.email = email
        User.active_users_count += 1

    @staticmethod
    def is_valid_password(password):
        return len(password) >= 8 and any(char.isdigit() for char in password)

    @classmethod
    def from_csv_string(cls, csv_string):
        name, email, password = csv_string.split(",")
        return cls(name, email, password)

user1 = User("Alice", "alice@email.com", "Password1")
user2 = User.from_csv_string("Navneet,navneet@email.com,Pass1234")

print(user1.name)
print(user2.email)

print(User.is_valid_password("Pass1234"))  # True
print(User.is_valid_password("password"))  # False

print(User.active_users_count)



