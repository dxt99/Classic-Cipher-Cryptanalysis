import string

f = open("cipher/substitution.enc", "r")
ct = f.read().strip()
ct = "".join(ct.split("\n"))
f.close()

def write_file(iteration, buffer):
    f = open(f"plaintext/substitution/iteration_{iteration}.flag", "w+")
    f.write(buffer)
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

def freq_count(ciphertext, seq_len = 1):
    freq = {}
    for i in range(0, len(ciphertext)-seq_len+1):
        key = ciphertext[i:i+seq_len]
        if key in freq:
            freq[key] += 1
        else:
            freq[key] = 1
    freq = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True)[:10])
    return freq

# calculate single letter frequency
print("Single letters:")
print(freq_count(ct, 1))
print("Bigrams:")
print(freq_count(ct, 2))
print("Trigrams:")
print(freq_count(ct, 3))
# try simple decryption
key = {"W":"e", "C":"t", "Z":"h", "N":"i", "P":"g", "J":"n", "F":"a", "Y":"d"}
write_file(1, substitute(ct, key))
# more infers from trigrams and partial decryption
key.update({"K":"r", "X":"o"})
write_file(2, substitute(ct, key))
# more infers
key.update({"Q":"w", "H":"u", "V":"l"})
write_file(3, substitute(ct, key))

key.update({"L":"s", "U":"v", "V":"l", "O":"b", "R":'y', "E":"m", "S":"k", "A":'c'})
write_file(4, substitute(ct, key))

key.update({"B":'f', "G":"p", "I":'x', "D":"z", "M":"j", "T":"q"})

write_file(5, substitute(ct, key))