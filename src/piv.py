import pandas as pd

df = pd.DataFrame({
    'r1': [1, 2, 3, 4],
    'r2': [1, 0, 1, 0],
    'c1': [1, 2, 3, 4],
    'c2': [1, 0, 1, 0],
    'v1': [1, 2, 3, 4]
})

pv = pd.pivot_table(data=df, index=['r1', 'r2'], columns=['c1', 'c2'])
print(pv)
print(pv.axes)


pv = pd.pivot_table(data=df, index=['r1', 'r2', 'c1', 'c2'], values=['v1'])
print(pv)
print(pv.axes)
pv = pv.unstack(level=[2, 3])
pv = pv.stack(level=0)
print(pv)
print(pv.axes)
