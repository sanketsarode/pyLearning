# identify operators:
print(5 is 5)
print(4 is not 3)

a = 1
b = 2
print(a is b)
print(a is not b)

# Membership operator: 'contains'
# applied to list, tuples, dict

A = [1, 2, 3, "edureka!"]
print("edureka!" in A)
print(5 in A)

A = {1, 2, 3, 3, "edureka!"}
print(3 in A)

#in dict we check the key is present or not and not the value in it.
A = {"Age": 24, "Name": "John"}
print(30 in A)
print(24 in A)
print("Age" in A)