## Y2 2018 Summer: Python Review Lab

Welcome to the Python review lab! Please read all the instructions so you don't
get lost halfway through, but definitely feel free to ask for help if you
get stuck. Good luck, and have fun!

### Part 1: Basic functions

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

5. Test your `encode` and `decode` functions to make sure that they work. To do this, try to run `decode(encode(x))` and make sure you get your original value of `x`!

### Part 2: Loops

The stubs for these functions can be found in `part2.py`.

1. First, update your function `encode`, to take in 2 numbers `x` and `y`, and compute their product.
This function should require `1 < y < 250` and `500 < x < 1,000`. If this isn't true, the function should print
`Invalid input: Outside range.`, and return None.

2. Update your encode function to guarantee that the inputs `x` and `y` are prime. If `x` is not prime,
then keep incrementing the value of `x` until it is prime; then, do the same process for `y`. If this
causes the new values of `x` and `y` to be out of the range, print `Invalid input: Outside range.`,
and return None.  
*Hint: Have we implemented any functions previously, which could be useful here?*

3. Write a function, `decode`, which takes in the output (the value of the product)
from your updated `encode` function and tries to compute values for `x` and `y`.
This function only takes in, as input,
the `coded_message`, which is output from `encode`. You may also use the ranges of possible values for `x` and `y` - that is, `1 < y < 250` and `500 < x < 1,000`.
Consider trying all possible values for `x` and `y`!
*Hint: The mod function might be useful here! The mod function can be used to calculate the remainder.
For instance, `500 % 6` returns the remainder when 500 is divided by 6.*

4. Test your `encode` and `decode` functions to
make sure they work. Note that the `encode` function changes your input to make sure that it's prime. Thus, if your original input was not prime, `decode(encode(x, y))`, might not return
the original values of `x` and `y`. So, in `encode`, add a print statement, to print the values of `x` and `y` after the incrementing is finished. These values, `x'` and `y'` should be returned when `decode(encode(x, y))` is run.

### Part 3: Classes

The stubs for these functions can be found in `part3.py`.

The `encode` and `decode` functions that you've constructed before are the basics of cryptography, the science
of creating and breaking codes. Now, to make things trickier, we want to create a class of codes.

1. Start by creating a class, `Cipher`, which has the following attributes, when
initialized:
- `secret_message`: a number we're trying to hide (the access code to the treasure..)
- `key`: the number we're using to hide our message (the number we multiply by!)
- `limit`: An integer representing the maximum value that the key or message can have. We assume
that all keys and messages must be non-negative.
Example: 1000

2. When initializing, make sure that both the `key` and `secret_message` values are greater than 1.
If they are, print `Invalid input: Keys and messages must be greater than one.` Similarly, make sure that
both the `key` and `secret_message` values are prime. If they are not, print `Invalid input: Both key
and message must be prime.`

3. Instead of initializing the Cipher class with explicit key and message limits, provide a
default value for the `limit` attribute of 10,000. If the key or the secret_message violates the limit,
then return `Invalid input: Keys and messages must be at most the limit, which is <LIMIT>.`

4. Add a function `encode`, which multiplies the `secret_message` by the `key`
to get the coded message. Now, instead of printing the coded message,
add it as a new attribute in the class!

5. Now, create a new class `Decoder`, which has the following attributes, when 
initialized:
- `coded_message`: the product of two large prime numbers
- `limit`: the maximum value that the key or message can have.

6. Now, add a `decode` function, to this class, to decode the `coded_message`. 
We can see how secure our system is by checking how long it takes us to decode! This function
should return a tuple of the form `(key, secret_message)`.
*Note: Order isn't important here. The tuples (5, 135) and (135, 5) are the same
thing*

7. Finally, test that your functions are working properly, by choosing a `secret_message` and a `key`.
One possible example is a `secret_message` of 4261 and a `key` of 1237.
Then, use the Cipher class to encode your message.
Use the coded_message and limit
from the Cipher class to create a Decoder class. Then, run the decode function to guarantee
that we can recover the original secret message and key (though the order might be flipped!).

8. Instead of initializing the Cipher class with a key, update the class
so it's just initialized with the `secret_message`. Then, write a function to randomly choose a
key value within the range `1 < key < limit`. This function should be called immediately after initialization and update the key attribute of your class. Note that this function should repeatedly choose a random value, until a value
which is prime is chosen.
Hint: Consider using the `random` module, in Python for this!

### Part 4: Vigenere Ciphers

The previous sections detailed how to make very basic ciphers, which just rely on the idea that, given
the product of two large prime numbers, finding the numbers themselves is difficult. However, this
required our secret messages to be prime numbers. In this section, we'll use a different cipher
to encode actual messages.

The stubs for these functions can be found in `part4.py`. 

1. Implement a function `transform_message_to_numbers`, which transforms an input, `secret_message`,
by mapping each letter to its index in the alphabet. That is, the message `abc` should be mapped to `[0,1,2]`, 
since `a` is the first letter, `b` is the second letter, etc. Note the use of zero-indexing here, since `a`
maps to 0. We would expect `z` to map to 25. The output of this function should be a comma-separated
list of integers.

2. Implement a function `transform_numbers_to_message`, which transforms a list of numbers back
to the original message. That is, a list of the form `[0, 1, 2]` should map to the string `abc`.
*Hint: First, transform `[0, 1, 2]` into `['a', 'b', 'c']`. Then, figure out how to combine an array `['a', 'b', 'c']` into `abc`, using the functions in the String class.

3. Initialize a class `VigenereCipher`, which is initialized with a string `secret_message` and an integer
value `shift`.

4. Make sure that the `shift` value is in the range `0 <= shift <= 25`. If not, print out `Invalid shift value: Outside range.`


5. Implement a function `encode`, which takes the `secret_message` and converts it into a list of numbers.
Then, we should increment each number in the list by the `shift` attribute. Finally, we can take
the new list of numbers and convert it back to a message. This function should use the previous functions
that you have already implemented.

This function should return `None`, however,
we should add the value of the final coded message, as the
`coded_message` attribute in our class.

*Note: Sometimes you might run into issues with shifting. For instance, consider a message `a`, which is
shifted by -1. If encode works properly, `a` will map to [0]. After the shift, the list will contain [-1].
However, -1 doesn't map to anything in the alphabet. However, we note that the cipher is circular - in this
case, we actually want `a` to map to `z`. Make sure you understand why this is true! An easy way to deal with
this is to take each element in the shifted list and calculate its value mod 26. Since -1 mod 26 is 25, this
will correctly get us a mapping of `z`.*

6. Initialize a class `VigenereDecoder`, which is initialized with a string `coded_message`.

7. Implement a function `decode`, which tries as input a `coded_message`, tries all possible shift values,
and prints all possible decoded_messages. You'll have to read through this output to figure out what
the original secret message was. This function
should return `None`.

8. Try out your `encode` function and send your friend a coded_message. You should receive one from them, in
return. Use your `decode` function to figure out what they're telling you!
