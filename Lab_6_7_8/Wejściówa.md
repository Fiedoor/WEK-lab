### Długości klucza i ilość rund:

- 128 bit - 10 rund

- 192 bit - 12 rund

- 256 bit - 14 rund

### Początkowe kroki przed rundami:

1. Podział wiadomości na bloki 128 bitów

2. Dopełnienie ostatniego bloku (padding)

3. Inicjalizacja macierzy 4x4 z bloku

4. Ekspansja klucza (utworzenie kluczy rund)

### Co wchodzi w skład jednej rundy:

1. Podstawienie bajtów - wykonanie defacto szyfru podstawieniowego na bajtach wiadomości (np bajt 1 traktujemy jako 99, 2 jako 43 itp.)

2. Przesunięcie cykliczne wierszy w lewo (każdy wiersz jest przesuwany o konkretną liczbę bajtów)

3. Mieszanie kolumn poprzez mnożenie każdej z kolumn przez z góry określoną macierz

4. XOR całej macierzy z kluczem rundy

### Typy paddingu

PKCS#7 - każdy bajt jest wypełniony liczbą bajtów brakujących (np jeśli brakuje 5 bajtów jest 05 05 05 05 05)

Zero - dopełnienie zerami

ISO/IEC 7816-4 (bit padding) - zera i na końcu bit o wartości 1

ANSI - zera i na końcu długość dopełnienia tak jak w PKCS#7

### Tryby szyfrowania

ECB - każdy blok jest szyfrowany niezależnie

    Zalety: 

    Wady:

CBC (cipher blok chaining) - każdy blok przed szyfrowaniem jest XOR'owany z szyfrogramem poprzedniego (dla pierwszego wykorzystujemy wektor inicjalizujący)

    Zalety:

    Wady:

PCBC - ewolucja CBC, blok tekstu jest xorowany z szyfrogramem po czym jak w CBC 

    Zalety:

    Wady:

CFB - szyfrowany jest klucz z poprzednim szyfrogramem (dla pierwszego wektor) po czym XOR z tekstem jawnym

    Zalety:

    Wady:

OFB - poprzedni jest szyfrowany z kluczem output trafia do następnego, szyfrogram bloku powstaje jeszcze przez XOR

    Zalety:

    Wady:

CTR - klucz jest szyfrowany z sumą jednorazowego numeru i licznika, to co powstanie jest xorowane z tekstem jawnym, tak dla każdego bloku 

    Zalety:

    Wady:

# Schematy szyfrowania


