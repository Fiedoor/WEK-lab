### Podpis RSA

generowanie kluczy standardowe

Nadawca (ma n,e,d) :

1.   h = H ( m )

2.    s = h^d mod n

3. Wysyła klucze publiczne, s i m

Odbiorca (ma n,e), dostaje m,s :

1. h = H (m)

2. h' = s^e mod n

3. jeśli h = h' podpis jest zgodny

### Podpis ElGamala

generowanie kluczy bez zmian

Nadawca (ma p,g,x) generuje k:

1. h = H(m)

2. r = g^k mod n

3. s = ( h - x * r) * k^-1 mod p-1

4. wysyła m, r,s (wiadomość i 2 części podpisu)

Odbiorca dostaje m , r , s, ma wartości publiczne g,p,y

1. Sprawdza czy 0 < r < p jeśli nie odrzuca podpis

2. h = H(m)

3. sprawdza czy y^r *r^s == g^k mod p

### Podpis DSA

Nadawca ma p, q (dzielnik p-1), g , x losuje k

1. h = H(m)

2. r = (g^k mod p ) mod q

3. s = k^-1 (h + x*r) mod q

Odbiorca ma p,q,g, y, dostaje r,s,m

1. Sprawdza czy 0 < r < q oraz 0 < s < q jeśli nie odrzuca podpis

2. h = H(m)

3. w = s^-1 mod q

4. u1 = h * w mod q

5. u2 = r * w mod q

6. v = ((g^u1 * y^u2) mod p) mod q

7. jeśli v = r akceptuje podpis


