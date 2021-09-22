def xor(plaintext,key):
  n = 0
  cipher = ''
  q = len(plaintext)%len(key)
  for r in plaintext:
    cipher += chr(ord(r)^ord(key[q]))
    if not(chr(ord(r)^ord(key[q])).isprintable()):
        n = 1
  if n:
        cipher = str(cipher.encode())
  return cipher
