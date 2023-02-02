import math
import string

f = open("cipher/kasiski.enc", "r")
ct = f.read().strip()
ct = "".join(ct.split("\n"))
f.close()

charset = string.ascii_uppercase
LEN_CHARSET = len(charset)

# Count trigram
# for each trigram, find len of the duplicate trigram
def get_potential_key_length(ciphertext, seq_len=3):
    dist = []
    # trigram = {}
    for i in range(len(ciphertext) - seq_len + 1):
        pattern = ct[i : i + seq_len]
        idx = i + seq_len
        # if pattern in trigram:
        #     continue
        # trigram[pattern] = 0
        while idx < len(ciphertext):
            idx = ciphertext.find(pattern, idx)
            if idx == -1:
                break
            dist.append(idx - i)
            # trigram[pattern] += 1
            idx += seq_len

    # print(sorted(trigram.items(), key=lambda x: x[1], reverse=True))
    # For each trigram find the intersection (gcd)
    guess = {}
    for i in range(len(dist)):
        for j in range(i + 1, len(dist)):
            gcd = math.gcd(dist[i], dist[j])
            if gcd != 1:
                if gcd in guess:
                    guess[gcd] += 1
                else:
                    guess[gcd] = 1
    guess = dict(sorted(guess.items(), key=lambda x: x[1], reverse=True))
    return guess


# print(get_potential_key_length(ct, 3))
# Because 10 is the most shared factor so the key len is most likely 10
# Use frequency analysis to figure out the cipher text
# Every same word with the distance of 10 character will give same output
# In english word the most frequent word E, T, A, O, I, N, S, H, R, dan D
def freq_count(ciphertext, key_len, seq_len=1):
    freq = []
    for s in range(key_len):
        freq.append(dict.fromkeys(list(charset), 0))
        for i in range(s, len(ciphertext) - seq_len + 1, key_len):
            freq[s][ciphertext[i]] += 1
    return freq


freq = freq_count(ct, 10)

# Most frequent character in each column
def freq_analysis(freq):
    most_frequent = []
    for frequency in freq:
        most_frequent.append(
            sorted(frequency.items(), key=lambda x: x[1], reverse=True)[0]
        )

    return most_frequent
  
# Try to map the frequency to english most used character E, T, A, O, I, N, S, H, R, dan D

frequent = [
    "R",
    "E",
    "W",
    "K",
    "I",
    "H",
    "P",
    "S",
    "K",
    "Y",
]

def initial_key(list_of_char=[], plain_char="E"):
    keys = ""
    for c in list_of_char:
        idx = charset.find(c) - charset.find(plain_char)
        keys += charset[idx % LEN_CHARSET]
    
    return keys


def make_key(text="AAAAAAAAAA", index=0, char="A"):
    keys = ""
    for i in range(10):
        if i == index:
            keys += char
        else:
          keys += text[i]

    return keys


def vignere(ciphertext, key):
    plaintext = ""
    cur = 0
    for c in ciphertext:
        key_to_check = key[cur]
        idx = charset.find(c) - charset.find(key_to_check)
        plaintext += charset[idx % LEN_CHARSET]
        cur += 1
        cur %= 10

    return plaintext


def write_file(iteration, buffer):
    f = open(f"plaintext/kasiski/iteration_{iteration}.txt", "w+")
    f.write(buffer)
    f.close()


# === First iteration assume all are E
# key = make_key("E")
key = initial_key(frequent, "E") # NASGEDLOGU
# write_file(1, vignere(ct, key))

# === Second iteration
# KNSW -> KNOW in the plaintext
# f = open("plaintext/kasiski/iteration_1.txt", "r")
# ct = f.read().strip()
# ct = "".join(ct.split(" "))
# f.close()
# idx = ct.find("KNSW")  # Index ke 97

# ct_part = ct[97:97+4] # YTMJ

# idx = charset.find("M") - charset.find("O")
# char = charset[idx % LEN_CHARSET] # Y
key = make_key(key, 9, "Y") # NASGEDLOGY
# write_file(2, vignere(ct, key))

# === Third iteration:
# ALCEADY -> ALREADY
# KRSW -> KNOW

# f = open("plaintext/kasiski/iteration_2.txt", "r")
# ct = f.read().strip()
# ct = "".join(ct.split(" "))
# f.close()
# idx_1 = ct.find("KRSW")  # Index ke 20
# idx_2 = ct.find("ALCEADY") # Index ke 13

# KRSW = ct[20:20 + 4] # 20, XRKC
# ALCEADY = ct[13:13 + 7] #13, GPFPOJW

# a = charset.find("F") - charset.find("R")
# a = charset[a % LEN_CHARSET] # O
# b = charset.find("R") - charset.find("N")
# b = charset[b % LEN_CHARSET] # E
# c = charset.find("K") - charset.find("O")
# c = charset[c % LEN_CHARSET] # W

key = make_key(key, 1, "E")
key = make_key(key, 2, "W")
key = make_key(key, 5, "O")
write_file(3, vignere(ct, key))
