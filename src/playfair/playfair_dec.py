from playfair_enc import Playfair

def write_file(iteration, buffer):
    f = open(f"plaintext/playfair/iteration_{iteration}.flag", "w+")
    f.write(buffer)
    f.close()

f = open("cipher/playfair.enc", "r")
ct = f.read().strip()
ct = "".join(ct.split("\n"))
f.close()

write_file("last", Playfair("turnbackfeeldigital").decrypt(ct))