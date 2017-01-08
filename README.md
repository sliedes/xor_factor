Let p and q be two (large, unknown) primes. Moreover, let us know n=pq
and x=p XOR q.

Given numbers n and x, this code efficiently (but slightly slowly,
because it's Python) factors n and outputs p and q.

Usage:
```
./ xor_factor.py n x
```

The algorithm is the one described [in this Math StackExchange
answer](http://math.stackexchange.com/a/2087589/123786).
