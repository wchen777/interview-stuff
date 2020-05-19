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

print("1" + str(primeNaive(1)))
print("2" + str(primeNaive(2)))
print("5" + str(primeNaive(5)))
print("6" + str(primeNaive(6)))