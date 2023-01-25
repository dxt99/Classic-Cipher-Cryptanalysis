import string

f = open("cipher/substitution.enc", "r")
ct = f.read().strip()
ct = "".join(ct.split("\n"))
f.close()

def substitute(ciphertext, dictionary):
    plaintext = ""
    for c in ciphertext:
        if c in dictionary:
            plaintext += dictionary[c]
        else:
            plaintext += c
    return plaintext

charset = string.ascii_uppercase

# calculate single letter frequency
freq = dict.fromkeys(list(charset), 0)
for c in ct:
    freq[c] += 1
freq = dict(sorted(freq.items(), key = lambda x: x[1], reverse = True))
print(freq)

# calculate bigrams frequenct
# TODO
