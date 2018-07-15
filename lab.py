## PART 1: Basic functions ##

# Write a function to print
# hello world

# Write a function greet_by_name
# which takes in a string, name 
# and prints "hello <name>"

# Write a function, encode, that takes in a number
# x and computes the product of x and 3953531
# This function shouldn't print anything, but
# should return an integer value.

# Write a function, decode, which takes in
# the output from the previous function and
# finds x

## PART 2: Loops ##

# First, update your function encode, to take in
# 2 numbers x and y, and compute their product. This
# function should require y < 250. If this isn't true,
# the function should print "Invalid input"

# Write a function, decode, which takes in the output 
# from your updated encode and tries to compute x. This
# function does not know the value of y

# Hint: Consider trying all possible values for y!

## PART 3: Classes ##

# The encode and decode functions that you've constructed
# before are the basics of cryptography, the science
# of creating and breaking codes. Now, to make things trickier,
# we want to create a class of codes.

# Start by creating a class, which has the following attributes, when
# initialized:
# - secret_message: a number we're trying to hide (the access code to the treasure..)
# - key: the number we're using to hide our message (the number we multiply by!)
# - key_limit: the maximum value that the key can have

# Add a function encode, which multiplies the secret_message by the key
# to get the coded message. Now, instead of printing the coded message,
# add it as a new attribute in the class!

# Now, add the decode function, which checks all values up to key_limit
# to find the key and decode the coded_message. We can see how secure
# our system is by checking how long it takes us to decode!

# Play around with the attributes to make the decode function more
# secure.

# Write a new encode function, which does anything you want with
# the key and the secret_message. Write the corresponding decode function, as
# well. To be correct, we expect the decode function to always return the
# correct secret_message. To be secure, we want the decode function to be
# slow! Can you create a slow function, with a key_limit of 100?

## PART 4: Bonus ##

# Instead of initializing the class with a key, update the class
# so it's just initialized with the secret_message and the key_limit
# Then, write a function to randomly choose a key value within the 
# range [0, key_limit]. This function should be called immediately
# after initialization and update the key attribute of your class.