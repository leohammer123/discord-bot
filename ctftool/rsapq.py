def rsapq(p,q,e,ct):
  p = int(p)
  q = int(q)
  e = int(e)
  ct = int(ct)
  def egcd(a, b):
      if a == 0:
          return (b, 0, 1)
      else:
          g, y, x = egcd(b % a, a)
          return (g, x - (b // a) * y, y)

  def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
  n = p * q
  phi = (p - 1) * (q - 1)
  gcd, a, b = egcd(e, phi)
  d = a
  pt = pow(ct, d, n)
  return str(pt)