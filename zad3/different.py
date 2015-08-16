string = "g65 fmnc wms3443 bgb4lr 6rp5ylq7jyr5c8 5g78r z6w f05ylb."

output = ''
for char in string:
    if not char.isdigit():
        newChar = chr(ord(char) + 2)
        output += newChar

print output
