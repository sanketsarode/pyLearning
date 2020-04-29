# import math # same as from math import *
# dir gives the list of variables and function defined in side the ()
# print(dir(math))

import re
import json
import datetime
import random
import math
import os
import sys
from math import sqrt
print(dir())

'''
Sys
Os
Math
DateTime
Random
Json
'''

print(sys.argv)
# print(sys.exit())
# print(not sys)
print(sys.winver)
print(sys.flags)
print(sys.prefix)

print(os.name)
print(os.environ)
print(os.getlogin())
print(os.getppid())

print(os.getcwd())
# print(os.chdir('D:/Softwares'))
print(os.mkdir('D:/Softwares/viaPython'))
print(os.mkdir('D:/Softwares/Sanket'))
# print(os.rmdir('D:/Softwares/viaPython'))
# print(os.path.normpath('D:\Softwares\Sanket'))

# os.path
print(os.path.join('D:/Softwares/viaPython', 'D:/Softwares/Sanket'))

print(os.path.abspath('14_modules.py'))
print(os.path.normpath("D:/Softwares/Sanket"))

print(os.rmdir('D:/Softwares/viaPython'))
print(os.rmdir('D:/Softwares/Sanket'))

print(os.path.split('D:/Study/Python/14_modules.py'))
print(os.path.exists('14_modules.py'))
print(os.path.isdir('D:/Study/Python'))
print(os.walk('D:/Study/Python'))

# math
print(math.ceil(10.98))
print(math.copysign(10, -1.5))
print(math.fabs(-15.5))
print(math.exp(5))      # returns e**x
print(math.expm1(2))    # returns e**x-1
print(math.log(10, 10))
print(math.acos(0.5))
print(math.asin(0.5))
print(math.atan(5))
print(math.cos(3))
print(math.sin(2))
print(math.tan(4))
print(math.degrees(0.1))
print(math.radians(5))
print(math.pi)
print(math.e)

# random module
num = random.randrange(100)
print(num)

num = random.randrange(0, 100, 20)
print(num)

num = random.randint(0, 30)
print(num)

print(random.getstate)
print(random.uniform(6, 5))


# datetime module

print(datetime.datetime.today())

now = datetime.datetime.today()
then = datetime.datetime(1990, 9, 23)
print(now - then)

then = datetime.timedelta(18901, 55547, 421000)
print(now - then)

print(datetime.MAXYEAR)
print(datetime.MINYEAR)
print(datetime.time)
print(datetime.timezone)

# JSON module

data = {'name': 'Sanket', 'age': 20, 'depart': 'science'}
jsonstr = json.dumps(data)  # this is no special, it just converts dict to str
print(jsonstr)
print(type(jsonstr))

# Regular Expressions:

print(re.sub(r'ab', '*', 'abce deabe edrtab'))
print(re.sub(r'[ae]', '*', 'abce deabe edrtab'))
print(re.sub('[ae]', '*', 'abce deabe edrtab'))
print(re.sub('[abc][123]', '*', 'a1=b2=b3=d4'))
print(re.sub('[abc][123]', '*', 'az1=b2=b3=d4'))
print(re.sub('A.B', '*', 'A2B AXB AXXB A$B'))
print(re.sub('AB+', '*', 'ABC ABBBBBC AC'))
print(re.sub('AB{3,6}', '*', 'AB ABB ABBBB ABBBBBBB'))
print(re.sub('^abc', '*', 'abcdefghiabc'))
print(re.sub('abc$', '*', 'abcdefghiabc'))
print(re.sub('AB\+', '*', 'AB+C'))
print(re.sub('\d', '*', '3+17=20'))
print(re.sub('\D', '*', '3+17=20'))
print(re.sub('\w', '*', 'this is a test Or is it?'))
print(re.sub('\W', '*', 'this is a test Or is it?'))
print(re.sub('\s', '*', 'this is a test Or is it?'))
print(re.sub('\S', '*', 'this is a test Or is it?'))
print(re.sub('the(?= cat)', '*', 'the dog and the cat'))
print(re.sub('(?<=)the', '*', 'Athens is the captial'))
print(re.sub('(?<!\w)[Tt]he(?!\w)', '*', 'the cat is on the latte there.'))
print(re.sub('(?i)ab', '*', 'ab AB'))

print(re.search('ab', 'I am the absolute'))  # search anywhere in the sentence

# search only at the beginning of the word in a sentence
print(re.match('ab', 'ab I am the absolute'))