numbers_dict = {}
even_numbers = []

for i in xrange(99):
    numbers_dict.update({
        i: i+1,
    })

    if numbers_dict[i] % 2 == 0:
        even_numbers.append(numbers_dict[i])

    print numbers_dict
    print "Ilosc liczb parzystych: %d" % len(even_numbers)
    print "Size = None"
