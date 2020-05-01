import pandas as ps
import numpy as np

# series

series = ps.Series([5], dtype=int)
print(series)

arr = np.array([28, 37, 34, 56, 57, 32])
series = ps.Series(arr)
print(series)

dict_ = {'a': 1, 'b': 2, 'c': 3}
series = ps.Series(dict_)
print(series)

print(series[1:4])  # slicing the series
print(series[1:])
print(series[:2])
print(series[1])
print(series[2])
print(series[0])
print(series[-1])
print(series[-2])
print(series[-3])

# DataFrames

lists = [1, 2, 3, 4]
dataframes = ps.DataFrame(lists)
print(dataframes)

lists = [{'a': 20, 'b': 30}, {'a': 40, 'b': 50}, {'a': 12, 'b': 22}]
dataframes = ps.DataFrame(lists)
print(dataframes)

dataframes = ps.DataFrame(lists, index=['row-1', 'row-2', 'row-3'])
print(dataframes)

# using series to create dataframes

series1 = ps.Series([40, 50, 60], index=['maths', 'physics', 'chemist'])
series2 = ps.Series([70, 20, 90], index=['maths', 'physics', 'chemist'])

dataframes = ps.DataFrame(
    {
        'Jim': series1,
        'Penny': series2
    }
)
print(dataframes)

# adding a column to the dataframes:

dataframes['John'] = ps.Series(
    [60, 50, 10], index=['maths', 'physics', 'chemist'])
print(dataframes)

# deleting a column from dataframes

del(dataframes['Jim'])
# del doesn't return any thing

print(dataframes)

# pop returns the deleted item from the dataframes
print(dataframes.pop('John'))
print(dataframes)

dataframes['John'] = ps.Series(
    [40, 50, 60], index=['maths', 'physics', 'chemist'])
dataframes['Jim'] = ps.Series(
    [70, 20, 90], index=['maths', 'physics', 'chemist'])

print(dataframes.loc['maths'])  # prints maths results for all
print(dataframes.iloc[1])  # prints maths results for all

# adding row to the dataframes

print(dataframes)
row = ps.DataFrame([[10, 20, 30]], columns=[
                   'Penny', 'John', 'Jim'], index=['history'])
dataframes = dataframes.append(row)
print(dataframes)

# reading and writing to files

dataframes.to_csv('pandas.csv')

print(ps.read_csv('pandas.csv'))