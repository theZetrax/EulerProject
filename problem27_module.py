from tqdm import tqdm

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
    a, b, n = 0, 0, 0
    for a in tqdm(range(int((-1 * LIMIT)), int(LIMIT)), desc="Working on Solution: "):
        for b in range((-1 * LIMIT), LIMIT + 1):
            global largest_prime_generator
            global largest_prime_record            
            n = 0
            while True:
                if n > largest_prime_record:
                    largest_prime_record = n
                    largest_prime_generator = a, b
                result = formula(n, a, b)
                isPrime = checkPrime(result)
                if not (isPrime):
                    break
                n = n + 1

    print("a, b, number of primes: %d, %d, %d" % (largest_prime_generator[0], largest_prime_generator[1], largest_prime_record))

def solve_out():
    a, b, n = 0, 0, 0
    for a in tqdm(range(int((-1 * LIMIT)), int(LIMIT)), desc="Working on Solution: "):
        for b in range((-1 * LIMIT), LIMIT + 1):
            global largest_prime_generator
            global largest_prime_record            
            n = 0
            while True:
                if n > largest_prime_record:
                    largest_prime_record = n
                    largest_prime_generator = a, b
                result = formula(n, a, b)
                isPrime = checkPrime(result)
                if not (isPrime):
                    break
                n = n + 1
    out = '''Behold the highest consequetive prime maker\na, b: %d, %d\nconseqetive primes: %d\ncoeffecient product: %d \ndone''' % (largest_prime_generator[0], largest_prime_generator[1], largest_prime_record, (largest_prime_generator[0] * largest_prime_generator[1]))
    
    return out
