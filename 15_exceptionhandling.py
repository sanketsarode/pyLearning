try:
    a = b/0
except:
    print('divide by zero exception')
finally:
    print('try again')


class Error (Exception):
    pass


class ValueGreaterThanFive(Error):
    pass


class ValueLessThanFive(Error):
    pass


try:
    num = int(input('Enter num: '))
    if num > 5:
        raise ValueGreaterThanFive
    elif num < 5:
        raise ValueLessThanFive
except ValueGreaterThanFive:
    print('Value is greater than 5')
except ValueLessThanFive:
    print('Value is less than 5')
finally:
    print('bye')
