#Challenge #44: FizzBuzz

'''
Write a program that prints the numbers from 1 to 100. 
For multiples of three print "Fizz" instead of the number.
For multiples of five print "Buzz" instead of the number.
For multiples of three & five print "FizzBuzz" instead of the number.
'''

def FizzBuzz(num): # First implementation tested working
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0: 
        return "Fizz"
    elif num % 5 == 0: 
        return "Buzz"
    else:
        return num

def improve_FizzBuzz(num): # Are these really better in fixing repetition?
    fizz = num % 3 == 0
    buzz = num % 5 == 0
    if fizz and buzz: 
        return "FizzBuzz"
    if fizz:
        return "Fizz"
    if buzz:
        return "Buzz"
    else:
        return num

def even_better_FizzBuzz(num): # Is this really better? I feel like it doesn't fix much repetition
    FIZZ = 'Fizz'
    BUZZ = 'Buzz'

    fizz = num % 3 == 0
    buzz = num % 5 == 0

    if fizz and buzz: 
        return FIZZ + BUZZ
    elif fizz:
        return FIZZ
    elif buzz: 
        return BUZZ
    else: 
        return num
