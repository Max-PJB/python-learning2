p = r'./1126.txt'
with open(p, 'r') as f:
    k = f.readlines()
start = 4
s = list(map(lambda x: x.split(), k[4:]))
print(s)


import pandas as pd
ss = pd.DataFrame(s)
pd.set_option('display.max_columns',50)
# pd.set_option('display.width',1000)
print(ss.loc[0:2])
ss.to_excel('hh.xlsx')