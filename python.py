# -*-:coding:utf-8 -*-
# 廖雪峰的python2.7教程笔记
# http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000

# 参数
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print calc([1,2,3,4,5,6,7,8,9])
print calc((1,2,3,4,5,6,7,8,9))

# 可变参数
''' 可传入0个或多个参数，会被组装成一个tuple '''
def varcalc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print varcalc(1,2,3,4,5,6,7,8,9)
print varcalc(9)
print varcalc(*[1,2,3])  #传入list和tuple时需要加*号
print varcalc(1, *(1,2)) #传入list和tuple时需要加*号

# 关键字参数
''' 关键字参数会被组装成Dict '''
def person(name, age, **kw):
    print 'name:', name, 'age:', age, 'other', kw
person('Aaron', '23')
person('Aaron', '23', city='Beijing')
person('Aaron', '23', city='Beijing', gender='male')
kw = {'city': 'Beijing', 'job': 'Engineer'}
person('Aaron', '23', **kw)
person('Aaron', '23', **{'city': 'Beijing', 'job': 'Engineer'})

# 参数组合
''' 默认参数，可变参数，关键字组合 '''
def varkw(a, b, c=0, *args, **kw):
    print 'a=', a, 'b=', b, 'c=', c, 'args=', args, 'kw=', kw

varkw(1, 2, c=5)
varkw(1, 2, 5, 'a', 'b')
varkw(1, 2, 5, 'a', 'b', x=99, y=123)
args = (1, 2, 5, 'a', 'b')
kw = {'x': 99, 'y': 123}
varkw(*args, **kw)

# 递归函数
''' f(n) = n! = 1*2*3*...*(n-1)*n = (n-1)!*n = f(n-1)*n '''
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)
print fact(10)
''' fact(1000) 栈溢出，解决递归调用栈溢出的方法是通过 尾递归优化 '''

# 切片
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print [L[0], L[1], L[2]]

# 迭代
''' dict默认迭代key, kw.itervalues()可以迭代value, kw.iteritems()可以迭代key,value '''
for k, v in kw.iteritems():
    print k,v
for v in kw.itervalues():
    print v
for k in kw.iterkeys():
    print k
for ch in 'ABC':
    print ch
for x, y in [(1, 11), (2, 22), (3, 33)]:
    print x, y

''' 判断一个对象是否可以迭代，使用 collections模块的Iterable类型判断 '''
from collections import Iterable
print isinstance('abc', Iterable) #True
print isinstance(123, Iterable) #False
print isinstance([1, 2, 3, 4], Iterable) #True

''' 把list,tuple变成索引-元素 '''
for i, v in enumerate(['a', 'b', 'c']):
    print i, v
for i, v in enumerate(('a', 'b', 'c')):
    print i, v

# 列表生成器
print range(1, 11) #前包含后不包含
print [i * i for i in range(1, 11)]
print [x * x for x in range(1, 11) if x%2 == 0]
print [m + n for m in 'ABC' for n in 'XYZ']

import os
print [d for d in os.listdir('.')] #列出当前目录下所有目录及文件
print [k + '=' + str(v) for k, v in kw.iteritems()]
print [l.lower() for l in L]