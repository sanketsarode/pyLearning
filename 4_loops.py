# while, For, Nested
'''
while condition:
    expression
'''

count = 0
while(count < 5):
    count += 1
    print(count)
print("Good Bye")

'''
for <variable> in <range>:
    stmt1
    stmt2
'''

fruits = ['banana', 'apple', 'grapes']
cars = {'maruti', 'tata', 'ferrari'}
bikes = {'hero': 'xblade', 'bajaj': 'dominar', 'yamaha': 'fz'}

for item in fruits:
    print(item)

for car in cars:
    print(car)

for bike in bikes:
    print(bike)

# break, continue, pass; pass is used when a stmt is required syntactically

for bike in bikes:
    pass