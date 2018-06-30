def solution(S, P, Q):
    N = len(S)
    M = len(P)
    res = []
    pars_s = []
    nuc_dict = {
        'A': 1,
        'C': 2,
        'G': 3,
        'T': 4
    }
    for i in range(N):
        pars_s.append(nuc_dict[S[i]])
    for i in range(M):
        res.append(min(pars_s[P[i]:Q[i]+1]))
    return res
