def matrix_mult(m, n):
    m1, m2, m3, m4 = m[0][0], m[0][1], m[1][0], m[1][1]
    n1, n2, n3, n4 = n[0][0], n[0][1], n[1][0], n[1][1]
    return ((m1 * n1 + m2 * n3, m1 * n2 + m2 * n4), (m3 * n1 + m4 * n3, m3 * n2 + m4 * n4))

identity = ((1, 0), (0, 1))

def prebuild_matrix(n):
    a = ((1, 1), (1, 0))
    fibm = [a]
    for _ in range(n):
        prev = fibm[-1]
        fibm.append(matrix_mult(prev, prev))
    return fibm

fibm = prebuild_matrix(24)

def fast_fib(n):
    if n <= 2:
        return 1
    else:
        n -= 1
        x = (bin(n)[2:])[::-1]
        indexes = [i for i, xx in enumerate(x) if xx == '1']
        mms = [fibm[i] for i in indexes]
        fibn = reduce(matrix_mult, mms, identity)
        return fibn[0][0]
