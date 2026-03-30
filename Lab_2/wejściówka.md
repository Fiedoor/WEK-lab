## Szyfr Cezara

### Sposób liczenia:

Każda litera z plaintextu jest przesunięta w alfabecie o x miejsc, dla każdej litery przesunięcie jest takie samo np. przy przesunięciu (kluczu) 2 A -> C itp.

### Przestrzeń klucza

Tyle ile liter w alfabecie

### Ataki

- Brute force - szyfr cezara jest łatwy do złamania siłowego, ponieważ mamy (dla alfabetu angielskiego) tylko 26 kluczy więc sprawdzenie wszystkich możliwości jest szybkie
- analiza częstościowa - polega na sprawdzeniu częstości występowania liter w szyfrogramie i dopasowaniu ich do liter najczęściej występujących w danym alfabecie i sprawdzeniu ile wynosi wartość przesunięcia

## Szyfr podstawieniowy monoalfabetyczny

### Sposób liczenia:

Wykonujemy permutację alfabetu i podpisujemy pod alfabet źródłowy, każda litera z tekstu jest zmieniana na literę o tym samym numerze po permutacji

przykład:

ABCDEFGHIJKLMNOPQRSTUVWXYZ		STANISLAW FIEDORUK
QRSTUVXZWCYABDEFGHIJKLMNOP		CDLXSCVLI PSONYBEU

### Przestrzeń klucza

N! gdzie n to ilość liter w alfabecie

### Ataki

- Analiza częstościowa - ponieważ permutacja jest jedna tak samo możemy przyporządkować litery najczęściej występujące w szyfrogramie do liter najczęściej występujących w alfabecie i odzyskać klucz
- Analiza n-gramów - w każdym języku występują krótkie, często występujące ciągi znaków (np. w angielskim THE, w polskim dwuznaki takie jak CZ, SZ itp.) znajdując je w tekście możemy dopasować odpowiadające im litery w kluczu

## Szyfr Vigenere'a

### Sposób liczenia:

Mamy tekst i słowo klucz, wartości liter w kluczu robią za przesunięcie jak w cezarze i każdą literę w tekście przesuwamy o wartość odpowiadającej litery w kluczu (jeśli klucz i tekst mają różne długości, to powielamy klucz lub go skracamy np. tekst 6 znaków a klucz 3 to piszemy klucz dwa razy).

### Przestrzeń klucza

N^L gdzie N to ilość liter w alfabecie a L to długość klucza

### Ataki

- rozbicie na szyfry cezara - jeśli znamy długosć klucza możemy użyć analizy częstościowej z podziałem na litery z tym samym przesunięciem np dla klucza 3 znakowego co 3 litera będzie miała to samo przesunięcie

## Szyfr przestawieniowy transpozycyjny

