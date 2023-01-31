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

"""
{10: 111377, 20: 31365, 2: 23831, 5: 14037, 30: 12659, 40: 9240, 4: 6786, 3: 4935, 70: 4582, 50: 4294, 60: 3502, 6: 3187, 15: 2650, 8: 2124, 80: 2029, 90: 1556, 100: 1095, 120: 1075, 7: 1068, 140: 969, 12: 893, 35: 818, 110: 691, 25: 600, 130: 497, 190: 487, 160: 469, 16: 454, 170: 422, 18: 409, 240: 370, 24: 357, 14: 345, 150: 330, 9: 319, 11: 289, 45: 236, 26: 207, 220: 206, 180: 205, 200: 203, 28: 175, 48: 167, 22: 161, 260: 153, 13: 143, 55: 134, 250: 134, 270: 129, 36: 114, 320: 110, 230: 103, 350: 98, 290: 98, 380: 95, 17: 94, 400: 93, 75: 84, 390: 78, 210: 77, 430: 77, 280: 69, 44: 68, 21: 67, 1330: 66, 590: 65, 32: 63, 820: 63, 105: 62, 38: 61, 58: 56, 810: 55, 85: 54, 500: 54, 340: 51, 370: 50, 330: 49, 34: 47, 72: 46, 470: 46, 440: 45, 880: 45, 570: 45, 550: 45, 46: 44, 19: 41, 310: 39, 165: 39, 300: 39, 410: 38, 1170: 36, 730: 36, 690: 34, 62: 33, 88: 33, 78: 33, 490: 33, 132: 32, 360: 32, 64: 30, 740: 29, 1600: 28, 1160: 28, 1720: 28, 74: 28, 95: 27, 660: 27, 790: 27, 610: 27, 146: 27, 33: 25, 295: 25, 118: 25, 450: 25, 510: 24, 83: 22, 27: 22, 830: 21, 68: 21, 49: 21, 1300: 21, 600: 21, 66: 21, 176: 20, 52: 20, 480: 20, 59: 20, 345: 20, 29: 19, 680: 18, 23: 18, 119: 18, 800: 17, 580: 17, 92: 17, 158: 16, 115: 16, 415: 15, 650: 15, 76: 15, 560: 15, 205: 15, 850: 15, 1200: 15, 69: 15, 1190: 15, 51: 14, 640: 14, 670: 14, 460: 14, 122: 14, 710: 14, 185: 14, 770: 14, 82: 13, 56: 12, 215: 12, 43: 12, 96: 12, 73: 12, 385: 12, 285: 11, 99: 11, 162: 11, 405: 11, 235: 11, 1090: 10, 275: 10, 167: 10, 2070: 10, 1670: 10, 2030: 10, 255: 9, 54: 9, 135: 9, 520: 9, 1140: 9, 172: 9, 136: 9, 630: 9, 396: 9, 178: 9, 860: 8, 305: 8, 420: 8, 138: 8, 77: 8, 225: 8, 264: 8, 42: 7, 129: 7, 1020: 6, 204: 6, 128: 6, 1120: 6, 101: 6, 144: 6, 780: 6, 1260: 6, 1530: 6, 102: 6, 142: 6, 166: 6, 1480: 6, 1290: 6, 890: 6, 238: 6, 595: 6, 322: 6, 700: 6, 245: 6, 274: 5, 1110: 5, 940: 5, 184: 4, 198: 4, 252: 4, 97: 4, 306: 4, 645: 4, 258: 4, 930: 3, 1730: 3, 408: 3, 1470: 3, 735: 3, 1640: 3, 1840: 3, 920: 3, 86: 3, 620: 3, 1010: 3, 485: 3, 970: 3, 292: 3, 1410: 3, 900: 3, 1610: 3, 1210: 3, 910: 3, 272: 3, 1360: 3, 1080: 3, 540: 3, 214: 2, 157: 2, 246: 2, 288: 2, 495: 2, 168: 2, 179: 2, 575: 2, 197: 2, 361: 2, 276: 2, 183: 2, 159: 2, 126: 2, 244: 2, 37: 2, 1070: 1, 332: 1, 316: 1, 2370: 1, 1050: 1, 1040: 1, 2280: 1, 1230: 1, 1340: 1, 764: 1, 2150: 1, 1130: 1, 1440: 1, 2210: 1, 1180: 1, 990: 1, 840: 1, 1370: 1, 1725: 1, 1000: 1, 1570: 1, 501: 1, 1970: 1, 722: 1, 2220: 1, 1380: 1, 1280: 1, 81: 1, 366: 1, 1420: 1, 530: 1, 318: 1, 41: 1, 271: 1, 853: 1, 750: 1, 1880: 1, 1540: 1, 1030: 1, 1584: 1, 1320: 1, 192: 1, 644: 1, 1220: 1, 241: 1, 313: 1, 1569: 1, 1313: 1, 249: 1, 1253: 1, 967: 1, 677: 1, 53: 1, 261: 1, 174: 1, 962: 1, 106: 1, 1155: 1, 87: 1}
"""

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

"""
[{'A': 17, 'B': 20, 'C': 3, 'D': 2, 'E': 15, 'F': 17, 'G': 20, 'H': 7, 'I': 4, 'J': 3, 'K': 0, 'L': 6, 'M': 0, 'N': 22, 'O': 4, 'P': 5, 'Q': 8, 'R': 34, 'S': 2, 'T': 2, 'U': 15, 'V': 23, 'W': 0, 'X': 6, 'Y': 12, 'Z': 7}, {'A': 6, 'B': 0, 'C': 3, 'D': 0, 'E': 28, 'F': 6, 'G': 5, 'H': 13, 'I': 26, 'J': 7, 'K': 3, 'L': 17, 'M': 10, 'N': 0, 'O': 1, 'P': 16, 'Q': 5, 'R': 16, 'S': 24, 'T': 3, 'U': 0, 'V': 12, 'W': 22, 'X': 20, 'Y': 9, 'Z': 2}, {'A': 28, 'B': 5, 'C': 3, 'D': 13, 'E': 20, 'F': 1, 'G': 3, 'H': 11, 'I': 7, 'J': 12, 'K': 16, 'L': 4, 'M': 0, 'N': 12, 'O': 24, 'P': 26, 'Q': 8, 'R': 2, 'S': 3, 'T': 2, 'U': 2, 'V': 0, 'W': 35, 'X': 4, 'Y': 7, 'Z': 6}, {'A': 5, 'B': 3, 'C': 7, 'D': 0, 'E': 4, 'F': 0, 'G': 22, 'H': 6, 'I': 7, 'J': 10, 'K': 30, 'L': 9, 'M': 4, 'N': 21, 'O': 10, 'P': 0, 'Q': 2, 'R': 14, 'S': 7, 'T': 18, 'U': 17, 'V': 5, 'W': 0, 'X': 16, 'Y': 13, 'Z': 24}, {'A': 1, 'B': 0, 'C': 3, 'D': 0, 'E': 24, 'F': 4, 'G': 5, 'H': 14, 'I': 36, 'J': 7, 'K': 1, 'L': 7, 'M': 24, 'N': 0, 'O': 3, 'P': 11, 'Q': 6, 'R': 8, 'S': 23, 'T': 4, 'U': 0, 'V': 16, 'W': 19, 'X': 27, 'Y': 9, 'Z': 1}, {'A': 8, 'B': 20, 'C': 24, 'D': 7, 'E': 0, 'F': 14, 'G': 20, 'H': 30, 'I': 10, 'J': 0, 'K': 5, 'L': 0, 'M': 2, 'N': 1, 'O': 24, 'P': 8, 'Q': 7, 'R': 8, 'S': 22, 'T': 6, 'U': 2, 'V': 14, 'W': 12, 'X': 0, 'Y': 2, 'Z': 7}, {'A': 5, 'B': 0, 'C': 15, 'D': 11, 'E': 22, 'F': 7, 'G': 1, 'H': 1, 'I': 0, 'J': 2, 'K': 0, 'L': 14, 'M': 5, 'N': 6, 'O': 11, 'P': 37, 'Q': 7, 'R': 6, 'S': 21, 'T': 21, 'U': 0, 'V': 4, 'W': 6, 'X': 7, 'Y': 17, 'Z': 27}, {'A': 8, 'B': 12, 'C': 26, 'D': 4, 'E': 0, 'F': 16, 'G': 18, 'H': 24, 'I': 7, 'J': 4, 'K': 10, 'L': 0, 'M': 5, 'N': 0, 'O': 26, 'P': 3, 'Q': 6, 'R': 11, 'S': 27, 'T': 6, 'U': 3, 'V': 12, 'W': 13, 'X': 0, 'Y': 4, 'Z': 8}, {'A': 5, 'B': 5, 'C': 4, 'D': 0, 'E': 5, 'F': 0, 'G': 25, 'H': 6, 'I': 4, 'J': 9, 'K': 32, 'L': 14, 'M': 3, 'N': 16, 'O': 21, 'P': 0, 'Q': 2, 'R': 9, 'S': 0, 'T': 14, 'U': 18, 'V': 7, 'W': 0, 'X': 12, 'Y': 23, 'Z': 19}, {'A': 6, 'B': 11, 'C': 24, 'D': 4, 'E': 1, 'F': 15, 'G': 21, 'H': 0, 'I': 2, 'J': 10, 'K': 7, 'L': 13, 'M': 23, 'N': 4, 'O': 0, 'P': 20, 'Q': 13, 'R': 22, 'S': 6, 'T': 6, 'U': 6, 'V': 0, 'W': 5, 'X': 0, 'Y': 27, 'Z': 7}]
"""

# Most frequent character in each column
def freq_analysis(freq):
    most_frequent = []
    for frequency in freq:
        most_frequent.append(
            sorted(frequency.items(), key=lambda x: x[1], reverse=True)[0]
        )

    return most_frequent


# print(freq_analysis(freq))
"""
[
('R', 34), 
('E', 28), 
('W', 35), 
('K', 30), 
('I', 36), 
('H', 30), 
('P', 37), 
('S', 27), 
('K', 32), 
('Y', 27)]
"""

# Try to map the frequency to english most used character E, T, A, O, I, N, S, H, R, dan D

"""
1	  the
2	  and
3	  tha
4	  ent
5	  ing
6	  ion
7	  tio
8	  for
9	  nde
10	has
11	nce
12	edt
13	tis
14	oft
15	sth
16	men
"""

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


def make_key(char="E"):
    keys = ""
    for i in range(10):
        idx = charset.find(frequent[i]) - charset.find(char)
        keys += charset[idx % LEN_CHARSET]

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


# First iteration assume all are E
# key = make_key("E")
# write_file(1, vignere(ct, key))

# KEY: NASGEDLOGU

# Second iteration
# `ISE` is most likely ISA in the plaintext
# f = open("plaintext/kasiski/iteration_1.txt", "r")
# ct = f.read().strip()
# ct = "".join(ct.split("\n"))
# f.close()
# idx = ct.find("ISE")  9 0 1
# print(idx, idx % 10)
# idx = charset.find("E") - charset.find("A")
# char = charset[idx % LEN_CHARSET]
# key = "N" + char + "SGEDLOGU" NESGEDLOGU
# print(key)
# write_file(2, vignere(ct, key))

# Third iteration: NEWGEDLOGU
# KNSW -> KNOW in the plaintext
# XRKC -> KNOW, K -> O
# f = open("plaintext/kasiski/iteration_2.txt", "r")
# ct = f.read().strip()
# ct = "".join(ct.split(" "))
# f.close()
# idx = ct.find("KNSW")  # Index ke 20
# print(idx) S ada di index ke 2 berati huruf 2
# idx = charset.find("K") - charset.find("O")
# char = charset[idx % LEN_CHARSET]
# key = "NE" + char + "GEDLOGU"
# write_file(3, vignere(ct, "NEWGEDLOGU"))

# Fourth iteration: NEWGEOLOGY
# PPOPLI -> PEOPLE plaintext
# TSZDRC -> PEOPLE, S -> E, C -> E
# f = open("plaintext/kasiski/iteration_3.txt", "r")
# ct = f.read().strip()
# ct = "".join(ct.split(" "))
# f.close()
# idx = ct.find("PPOPLI")  # Index ke 20
# print(idx)  # S ada di index ke 4 berati huruf 5,9
# print(ct[4 : 4 + 6])
# a = charset.find("S") - charset.find("E")
# a = charset[a % LEN_CHARSET]
# b = charset.find("C") - charset.find("E")
# b = charset[b % LEN_CHARSET]
# key = "NEWGE" + a + "LOG" + b
# write_file(4, vignere(ct, "NEWGEOLOGY"))
