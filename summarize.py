from z3 import *

def plus(a1, a2):
    return a1 + a2
    # v9 = 0
    # v5 = 0
    # v6 = 0
    # while a1 or a2:
    #     v7 = a1 & 1
    #     v8 = a2 & 1
    #     a1 >>= 1;
    #     a2 >>= 1;
    #     v9 += (v5 ^ v8 ^ v7) << v6;
    #     v5 = v5 & v7 | v8 & v7 | v5 & v8;
    #     v6 += 1
    # return (v5 << v6) + v9

def plus_min(a1, a2):
    return plus(a1, -a2)

def multiply(a1, a2):
    return a1*a2
    # v4 = 0
    # v5 = 0
    # while a1:
    #     v4 += (a1 & 1) * (a2 << v5)
    #     a1 >>= 1
    #     v5 += 1
    # return v4

def xor(a1, a2):
    return a1^a2
    # v5 = 0
    # v6 = 0
    # while a1 or a2:
    #     v7 = a1 & 1
    #     v8 = a2 & 1
    #     a1 >>= 1
    #     a2 >>= 1
    #     v5 += (v8 ^ v7) << v6
    #     v6 += 1
    # return v5

def And(a1, a2):
    return a1 & a2
    # v5 = 0
    # v6 = 0
    # while a1 or a2:
    #     v7 = a1 & 1
    #     v8 = a2 & 1
    #     a1 >>= 1
    #     a2 >>= 1
    #     v5 += (v8 & v7) << v6
    #     v6 += 1
    # return v5

a1 = BitVec("a1", 32)
a2 = BitVec("a2", 32)
a3 = BitVec("a3", 32)
a4 = BitVec("a4", 32)
a5 = BitVec("a5", 32)
a6 = BitVec("a6", 32)
s = Solver()
s.add(a1 > 100000000, a1 < 999999999, a2 > 100000000, a2 < 999999999, a3 > 100000000, a3 < 999999999, a4 > 100000000, a4 < 999999999, a5 > 100000000, a5 < 999999999, a6 > 100000000, a6 < 999999999)
s.add(((a1 - a2) + a3) % 17492321 == 4139449)   #v18
s.add((a1 + a2) % 17381917 == 9166034)                                                                                              #v19
s.add(((3*a1) - (2*a2)) % (a1^a4) == 556569677)                                                         #v20
s.add(((a3 + a1) & a2) % 28194 == 12734)                                                                                                     #v21
s.add((a2 + a4) % a1 == 540591164)                                                                                                  #v22
s.add(((a4 + a6) ^ a3) % 1893928 == 1279714) #v23
s.add((a5-a6) % 18294018 == 17026895) #v24
s.add((a5 + a6) % 48328579 == 23769303) #v25
s.check()
model = s.model()
print(model)

#print(plus(190,10))
#print(123*97)
# v7 = plus_min(a1, a2)
# v18 = plus(v7, a3) % 17492321
# v19 = plus(a1, a2) % 17381917
# v8 = multiply(2LL, a2)
# v9 = multiply(3LL, a1)
# v10 = plus_min(v9, v8)
# v20 = v10 % xor(a1, a4)
# v11 = plus(a3, a1);
# v21 = And(a2, v11) % 28194;
# v22 = plus(a2, a4) % a1;
# v12 = plus(a4, a6);
# v23 = xor(a3, v12) % 1893928;
# v24 = plus_min(a5, a6) % 18294018;
# v25 = plus(a5, a6) % 48328579;

# v18 == 4139449
# v19 == 9166034
# v20 == 556569677
# v21 == 12734
# v22 == 540591164
# v23 == 1279714
# v24 == 17026895
# v25 == 23769303