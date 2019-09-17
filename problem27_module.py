from tqdm import tqdm

problem_name = "Quadratic primes"

problem_definition = '''Euler discovered the remarkable quadratic formula: 
    n2+n+41
It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39. However, when n=40,402+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,412+41+41 is clearly divisible by 41.

The incredible formula n2−79n+1601 was discovered, which produces 80 primes for the consecutive values 0≤n≤79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form: n2+an+b, where |a|<1000 and |b|≤1000

where |n| is the modulus/absolute value of n
        e.g. |11|=11 and |−4|=4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.'''

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

    print("a, b, number of primes: %d, %d, %d" % (largest_prime_generator[0], largest_prime_generator[1], largest_prime_record))

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
    out = '''Behold the highest consequetive prime maker\na, b: %d, %d\nconseqetive primes: %d\ncoeffecient product: %d \ndone''' % (largest_prime_generator[0], largest_prime_generator[1], largest_prime_record, (largest_prime_generator[0] * largest_prime_generator[1]))
    
    return out
