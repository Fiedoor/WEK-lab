def is_prime(n):
    """Sprawdza, czy liczba n jest pierwsza."""
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

def prime_factors(n):
    """Znajduje wszystkie unikalne czynniki pierwsze liczby n."""
    factors = set()
    while n % 2 == 0:
        factors.add(2)
        n //= 2
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.add(i)
            n //= i
    if n > 2:
        factors.add(n)
    return factors

def find_generators(p):
    """Znajduje wszystkie pierwiastki pierwotne (generatory) dla liczby pierwszej p."""
    if not is_prime(p):
        raise ValueError("Liczba p musi być pierwsza.")

    phi = p - 1  # phi(p) dla liczby pierwszej p to p-1
    factors = prime_factors(phi)

    def is_generator(g):
        for factor in factors:
            if pow(g, phi // factor, p) == 1:
                return False
        return True

    generators = []
    for g in range(2, p):
        if is_generator(g):
            # print(g)
            generators.append(g)
    return generators

# Przykład użycia
p = 197  # dowolna liczba pierwsza
generators = find_generators(p)
print(f"Generatory dla liczby pierwszej {p}: {generators}")
