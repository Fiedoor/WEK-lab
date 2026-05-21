### Diffie-Helman

dane: g, p, a, b

$$
A=g^a(modp)
$$

$$
B=g^b(modp)
$$

$$
K=A^b(modp)
$$

$$
K=B^a(modp)
$$

### RSA

**Dane:** p, q, m (wiadomość)

**Obliczenie wartości:**

p i q pierwsze

n = p * q

Φ (n) = (p-1) * (q-1)

e to wartość z przedziału (1, Φ (n) ) względnie pierwsza z Φ (n)

e * d ≡ 1 mod Φ(n)
Wartości publiczne: (n,e)

Wartości prywatne: (d)

**Szyfrowanie:**

$$
c=m^emod(n)
$$

**Deszyfrowanie:**

$$
m=c^dmod(n)
$$

### ElGalman

Dane: p, g, x (klucz prywatny z przedziału (1,p-1)), m (wiadomość)

$$
y=g^xmod(p)
$$

Publiczne: (g, y, p)

Prywatne: (x)

**Szyfrowanie:**

k to losowa wartość od 1 do p-1

$$
c_1=g^kmod(p)
$$

$$
c_2=m*y^kmod(p)
$$

**Deszyfrowanie:**

$$
s=c_1^xmod(p)
$$

$$
s^{-1}mod(p)
$$

$$
m=c_2 * s^{-1}mod(p)
$$


