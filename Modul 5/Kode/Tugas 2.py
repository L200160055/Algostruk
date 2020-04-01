def AB(a,b):
    c=a+b
    n=len(c)
    for i in range(1,n):
        nilai=c[i]
        pos=i
        while pos > 0 and nilai < c[pos-1]:
            c[pos]=c[pos-1]
            pos=pos-1
        c[pos] = nilai
    return c
