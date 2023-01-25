import string
import math

f = open("cipher/kasiski.enc", "r")
ct = f.read().strip()
ct = "".join(ct.split("\n"))
f.close()

charset = string.ascii_uppercase

def get_potential_key_length(ciphertext, seq_len):
    dist = []
    for i in range(len(ciphertext)-seq_len+1):
        pattern = ct[i:i+seq_len]
        idx = i+seq_len
        while idx < len(ciphertext):
            idx = ciphertext.find(pattern, idx)
            if idx == -1:
                break
            dist.append(idx - i)
            idx += seq_len
    guess = {}
    for i in range(len(dist)):
        for j in range(i+1, len(dist)):
            gcd = math.gcd(dist[i], dist[j])
            if gcd!=1:
                if gcd in guess:
                    guess[gcd] += 1
                else:
                    guess[gcd] = 1
    guess = dict(sorted(guess.items(), key = lambda x: x[1], reverse = True))
    return guess

def freq_count(ciphertext, key_len, seq_len = 1):
    freq = []
    for s in range(key_len):
        freq.append(dict.fromkeys(list(charset), 0))
        for i in range(s, len(ciphertext)-seq_len+1, key_len):
            freq[s][ciphertext[i]] += 1
    return freq
    
print(get_potential_key_length(ct, 3))
print(freq_count(ct, 10))