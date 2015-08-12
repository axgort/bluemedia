even_numbers_count = 0

for n in xrange(1, 100):
    if n % 2 == 0:
        even_numbers_count += 1

    msg = "Ilosc liczb parzystych w przedziale <1,%d>: %d"
    print msg % (n, even_numbers_count)
