def a_highest_prime_factor(num):
    result = 0

    #basis
    if num % 2 == 0:
        while num % 2 == 0:
            num /= 2
            num = int(num)
            result = num
        return result

def highest_prime_factor(n):
    prime_factor = 1
    i = 2

    while i <= n/i:
        if n % i == 0:
            prime_factor = i
            n /= i
        else: 
            i += 1
    
    if prime_factor < n:
        prime_factor = n
    
    return prime_factor