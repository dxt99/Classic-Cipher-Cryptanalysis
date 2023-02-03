import string

f = open("cipher/playfair.enc", "r")
ct = f.read().strip()
ct = "".join(ct.split("\n"))
f.close()

def write_file(iteration, buffer):
    f = open(f"plaintext/playfair/iteration_{iteration}.flag", "w+")
    f.write(buffer)
    f.close()

def substitute(ciphertext, dictionary):
    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        c = ciphertext[i: i+2]
        if c in dictionary:
            plaintext += dictionary[c]
        else:
            plaintext += c
    return plaintext

def freq_count(ciphertext, seq_len = 1):
    unit_size = 2
    freq = {}
    for i in range(0, len(ciphertext)-seq_len+1, unit_size):
        key = ciphertext[i:i+unit_size*seq_len]
        if key in freq:
            freq[key] += 1
        else:
            freq[key] = 1
    freq = (sorted(freq.items(), key=lambda x: x[1], reverse=True)[:50])
    return freq
print(len(ct))
print(freq_count(ct))
print(freq_count(ct, 2))
print("----------------------------")
freq = (freq_count(ct))

f = open("data/english_bigrams.txt", "r")
data = f.readlines()
f.close()

key = {}
for i in range(20):
    line = data[i].strip().split()
    key[freq[i][0]] = line[0].lower()

print(key)

write_file(0, substitute(ct, key))
