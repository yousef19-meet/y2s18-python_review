## Y2 2018 Summer: Python Review Lab

Welcome to the Python review lab! Please read all the instructions so you don't
get lost halfway through, but definitely feel free to ask for help if you
get stuck. Good luck, and have fun!

### Part 0: Setup

1. Before you start coding, make sure you clone the repository for this lab:
```
cd ~/Desktop
https://github.com/meet-projects/y2s18-python_review
cd y2s18-python_review
subl lab &
```

### PART 1: Basic functions

The stubs for these functions can be found in `part1.py`.

1. Write a function to `hello_world`, which takes in no inputs
and prints "hello world". 

2. Write a function `greet_by_name` which takes in a string, `name`,
and prints "hello <name>"

3. Write a function, `encode`, that takes in a number, `x` and computes
the product of `x` and 3953531.
This function shouldn't print anything, but should return an integer value.

4. Write a function, `decode`, which takes in the output from the previous function and
finds `x`. You may use the value 3953531 in this function.

### PART 2: Loops

The stubs for these functions can be found in `part2.py`.

1. First, update your function `encode`, to take in 2 numbers `x` and `y`, and compute their product.
This function should require `y < 250`. If this isn't true, the function should print "Invalid input",
and return None.

2. Write a function, `decode`, which takes in the output from your updated `encode` function
and tries to compute `x`. This function does not know the value of `y`
Hint: Consider trying all possible values for `y`!

### PART 3: Classes

The stubs for these functions can be found in `part3.py`.

The `encode` and `decode` functions that you've constructed before are the basics of cryptography, the science
of creating and breaking codes. Now, to make things trickier, we want to create a class of codes.

1. Start by creating a class, `Cipher`, which has the following attributes, when
initialized:
- `secret_message`: a number we're trying to hide (the access code to the treasure..)
- `key`: the number we're using to hide our message (the number we multiply by!)
- `key_limit`: the maximum value that the key can have

2. Add a function `encode`, which multiplies the `secret_message` by the `key`
to get the coded message. Now, instead of printing the coded message,
add it as a new attribute in the class!

3. Now, add the `decode` function, which checks all values up to `key_limit`
to find the key and decode the `coded_message`. We can see how secure
our system is by checking how long it takes us to decode!

4. Play around with the attributes to make the decode function more secure. Is there any attribute
that you can change to make our message more secure?

5. Write a new encode function, which does anything you want with
the key and the secret_message. Write the corresponding decode function, as
well. To be correct, we expect the decode function to always return the
correct secret_message. To be secure, we want the decode function to beslow!
Can you create a slow function, with a `key_limit` of 1000? How slow?

### PART 4: Bonus
Instead of initializing the class with a key, update the class
so it's just initialized with the `secret_message` and `key_limit`.
Then, write a function to randomly choose a key value within the range [0, key_limit]. This function should be called immediately after initialization and update the key attribute of your class.
Hint: Consider using the `random` module, in Python for this!