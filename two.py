import one

print('TopLevel in two.py')
one.func()

if __name__ == '__main__':
    print('two.py Run directly')
else:
    print('two.py imported by anther module')