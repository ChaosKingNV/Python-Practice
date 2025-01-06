def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_belzabar_number(num):
    if num <= 0:
        return False

    for n in range(2, num // 2 + 1):
        if is_prime(n) and (num == n * (n + 20) or num == n * (n - 20)):
            return True

    return False

# Test cases
print(is_belzabar_number(125))  # True (5 * (5 + 20))
print(is_belzabar_number(189)) # True (21 * (21 - 20))
print(is_belzabar_number(25))  # False
print(is_belzabar_number(120)) # False
