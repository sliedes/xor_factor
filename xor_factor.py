#!/usr/bin/env python3

import math
import sys

def check_cong(k, p, q, n, xored=None):
    kmask = (1 << k) - 1
    p &= kmask
    q &= kmask
    n &= kmask
    pqm = (p*q) & kmask
    return pqm == n and (xored is None or (p^q) == (xored & kmask))

def extend(k, a):
    kbit = 1 << (k-1)
    assert a < kbit
    yield a
    yield a | kbit

def factor(n, p_xor_q):
    tracked = set([(p, q) for p in [0, 1] for q in [0, 1]
                   if check_cong(1, p, q, n, p_xor_q)])

    PRIME_BITS = int(math.ceil(math.log(n, 2)/2))

    maxtracked = len(tracked)
    for k in range(2, PRIME_BITS+1):
        newset = set()
        for tp, tq in tracked:
            for newp_ in extend(k, tp):
                for newq_ in extend(k, tq):
                    # Remove symmetry
                    newp, newq = sorted([newp_, newq_])
                    if check_cong(k, newp, newq, n, p_xor_q):
                        newset.add((newp, newq))

        tracked = newset
        if len(tracked) > maxtracked:
            maxtracked = len(tracked)
    print('Tracked set size: {} (max={})'.format(len(tracked), maxtracked))

    # go through the tracked set and pick the correct (p, q)
    for p, q in tracked:
        if p != 1 and p*q == n:
            return p, q

    assert False, 'factors were not in tracked set. Is your p^q correct?'

def main():
    if len(sys.argv) != 3:
        print('Usage: xor_factor.py n p_xor_q', file=sys.stderr)
        print('(give both numbers in decimal)', file=sys.stderr)

    n = int(sys.argv[1])
    p_xor_q = int(sys.argv[2])

    p, q = factor(n, p_xor_q)
    print(p)
    print(q)

if __name__ == '__main__':
    main()
