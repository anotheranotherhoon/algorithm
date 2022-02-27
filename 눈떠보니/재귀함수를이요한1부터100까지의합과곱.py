def f(n):
    if n<=1:
        return 1
    else:
        return n+f(n-1)

def fs(n):
    if n<=1:
        return 1
    else:
        return n*fs(n-1)
