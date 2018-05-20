from math import sqrt, ceil

def get_private_key(e, p, q):
  fin = (p-1)*(q-1)
  d = gcd_ext(e, fin)
  if d[1] < 0:
    return d[1]+fin, p*q
  return d[1], p*q

def hack(public_key):
  fin = euler(public_key[1])
  d = gcd_ext(public_key[0], fin)
  if d[1] < 0:
    return d[1]+fin, public_key[1]
  return d[1], public_key[1]

def rsa(message, key):
  return power_mod(message, key[0], key[1])

def gcd_ext(a, b):
  if b == 0:
    return a, 1, 0
  else:
    d, x, y = gcd_ext(b, a % b)
    return d, y, x - y * (a // b)

def power_mod(num, power, mod):
  count = 1
  if power == 0:
    return 1
  while power != 0:
    if power % 2 == 0:
      power //= 2
      num *= num
      num %= mod
    else:
      power -= 1
      count *= num
      count %= mod
  return count % mod

def euler(num):
  res = num
  for i in range(2, ceil(sqrt(num))):
    if num % i == 0:
      while num % i == 0:
        num //= i
      res -= res // i
  if num > 1:
    res -= res // num
  return res

def rsa_string(message, key, encoding = True):
  processed = ''
  last = 0
  for letter in message:
    if encoding:
      processed += chr(rsa(ord(letter), key) + last % key[1])
    else:
      processed += chr(rsa(ord(letter), key) - last % key[1])
  return processed
