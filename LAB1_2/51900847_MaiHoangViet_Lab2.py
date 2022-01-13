import itertools


# Câu 1
def lImplies(p, q):
    if p:
        return q
    else:
        return True


def lAnd(p, q):
    return p and q


def lOr(p, q):
    return p or q


def lXor(p, q):
    if p != q:
        return True
    else:
        return False


def lNot(p):
    if p:
        return False
    else:
        return True


def lEquipvalent(p, q):
    if p == q:
        return True
    else:
        return False


# Câu 2
P = [True, True, False, False, False]
Q = [True, False, True, False, True]


def lLImplies(P, Q):
    return [lImplies(p, q) for p, q in zip(P, Q)]


def lLAnd(P, Q):
    return [lAnd(p, q) for p, q in zip(P, Q)]


def lLOr(P, Q):
    return [lOr(p, q) for p, q in zip(P, Q)]


def lLXor(P, Q):
    return [lXor(p, q) for p, q in zip(P, Q)]


def lLNot(P):
    return [lNot(p) for p in P]


def lLEquipvalent(P, Q):
    return [lEquipvalent(p, q) for p, q in zip(P, Q)]


print('Câu 2')
print('a) R=lLImplies(P,Q) is {}'.format(lLImplies(P, Q)))
print('b) R=lLAnd(P,Q) is {}'.format(lLAnd(P, Q)))
print('c) R=lLOr(P,Q) is {}'.format(lLOr(P, Q)))
print('d) R=lLXor(P,Q) is {}'.format(lLXor(P, Q)))
print('e) R=lLNot(P) is {}'.format(lLNot(P)))
print('f) R=lLEquipvalent(P,Q) is {}'.format(lLEquipvalent(P, Q)))

print()

# Câu 3
print('Câu 3')
table = list(itertools.product([True, False], repeat=3))
p = [a[0] for a in table]
q = [a[1] for a in table]
r = [a[2] for a in table]

p_and_q = lLAnd(p, q)
p_and_q_implies_r = lLImplies(p_and_q, r)
table_1 = list(zip(p, q, r, p_and_q, p_and_q_implies_r))

print('p^q->r')
print('p \t\t q \t\t r \t\tp^q \tp^q->r')

for i in range(len(p)):
    print(*table_1[i], sep='\t')

print()
r_implies_p_and_q = lLImplies(r, lLAnd(p, q))
table_2 = list(zip(p, q, r, p_and_q, r_implies_p_and_q))

print('r->p^q')
print('p \t\t q \t\t r \t\tp^q \tr->p^q')

for i in range(len(p)):
    print(*table_2[i], sep='\t')

print()

# Câu 4
print('Câu 4')
p_or_q = lLOr(p, q)
p_and_q = lLAnd(p, q)
not_p = lLNot(p)
not_q = lLNot(q)
not_p_or_not_q = lLOr(not_p, not_q)
p_or_q_implies_p_and_q = lLImplies(p_or_q, p_and_q)
p_or_q_implies_p_and_q_implies_not_p_or_not_q = lLImplies(p_or_q_implies_p_and_q, not_p_or_not_q)
table_3 = list(zip(p, q, r, p_or_q, p_and_q, not_p_or_not_q, p_or_q_implies_p_and_q_implies_not_p_or_not_q))

print('pvq->p^q->~pv~q')
print('p \t\t q \t\t r \t\tpvq \tp^q \t~pv~q \tpvq->p^q->~pv~q')

for i in range(len(p)):
    print(*table_3[i], sep='\t')

print()

not_p = lLNot(p)
q_and_r = lLAnd(p, r)
not_p_or_q_and_r = lLOr(not_p, q_and_r)
not_p_or_q_and_r_implies_r = lLImplies(not_p_or_q_and_r, r)
table_4 = list(zip(p, q, r, q_and_r, not_p_or_q_and_r, not_p_or_q_and_r_implies_r))

print('-pv(q^r)->r')
print('p \t\t q \t\t r \t\tq^r \t~pv(q^r) ~pv(q^r)->r')

for i in range(len(p)):
    print(*table_4[i], sep='\t')

print()

p_implies_q = lLImplies(p, q)
q_implies_r = lLImplies(q, r)
p_implies_q_or_q_implies_r = lLOr(p_implies_q, q_implies_r)
table_5 = list(zip(p, q, r, p_implies_q, q_implies_r, p_implies_q_or_q_implies_r))

print('(p->q)^(q->r)')
print('p \t\t q \t\t r \t\tp->q \tq->r \t(p->q)^(q->r)')

for i in range(len(p)):
    print(*table_5[i], sep='\t')

print()

q_and_r = lLAnd(q, r)
p_or_q_and_r = lLOr(p, q_and_r)
p_or_q = lLOr(p, q)
p_or_r = lLOr(p, r)
p_or_q_and_p_or_r = lLAnd(p_or_q, p_or_r)
p_or_q_and_r_equipvalent_p_or_q_and_p_or_r = lLEquipvalent(p_or_q_and_r, p_or_q_and_p_or_r)
table_6 = list(
    zip(p, q, r, q_and_r, p_or_q_and_r, p_or_q, p_or_r, p_or_q_and_p_or_r, p_or_q_and_r_equipvalent_p_or_q_and_p_or_r))

print('(p->q)^(q->r)')
print('p \t\tq \t\tr \t\tq^r \tpv(q^r) pvq \t pvr  (pvq)^(pvr) (p->q)^(q->r)')

for i in range(len(p)):
    print(*table_6[i], sep='\t')

print()

table_7 = list(itertools.product([True, False], repeat=4))
p = [a[0] for a in table_7]
q = [a[1] for a in table_7]
r = [a[2] for a in table_7]
t = [a[3] for a in table_7]

p_or_q = lLOr(p, q)
not_r_or_t = lLOr(lLNot(r), t)
p_or_q_implies_not_r_or_t = lLImplies(p_or_q, not_r_or_t)
table_7 = list(zip(p, q, r, t, p_or_q, not_r_or_t, p_or_q_implies_not_r_or_t))

print('pvq->~rvt')
print('p \t\tq \t\tr \t\tt \t\tpvq \t~rvt \tpvq->~rvt')

for i in range(len(p)):
    print(*table_7[i], sep='\t')

print()

p_or_t = lLOr(p, t)
p_or_t_implies_q = lLImplies(p_or_t, q)
r_implies_t = lLImplies(r, t)
p_or_t_implies_q_implies_r_implies_t = lLImplies(p_or_t_implies_q, r_implies_t)
table_8 = list(zip(p, q, r, t, p_or_t, p_or_t_implies_q_implies_r_implies_t))

print('pvt->q->(r->t)')
print('p \t\tq \t\tr \t\tt \t\tpvt \tpvt->q->(r->t)')

for i in range(len(p)):
    print(*table_8[i], sep='\t')

print()

q_and_r = lLAnd(q, r)
p_or_q_and_r = lLOr(p, q_and_r)
p_or_q = lLOr(p, q)
p_or_r = lLOr(p, r)
p_or_q_and_p_or_r = lLAnd(p_or_q, p_or_r)
not_t = lLNot(t)
t_or_not_t = lLOr(t, not_t)
p_or_q_and_p_or_r_and_t_or_not_t = lLAnd(p_or_q_and_p_or_r, t_or_not_t)
p_or_q_and_r_equipvalent_p_or_q_and_p_or_r_and_t_or_not_t = lLEquipvalent(p_or_q_and_r,
                                                                          p_or_q_and_p_or_r_and_t_or_not_t)
table_9 = list(zip(p, q, r, t, p_or_q_and_r_equipvalent_p_or_q_and_p_or_r_and_t_or_not_t))

print('(pv(q^r))<->(((pvq)^(pvr))^(tv~t))')
print('p \t\tq \t\tr \t\tt \t\t(pv(q^r))<->(((pvq)^(pvr))^(tv~t))')

for i in range(len(p)):
    print(*table_9[i], sep='\t')

print()

# Câu 5
print('Câu 5')
p = True
q = False
r = True

if p == lNot(lNot(p)):
    print('p = ~(~p): Equivalent')
else:
    print('p = ~(~p): Inequivalent')

if lAnd(lNot(lAnd(lNot(p), q)), lOr(p, q)) == q:
    print('~(~q^p)^(qvp) = q: Equivalent')
else:
    print('~(~q^p)^(qvp): Inequivalent')

if lNot(lOr(p, q)) == lOr(lNot(p), lNot(q)):
    print('~(pvq) = (~pv~q): Equivalent')
else:
    print('~(pvq) = (~pv~q): Inequivalent')

if lImplies(lOr(p, q), r) == lAnd(lImplies(p, r), lImplies(q, r)):
    print('(pvq)->r = (p->r)^(q->r): Equivalent')
else:
    print('(pvq)->r = (p->r)^(q->r): Inequivalent')

if lNot(lAnd(p, q)) == lAnd(lNot(p), lNot(q)):
    print('~(p^q) = (~p^~q): Equivalent')
else:
    print('~(p^q) = (~p^~q): Inequivalent')

if lImplies(lOr(p, lNot(q)), lNot(p)) == lImplies(lOr(p, lNot(q)), lNot(p)):
    print('(pv~q)->~p = (pv(~q))->~p: Equivalent')
else:
    print('(pv~q)->~p = (pv(~q))->~p: Inequivalent')

if lNot(lOr(p, q)) == lAnd(lNot(p), lNot(q)):
    print('~(pvq) = (~p^~q): Equivalent')
else:
    print('~(pvq) = (~p^~q): Inequivalent')

print()

# Câu 6
print('Câu 6')
# Câu a
table_10 = list(itertools.product([True, False], repeat=4))
p = [a[0] for a in table_10]
q = [a[1] for a in table_10]
r = [a[2] for a in table_10]
s = [a[3] for a in table_10]

p_implies_r = lLImplies(p, r)
not_p_implies_q = lLImplies(lLNot(p), q)
q_implies_s = lLImplies(q, s)
not_r_implies_s = lLImplies(lLNot(r), s)

result = False
for i in range(len(table_10)):
    if p_implies_r[i] and not_p_implies_q[i] and q_implies_s[i] and not_r_implies_s[i]:
        result = True
        break
if result:
    print('a) Valid')
else:
    print('a) Invalid')

# Câu b
table_11 = list(itertools.product([False, True], repeat=5))
p = [a[0] for a in table_11]
q = [a[1] for a in table_11]
r = [a[2] for a in table_11]
s = [a[3] for a in table_11]
t = [a[4] for a in table_11]

p_implies_q_implies_r = lLImplies(p, lLImplies(q, r))
p_or_s = lLOr(p, s)
t_implies_q = lLImplies(t, q)
not_s = lLNot(s)
not_r_implies_not_t = lLImplies(lLNot(r), lLNot(t))

result = False
for i in range(len(table_11)):
    if p_implies_q_implies_r[i] and p_or_s[i] and t_implies_q[i] and not_s[i] and not_r_implies_not_t[i]:
        result = True
        break
if result:
    print('b) Valid')
else:
    print('b) Invalid')

# Câu c
table_12 = list(itertools.product([True, False], repeat=4))
p = [a[0] for a in table_12]
q = [a[1] for a in table_12]
r = [a[2] for a in table_12]
s = [a[3] for a in table_12]

p_implies_q = lLImplies(p, q)
not_r_or_s = lLOr(lLNot(r), s)
p_or_r = lLOr(p, r)
not_q_implies_s = lLImplies(lLNot(q), s)

result = False
for i in range(len(table_12)):
    if p_implies_q[i] and not_r_or_s[i] and p_or_r[i] and not_q_implies_s[i]:
        result = True
        break
if result:
    print('c) Valid')
else:
    print('c) Invalid')

# Câu d
table_13 = list(itertools.product([True, False], repeat=4))
p = [a[0] for a in table_13]
q = [a[1] for a in table_13]
r = [a[2] for a in table_13]
s = [a[3] for a in table_13]
p_implies_r = lLImplies(p, r)
p_implies_q_or_not_r = lLImplies(p, lLOr(q, lLNot(r)))
not_q_or_not_s = lLOr(lLNot(q), lLNot(s))

result = False
for i in range(len(table_13)):
    if p[i] and p_implies_r[i] and p_implies_q_or_not_r[i] and not_q_or_not_s[i] and s[i]:
        result = True
        break
if result:
    print('d) Valid')
else:
    print('d) Invalid')