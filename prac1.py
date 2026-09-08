def sumpro(*x):
    a=0
    p=1
    for i in x:
        a+=i
        p*=i
        return a,p
        