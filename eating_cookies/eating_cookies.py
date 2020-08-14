'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n, cache = {}):

    if n == 0:
        return 1

    if n < 0:
        return 0

    if n in cache.keys():
        return cache[n]

    value = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
    cache[n] = value
    return value

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
