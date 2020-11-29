Highest Prime Factor Research

What is a Prime Factor?
    A prime factor is a factor that is a prime number.
    In other words, any of the prime numbers that can be multiplied to give the original number.
    Example: The prime factors of 15 are 3 and 5 because 3 multipled by 5 is 15 and 3 and 5 are prime numbers.

What is a Prime Number?
    A whole number greater than 1 that can not be made by multiplying other whole numbers.
    Example: 5 is a prime number because we cannot multiple 2, 3, or 5 together to make 5.

What is a Composite Number?
    A whole number greater than 1 that can be made by multiplying other whole numbers. The opposite of a prime number.
    Example: 6 is a composite number because 2 multipled by 3 equals 6.

All whole numbers are either composite or prime.

List of all prime numbers: 
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101


to check if a number is prime or not:

if num > 1:
    for i in range(2, num):
        if (num % i ) == 0:
            print(num, "is not a prime number")
            break
        else:
            print(num, "is a prime number")
else:
    print(num, "is not a prime number")


If we wish to find the largest prime factor, perhaps we can try iterating this function thru to find the prime numbers, and maybe set up a 0 value variable that updates whenever a higher factor is found.

Factor Trees

    52          2x2x13
    /\
   2  26
      /\
     2  13

    96          2x2x2x2x2x3
    /\
   2  48
      /\
     2  24
        /\
       2  12
          /\
         2  6
            /\
           2  3

result = 0
while num / 2 != 0:
    num /= 2
    result = num


I have a basis code setup that will allow me to factor down all the way to 2. However I have noted that there needs to be a way to find higher factors, like 5 mainly. I need to find a way to go thru factorials and see which one will return the highest prime factor. Some way in which I can first test the program and find out which prime factor will yield the highest result.