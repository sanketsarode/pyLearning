class edureka():
    '''
    This is a class with function to present hello func
    '''

    def Hello(self):
        print('Inside hello func')
        return ()


ob = edureka()
ob.Hello()

# These are the built-in class attributes
print('Edureka.__dict__: ', edureka.__dict__)
print('Edureka.__doc__: ', edureka.__doc__)
print('Edureka.__name__: ', edureka.__name__)
print('Edureka.__module__: ', edureka.__module__)
print('Edureka.__bases__: ', edureka.__bases__)


class Attr():
    def __init__(self):
        self.__private = ('I am Private')
        self._protected = ('I am protected')
        self.public = ('I am public')

        print(self.__private)

    @classmethod
    def myInit(cls):
        print('I am inside my init method')


ob = Attr()
print(ob.public)
# protected can be accessed outside, python is relaxed language
print(ob._protected)
# print(ob.__private) AttributeError: 'Attr' object has no attribute '__private'
myobj = Attr().myInit()

# The private protected and public are applicable to the methods as well


class Edu():
    def _protected(self):
        print('This is inside protected method')
        return ()

    def public(self):
        print('This is inside public method')
        return()

    def __private(self):
        print('This is inside private method')
        return ()

    def callPrivate(self):
        print('Calling Private Method From Other method of class')
        self.__private()


ob = Edu()
ob._protected()
ob.public()
# ob.__private() AttributeError: 'Edu' object has no attribute '__private'
ob.callPrivate()

#Constructor and Destructor


class Testcase:
    def __init__(self):
        print('this is constructor')

    def __del__(self):
        print('this is destructor')


if __name__ == '__main__':
    ob = Testcase()
    del ob

# single inheritance


class base1:
    def func(self):
        print('In superclass func')


class sub(base1):
    def xyz(self):
        print('In subclass xyz')


ob = sub()
ob.func()
ob.xyz()

obj = base1()
obj.func()
# obj.xyz() AttributeError: 'base1' object has no attribute 'xyz'

# multiple inheritance


class First:
    def __init__(self):
        super(First, self).__init__()
        print('First')


class Second:
    def __init__(self):
        super(Second, self).__init__()
        print('Second')


class Third(Second, First):
    def __init__(self):
        super(Third, self).__init__()
        print('Third')


Third()


# multilevel inheritance

class Animal:
    def eat(self):
        print('Eating...')


class Dog(Animal):
    def bark(self):
        print('Barking...')


class BabyDog(Dog):
    def weep(self):
        print('Weeping...')


ob = BabyDog()
ob.eat()
ob.bark()
ob.weep()

# Polymorphism


class Animals:
    def __init(self, name):
        self.name = name

    def talk(self):
        pass


class Cats(Animals):
    def talk(self):
        print('Meow')


class Dogs(Animals):
    def talk(self):
        print('Woof')


c = Cats()
c.talk()

d = Dogs()
d.talk()