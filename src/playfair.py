import string

f = open("cipher/playfair.enc", "r")
ct = f.read().strip()
ct = "".join(ct.split("\n"))
f.close()

def freq_count(ciphertext, seq_len = 2):
    freq = {}
    for i in range(0, len(ciphertext)-seq_len+1):
        key = ciphertext[i:i+seq_len]
        if key in freq:
            freq[key] += 1
        else:
            freq[key] = 1
    freq = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True)[:30])
    return freq

print(freq_count(ct))