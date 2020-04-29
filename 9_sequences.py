list123 = ['1', 3, 'Sanket']

print(list123[1])
print(list123[0:2])
print(list123[-1])  # last element

print(list123 + ['2', 5, 'Sarode'])
print(list123 * 3)
print('Sanket' in list123)

del(list123[0])
print(list123)

list123 = ['1', 3, 'Sanket']

print(list123.pop(2))  # pop will return the element being removed
print(list123)

list123 = ['1', 3, 'Sanket']
print(list123.remove('1'))  # remove won't return the element being removed
print(list123)

print(type(list123))
print([x**2 for x in [1, 2, 3]])

list123 = [1, 2, 3]
list123.append(['Machine Learning', 'ss'])
print(list123)

list123.extend(['g', 's'])
print(list123)

list123.insert(1, 'Sanket')
print(list123)

list123 = ['sanket', 'is', 'learning', 'python']
list123.sort()
print(list123)

print(sorted(list123))
print(list123[::-1])

tup = ('Sanket', 'raj', 'Abc', 'ZXY')  # based on ascii value
print(tup)
print(len(tup))
print(min(tup))
print(max(tup))

tup = ('Sanket', 'Raj', 'Abc', 'ZXY')  # based on ascii value
print(tup)
print(len(tup))
print(min(tup))
print(max(tup))

'''
tup = ('Sanket', 'raj', 'Abc', 'ZXY', 6)
print(tup)
print(len(tup))
print(min(tup))
print(max(tup))
output:
Traceback (most recent call last):
  File "D:\Study\Python\sequences.py", line 58, in <module>
    print(min(tup))
TypeError: '<' not supported between instances of 'int' and 'str
'''

# convert tupe to list123 and vice versa
tupe = (2, 3, 4)
s = list(tupe)
print(s)

s[1] = 'Sanket'

tupe = tuple(s)
print(tupe)

# string
str1 = """Sanket"""
print(str1[0])
print(str1)
print(len(str1))
print(str1[1:3])
print('t' in str1)

print("Welcome %s. Have a nice day!" % (str1))

str1 = "news"
print(str1.capitalize())
print(str1.count("w", 0, len(str1)))

s = str1.encode('utf-8', 'strict')
print(s)

print(str1.replace('e', '--E--', 1))
print(str1.upper())

print(str1.index('s'))

print(str1[::-1])
print(str1[0:1])
print(str1.find('s'))

print(str1*2)

# Sets

A = {1, 2, 3}
B = {3, 4, 5}
a = set('Welcome')
print(A)
print(a)
# union of two sets
print(A | B)
print(A - B)
print(A & B)

print(A.union(B))
print(A.intersection(B))
print(A.difference(B))
print(A.symmetric_difference(B))

C = {1, 2}
print(B.issubset(A))
print(C.issubset(A))
print(A.issuperset(C))

print(1 in C)
print(9 not in C)

C.add('A')
print(C)
print(C.remove('A'))
print(C)
C.add('A')
print(C.discard('A'))
print(C)
C.add('A')
print(C.pop())
print(C)
C.clear()
print(C)

# dict
dict = {1: "Python", 2: "Android"}
print(dict)
print(dict[1])

dict[1] = 'Windows'
print(dict)

del(dict[2])
print(dict)
print(len(dict))
print(str(dict))
print(type(dict))

dict = {'name': 'sanket', 'age': '20'}
print(dict.get('name'))
print(sorted(dict))
print(dict.items())
print(dict.values())
print(dict.keys())
print(dict.setdefault(1, 4))

print(dict[1])

print(dict.copy())
dict.clear()
print(dict)