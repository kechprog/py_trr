import numpy as np
import pandas as pd

def parse_txt():
    FILE = './RI_5min.txt'
    #FORMAT:close, open, high, low, avarage
    data = []
    with open(FILE) as f:
        for l in f.readlines():
            e = l.replace(' ', '').replace('\n','').split(',')
            e.pop(0)
            e.pop(0)
            data.append(e)
            
    
    df = pd.DataFrame(data)
    df = df.set_axis(
        ['close', 'open', 'high', 'low', 'avarage'],
        axis   = 'columns'
    )
    for key in df.columns:
        df[key] = df[key].astype(float)

    df['log_diff'] = np.log(df.close) - np.log(df.close.shift(1))
    df = df.drop(df.index[0])
    return df