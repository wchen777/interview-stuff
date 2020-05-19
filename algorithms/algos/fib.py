# DP fibonacci w/ O(n) time and O(1) space
def fib(num):
    if num == 0:
        return 0
    elif num == 1:
            return 1
    else:
        memo = [0, 1]
        for _ in range(2, num + 1):
            before = memo[0]
            top = memo[1]
            memo[1] = before + top
            memo[0] = top 
        return memo[1]

print(fib(2)) # 0 + 1 = 1
print(fib(3)) # 1 + 1 = 2
print(fib(4)) # 1 + 2 = 3
print(fib(5)) # 2 + 3 = 5
print(fib(6)) # 3 + 5 = 8
print(fib(7)) # 5 + 8 = 13