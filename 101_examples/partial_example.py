from functools import partial


# A function that needs TWO things.
def greet(greeting, name):
    print(greeting, name)


# 1. Normal call: you give both things now.
greet("Hello", "Ana")

# 2. partial: give the first thing now. Nothing is printed yet.
say_hi = partial(greet, "Hi")

# 3. Later, give only the missing thing. Now it prints.
say_hi("Ana")
say_hi("Bob")

# 4. partial with the name instead. "name=" says which one you are giving.
greet_ana = partial(greet, name="Ana")

# 5. Later, give only the greeting.
greet_ana("Hi")
greet_ana("Hello")
