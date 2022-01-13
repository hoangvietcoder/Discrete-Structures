import itertools


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


# Câu 1
print('Câu 1')
table = list(itertools.product([True, False], repeat=3))
p = [a[0] for a in table]
q = [a[1] for a in table]
r = [a[2] for a in table]

p_or_q = lLOr(p, q)
p_or_q_implies_r = lLImplies(p_or_q, r)
table_1 = list(zip(p, q, r, p_or_q, p_or_q_implies_r))

print('pvq->r')
print('p \t\t q \t\t r \t\tpvq \tpvq->r')

for i in range(len(p)):
    print(*table_1[i], sep='\t')

print()
p_and_not_q = lLAnd(p, lLNot(q))
r_implies_p_and_not_q = lLImplies(r, p_and_not_q)
table_2 = list(zip(p, q, r, p_and_not_q, r_implies_p_and_not_q))

print('r->p^~q')
print('p \t\t q \t\t r \t\tp^~q \tr->p^~q')

for i in range(len(p)):
    print(*table_2[i], sep='\t')
