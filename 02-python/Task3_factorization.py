def prime_factors(n):
    """
    Находит простые множители числа n.

    Временная сложность: O(N)
    Пространственная сложность: O(K), где K — количество простых множителей числа.
    """
    factors = []
    i = 2
    while n != 1:
        if n % i == 0:
            factors += [i]
            n //= i
        else:
            i += 1
    return(factors)