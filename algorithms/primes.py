# check whether or not given integer is a prime

# O(n) naive solution
def primeNaive(num):
    def recMod(num, divisor):
        