i = 0
numbers_dict = {}

for n in xrange(1, 100):
    numbers_dict.update({
        i: n,
    })

    i += 1
    print numbers_dict

    even_numbers = []
    for k, v in numbers_dict.items():
        if v % 2 == 0:
            even_numbers.append(v)
        else:
            pass

    print "Ilosc liczb parzystych: " + str(even_numbers.__len__())

    try:
        size = even_numbers.size
    except Exception:
        size = None

    print "Size = " + str(size)
