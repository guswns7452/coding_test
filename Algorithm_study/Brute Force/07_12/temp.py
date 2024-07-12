import time
def combination(n, k, memo={}):
    # Base cases
    if k == 0 or k == n:
        return 1
    # Check if result is already in memo
    if (n, k) in memo:
        return memo[(n, k)]
    # Recursive step with memoization
    result = combination(n-1, k-1, memo) + combination(n-1, k, memo)
    memo[(n, k)] = result
    return result

start = time.time()
# Calculate the number of combinations of 100 choose 5
result = combination(100, 5)
print(result)

end = time.time()-start
print(f"time : {time.time()-start}")