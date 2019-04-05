import pandas as pd
import numpy as np


i1 = pd.Index([1, 1, 1, 2])
i2 = pd.Index([2, 2, 3, 4, 5, 6])

i_u = i1.union(i2)

print(i_u)

i1 = pd.CategoricalIndex(["1", "1", "1", "2"], ["1", "2"])
i2 = pd.CategoricalIndex(["2", "2", "3", "4", "5", "6"], ["2", "3", "4", "5", "6"])

i_u = i1.union(i2)

print(i_u)

exit(0)

s1 = pd.Series([39, 6], index=pd.CategoricalIndex(['female','male']))
s2 = pd.Series([2, 152, 2], index=pd.CategoricalIndex(['female', 'male','unknown']))
df = pd.DataFrame([s1,s2])

print(s1)
print(s2)
print(df)

exit(0)

# df = pd.DataFrame([[1, 2], [2, 2], [3.3, 4.4]])
df = pd.DataFrame([[1], [2], [3.3]])

grp = df.groupby([1,1,1]) #.agg(len)

for g, k in grp:
    print(g)
    print(k)


print(df)
print(grp.agg('idxmin'))

exit(1)

df = pd.DataFrame({'name': ['A', 'A', 'B', 'B'],
                    'c_int': [1, 2, 3, 4],
                    'c_float': [4.02, 3.03, 2.04, 1.05],
                    'c_date': ['2019', '2018', '2016', '2017']},
                    index=["a", "b", "c", "d"])
df['c_date'] = pd.to_datetime(df['c_date'])
print(df.groupby('name').idxmax())

exit()



rng = pd.date_range('1/1/2011', periods=15, freq='D') 
np.random.seed(4)

stocks = pd.DataFrame({ 
    'price':(np.random.randn(15).cumsum() + 10) },index = rng)

stocks['week_id'] = pd.to_datetime(stocks.index).week #used for the groupby
print (stocks)
print("xxxxx")
x = stocks.groupby('week_id')['price']

for a, b in x:
    print(a)
    print(b)

print(x.transform('idxmax'))

print (stocks.groupby(stocks['week_id'])['price'].transform('idxmax'))
exit(0)

import pandas as pd
fname = 'foo.csv'

sample_data = '''clientid,datetime
A,2017-02-01 00:00:00
B,2017-02-01 00:00:00
C,2017-02-01 00:00:00'''
open(fname, 'w').write(sample_data)

df = pd.read_csv(fname)
df['datetime'] = pd.to_datetime(df.datetime)
df['time_delta_zero'] = df.datetime - df.datetime
# Next line fails w error message below
print(df.groupby('clientid').apply(
	lambda ddf: pd.Series(dict(
		clientid_age = ddf.time_delta_zero.min(),
		date = ddf.datetime.min()
		))
	))
exit(0)

# df = pd.DataFrame({'a': range(10), 'b': range(10)})

# df.to_hdf('/tmp/1.hdf', 'k1')
# try:
#     pd.read_hdf('/tmp/1.hdf', 'k2')
# except Exception as e:
#     print(type(e))
#     print(e)
    
# df.to_hdf('/tmp/1.hdf', 'k2')
# df1 = pd.read_hdf('/tmp/1.hdf', 'k2')
# print(df1)

# exit(0)




# df1 = pd.DataFrame({'key': [1, 2], 'value': [0, 1]})
# df2 = pd.DataFrame({'key': [1.0, 3.0], 'other_value': ['A', 'B']})

# print(df1.dtypes)
# print(df2.dtypes)
# print(pd.merge(df1, df2, how='left', on='key').dtypes)
# print(pd.merge(df1, df2, how='left', on='key'))

df = pd.DataFrame({'name': ['A', 'A', 'A', 'B', 'B'], 
                   'int':[1, 2, 3, 4, 5], 
                   'float':[5.01, 4.02, 3.03, 2.04, 1.05], 
                #    'date': ['2016', '2019', '2018', '2016', '2017']
                    })
# df['date'] = pd.to_datetime(df['date'])

import numpy as np
#current behaviour

p = df.groupby('name').idxmin()
x = p["int"].dtype
print(df.groupby('name').idxmin())
# print(df.groupby('name').aggregate('idxmin', 'idxmax'))