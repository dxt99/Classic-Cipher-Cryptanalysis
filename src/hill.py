import string
import numpy as np

f = open("cipher/hill.enc", "r")
ct = f.read().strip()
ct = "".join(ct.split("\n"))
f.close()

charset = string.ascii_uppercase

def idx(c):
    return charset.find(c)

def mod_matmul(a, b, m=26):
    c = np.matmul(a, b)
    return np.fromiter(map(lambda x: round(x)%m, c), dtype=np.int32)

def minor(arr,i,j):
    # ith row, jth column removed
    return arr[np.array(list(range(i))+list(range(i+1,arr.shape[0])))[:,np.newaxis],
               np.array(list(range(j))+list(range(j+1,arr.shape[1])))]

def mod_inv(a, m=26):
    assert(a.shape[0] == a.shape[1])
    c = np.zeros(a.shape)
    invdet = pow(round(np.linalg.det(a)), -1, m)
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            c[i, j] = (pow(-1, (i+j)) * np.linalg.det(minor(a, i, j))) % 26
            c[i, j] = (c[i, j] * invdet) % 26
    return np.matrix.transpose(c)

plaintext = "HELLOCAPTAINHADDOCK"

# construct mult matrix
k = np.zeros(shape=(3,3))
for i in range(0, 9, 3):
    k[i//3] = [idx(plaintext[j]) for j in range(i, i+3)]

# find keys
inv_k = mod_inv(k)
k1 = [idx(ct[i]) for i in range(0, 9, 3)]
k2 = [idx(ct[i+1]) for i in range(0, 9, 3)]
k3 = [idx(ct[i+2]) for i in range(0, 9, 3)]

print("Key: ")
print(mod_matmul(inv_k, k1))
print(mod_matmul(inv_k, k2))
print(mod_matmul(inv_k, k3))