import string

f = open("cipher/substitution.enc", "r")
ct = f.read().strip()
ct = "".join(ct.split("\n"))
f.close()

charset = string.ascii_uppercase
freq = dict.fromkeys(list(charset), 0)
for c in ct:
    if c in charset:
        freq[c] += 1
freq = dict(sorted(freq.items(), key = lambda x: x[1], reverse = True))
print(freq)