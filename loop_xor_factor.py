#!/usr/bin/env python3

from Crypto.Util import number

import xor_factor as xf

PRIME_BITS = 512

def prime():
    # Turns out number.getPrime(4) occasionally returns 17, which is a
    # 5-bit number.
    while True:
        n = number.getPrime(PRIME_BITS)
        if n < (1<<PRIME_BITS):
            return n

def test_one():
    p = prime()
    q = prime()
    if q < p:
        p, q = q, p
    n = p*q

    print('p=' + hex(p)[2:])
    print('q=' + hex(q)[2:])
    print('Factoring...')
    a, b = xf.factor(n, p^q)
    if (a, b) == (p, q):
        print('Success!')
    else:
        print('Weird: Got p={}, q={}'.format(hex(a)[2:], hex(b)[2:]))
    print()

def main():
    while True:
        test_one()

if __name__ == '__main__':
    main()
