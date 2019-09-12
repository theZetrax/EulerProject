LIMIT = 1000

def checkPrime(num):
    # prime numbers are greater than 1
    if num > 1:
       # check for factors
       for i in range(2,num - 1):
           if (num % i) == 0:
               return False
       return True
    # if input number is less than
    # or equal to 1, it is not prime
    else:
       return False

def formula(n, a, b):
	return (n**2) + (a*n) + b

largest_prime_generator = (0, 0)
largest_prime_record = 0

def solve():
    for a in range(1, LIMIT):
        for b in range(1, LIMIT + 1):
            n = 0
            while True:
                result = formula(n, a, b)
                isPrime = checkPrime(result)
                if not (isPrime):
                    print("a, b, n: %d, %d, %d prime: %r" % (a, b, n, isPrime))
                    break
                n = n + 1
                print("a, b, n: %d, %d, %d prime: %r" % (a, b, n, isPrime))

    print("Done")
