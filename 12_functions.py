from functools import reduce


def sum(a, b):
    c = a + b
    return (c)


print(sum(30, 40))

ans = (lambda z: z*2)
print(ans(7))

items = [1, 2, 3, 4]
sqr = list(map(lambda x: x**3, items))
print(sqr)

num_list = [-5, 5]
less_than_zero = list(filter(lambda z: z < 0, num_list))
print(less_than_zero)

ls = [1, 2, 3, 4]
product = reduce((lambda x, y: x*y), ls)
print(product)


def Welcome(str):
    print('Welcome to ', str)
    return()


Welcome('Physics')
Welcome(str='Chemistry')


def info(name, age=50):
    print('Name: %s' % name)
    print('Age: %d' % age)
    return ()


info('Sanket')
info(name='Sarode')
info('Sanket', 20)
info(name='Rahul', age=25)


def Users(*users):
    for user in users:
        print(user)
    return()


Users('Sanket')
Users('Sanket', 'Sarode')
Users('Rahul', 'Tushar', 'Sanket')


def multiArg(agr1, arg2, arg3, *arg, **args):
    print("1st Arg: ", agr1)
    print("2nd Arg: ", arg2)
    print('3rd Arg: ', arg3)
    print('4th Non-Keyworded Arg: ', arg)
    print('Keyword Arg: ', args)


multiArg(1, 2, 3, 4, 5, 6, 7, name='Sanket', age='20', course='python')