def func():
    print('This is func() in one.py')


print('TopLevel in one.py')

if __name__ == '__main__':
    print('one.py run directly')
else:
    print('one.py imported to other module')