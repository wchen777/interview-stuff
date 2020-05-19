# check whether or not given integer is a prime

# O(n) naive solution
def primeNaive(num):
    def recMod(num, divisor):
        if divisor == 1:
            return True
        else: 
            return (num % divisor != 0) and recMod(num, divisor - 1)
    if 0 < num <= 1:
        return False
    else:
        return recMod(num, num - 1)
print("naive:")
print("1 " + str(primeNaive(1)))
print("2 " + str(primeNaive(2)))
print("5 " + str(primeNaive(5)))
print("6 " + str(primeNaive(6)))

# all primes are in the form 6n +- 1, and all numbers are made up of a product primes
def prime(num):
    if not(2 <= num <= 3) and (num % 2 == 0 or num % 3 == 0 or num == 1):
        return False
    else:
        n = 1
        while (6*n + 1 < num):
            if (num % (6*n - 1) == 0 or num % (6*n + 1) == 0):
                return False
            n += 1
        return True
print("efficient:")
print("1 " + str(prime(1)))
print("2 " + str(prime(2)))
print("5 " + str(prime(5)))
print("6 " + str(prime(6)))
print("11 " + str(prime(11)))
print("12 " + str(prime(12)))
print("13 " + str(prime(13)))
print("15 " + str(prime(15)))

def printPrimes(primesUntil):
    print("primes until " + str(primesUntil) + ": ")
    for i in range(primesUntil):
        if prime(i):
            print(str(i) + " ")

printPrimes(100)