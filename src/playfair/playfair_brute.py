from playfair_enc import Playfair

def quadgram_fitness(iptext):
    a = iptext
    quadtext = [a[idx:idx+4] for idx in range(len(a)-3)]
    quaddict={}
    with open("data/english_quadgrams_log.txt") as f:
        for line in f:
            quaddict[line.split(",")[0]]= float(line.split(",")[1])

    sum = 0
    for quad in quadtext:
        sum += (quaddict.get(quad.upper(),0))
    return abs(sum)/len(quadtext)



f = open("cipher/playfair.enc", "r")
ct = f.read().strip()
ct = "".join(ct.split("\n"))
f.close()

ct = ct[-100:]

f = open("data/english_words.txt", "r")
words = f.readlines()
words = [c.split()[1] for c in words]
f.close()

mp = {}
cnt = 0


for word in words:
    if cnt%10 == 0:
        print(cnt)
    cnt += 1
    cipher = Playfair(word)
    score = quadgram_fitness(cipher.decrypt(ct))
    mp[word] = score
    
mp = (sorted(mp.items(), key=lambda x: x[1], reverse=True)[:5])
save = [c[0] for c in mp]
print(mp)
cnt = 0
mp = {}
for s in save:
    for w in words:
        if cnt%10 == 0:
            print(cnt)
        cnt += 1
        word = s+w
        cipher = Playfair(word)
        score = quadgram_fitness(cipher.decrypt(ct))
        mp[word] = score
mp = (sorted(mp.items(), key=lambda x: x[1], reverse=True)[:5])
save = [c[0] for c in mp]
print(mp)
cnt = 0
mp = {}
for s in save:
    for w in words:
        if cnt%10 == 0:
            print(cnt)
        cnt += 1
        word = s+w
        cipher = Playfair(word)
        score = quadgram_fitness(cipher.decrypt(ct))
        mp[word] = score
mp = (sorted(mp.items(), key=lambda x: x[1], reverse=True)[:100])

save = [c[0] for c in mp if c[1] > 2]
cnt = 0
mp = {}
for s in save:
    for w in words:
        if cnt%10 == 0:
            print(cnt)
        cnt += 1
        word = s+w
        cipher = Playfair(word)
        if (cipher.encrypt("THHE") == "BLSH"):
            score = quadgram_fitness(cipher.decrypt(ct))
            mp[word] = score
mp = (sorted(mp.items(), key=lambda x: x[1], reverse=True)[:100])
print(mp)
