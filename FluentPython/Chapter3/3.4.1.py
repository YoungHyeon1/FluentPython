tt = (1, 2, (30, 40))
hash(tt)

tl = (1, 2, [30, 40])
# hash(tl) list 형식이라 안됨

tf = (1, 2, frozenset([30, 40]))
hash(tf)

