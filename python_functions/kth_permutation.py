def kth_permutation(n,k):
    permutation = []
    unsed = list(range(1,n+1))
    fact = [1]*(n+1)
    for i in range(1,n+1):
        fact[i]=i*fact[i-1]
    k -= 1
    while n > 0:
        part_length = fact[n]//n
        i = k//part_length
        permutation.append(unsed[i])
        unsed.pop(i)
        n-=1
        k %= part_length
    return ''.join(map(str,permutation))
    