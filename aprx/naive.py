import pandas as pd
import numpy as np

def mk_coef(p):
    n = len(p)
    A = np.ones([n,n], dtype=np.float64)
    B = np.ones(n,     dtype=np.float64)

    for i in range(n):
        x,y = p[i]
        for j in range(n):
            A[i][j] = x**(n-j-1)
        B[i] = y
    
    return np.linalg.solve(A,B) 

def mk_polinomial(k):
    def f(x):
        s = 0
        for idx, i in enumerate(k):
            s += i * x**(len(k)-idx-1)
        return s
    return f