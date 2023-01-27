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

def parse_txt():
    FILE = './RI_5min.txt'
    #FORMAT: year, time(hhmm), close, open, high, low, avarage
    data = []
    with open(FILE) as f:
        for l in f.readlines():
            e = l.replace(' ', '').replace('\n','').split(',')
            e[0] = f'20{e[0][1:3]}/{e[0][3:5]}/{e[0][5:7]} {e[1][:-3]}'
            e.pop(1)
            data.append(e)
            
    
    df = pd.DataFrame(data)
    df = df.set_axis(
        ['time', 'close', 'open', 'high', 'low', 'avarage'],
        axis   = 'columns'
    )
    df['time'] = pd.to_datetime(df['time'], 
    format='%Y/%m/%d %H%M')
    for key in df.columns[1:]:
        df[key] = df[key].astype(float)

    sigmoid = lambda x: 1/(1+np.exp(-x))
    df['log_diff'] = np.log(df.close) - np.log(df.close.shift(1))
    # sigmoid = lambda x: 1/(1+np.exp(x))
    # df.log_diff = sigmoid(df.log_diff)
    df = df.drop(df.index[0])
    return df