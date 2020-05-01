from struct import pack, unpack

def F(w):
    return ((w * 31337) ^ (w * 1337 >> 16)) % 2**32

def decrypt(block):
    a, b, c, d = unpack("<4I", block)
    for i in range(32):
        # decrypting the second step in encrypt
        tempa = a
        d = d ^ 1337
        a = c ^ (F(d | F(d) ^ d))
        b = b ^ (F(d ^ F(a) ^ (d | a)))
        c = tempa ^ (F(d | F(b ^ F(a)) ^ F(d | b) ^ a))
        # decrypting the frist step in encrypt
        tempa = a
        a = d ^ 31337
        d = c ^ (F(a | F(a) ^ a))
        c = b ^ (F(a ^ F(d) ^ (a | d)))
        b = tempa ^ (F(a | F(c ^ F(d)) ^ F(a | c) ^ d))
        plaintext = "{}".format(pack("<4I", a, b, c, d))
    return plaintext[1:].replace("'" ,"")


ct = open("flag.enc","rb").read()
pt = "".join(decrypt(ct[i:i+16]) for i in range(0,len(ct), 16))
print (pt[0:pt.index('#')])
