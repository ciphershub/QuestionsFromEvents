def getWays(n, c):
    temp=[0]*(n+1)
    temp[0]=1
    for x in c:
        for y in range(x, n+1):
            temp[y]+=temp[y-x]
    return temp[n]
