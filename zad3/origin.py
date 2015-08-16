string = "g65 fmnc wms3443 bgb4lr 6rp5ylq7jyr5c8 5g78r z6w f05ylb."

print ''.join([chr(ord(ch) + 2) for ch in string if not ch.isdigit()])
