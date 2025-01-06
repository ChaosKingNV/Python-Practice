def is_belzabar_number(n):

  if not isinstance(n, int) or n < 1:
    return False

  def is_prime(n):
    if n <= 1:
      return False

    for i in range(2, n):
      if n % i == 0:
        return False

    return True

  return (is_prime(n) and (n * (n + 20) == n ** 2 + 20 * n) or
          is_prime(n) and (n * (n - 20) == n ** 2 - 20 * n))
  
print(is_belzabar_number(125))  # True (5 * (5 + 20))
print(is_belzabar_number(504)) # True (22 * (22 - 20))
print(is_belzabar_number(25))  # False
print(is_belzabar_number(120)) # False