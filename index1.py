#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# print(123,'hello','world')
# print(300+100)
# name = input('please enter your name => ')
# print('hello ',name)
# print(1024*768)
# print("'hello \"'")

# print(r'''line
# line
# hello''')

# and or not
# print(True,3>2,3<2)
# print(False)

# age = int(input())
# if age >=21:
#     print('adult')
# else:
#     print('teen')

# print(None)
#
# 2_name = 123
# print(2_name)

# print(10//3)
# 对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符：
# print(ord('A'))
# print(chr(65))
# 以Unicode表示的str通过encode()方法可以编码为指定的bytes，例如：
# Python对bytes类型的数据用带b前缀的单引号或双引号表示：
# print('ABC'.encode('ascii'))
#  b'ABC'
# print(b'ABC'.decode('ascii'))

# 要计算str包含多少个字符，可以用len()函数：
# print(len('abc'))


# %运算符就是用来格式化字符串的。在字符串内部，%s表示用字符串替换，%d表示用整数替换，有几个%?占位符，后面就跟几个变量或者值，顺序要对应好。如果只有一个%?，括号可以省略。
# print('hello ,%s' % 'world')
# print('hi,%s, you have $%d' %('mick',100))

# 用%%来表示一个%：
# print('Age : %d%%.Gender : %s' %(25,True) )

#format()

# print('hello,{0},成绩提升了 {1:.3f}%'.format('小名',17.230) )


#  使用list和tuple

# arr1 = [1,2,3]
# arr1.append('hello')
# arr1.insert(1,'insert')
# arr1.pop(2)
# print(arr1)
# print(len(arr1))

#  但是tuple一旦初始化就不能修改，
# arr2 = (1,23,3)
# arr3 = (1,)
# print(arr2,arr3)

# 条件判断
# age = 3;
# if age<=18:
#     print('teen')
# else :
#     print("old")
#
# if age>=3:
#     print("adult")
# elif age>=6:
#     print("teen")
# else :
#     print("kid")

# birth = int(input("birth : "))
# if birth<2000 :
#     print("00前")
# else :
#     print("00后")

# 循环 一种是for...in循环， 第二种循环是while循环， range()
# sum = 0;
# arr3 = [12,3,4,5,52]
# for item in arr3:
#     sum = sum + item
# print(sum)
#
# arr4 = range(4)
# for item in arr4:
#     print(item)
#

# break continue
# sum5 = 0;
# arr5 = [1,2,3,4,5,6,5]
# lens = len(arr5)
# while lens>=0 :
#     sum5 = sum5+arr5[lens-1]
#     lens = lens -1;
#     break
#     print(lens)
# print(sum5)

# 使用dict和set

# 查找和插入的速度极快，不会随着key的增加而变慢；
# 需要占用大量的内存，内存浪费多。
# dict的key必须是不可变对象。
# obj = {'name' : 'liyang','age' : 123}
# print(obj)
# obj['sex'] = 'male';
# print('sex' in obj)
# print(obj["sex"])
# # obj.pop('sex')
# print(obj['sex'])
# print(obj.get('name',-1))


#  set add remove
# s = set([2,1,2,3,3])
# s.add(56)
# s.remove(2)
# print(s)

# a = ['c','b','a']
# a.sort()
# print(a)

# a = 'abc'
# a.replace('a','S')
# print(a)


# 调用函数
# 绝对值的函数abs
# max()
# print(abs(100))
# print(max(12,3,0))

# 数据类型转换 int float str hex
# print(float('123.12'))
# print(hex(123))

# 定义函数
# 定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用return语句返回
# from abstest import my_abs 导入

# def my_abs(x):
#     if not isinstance(x,(int,float)):
#         raise TypeError('bad operand type')
#     if x>0:
#         return x
#     else:
#         return -x
# print(my_abs('4'))
#
# def nop():
#     pass

# import math
# def move(x,y,step,angle=0):
#     nx = x + step*math.cos(angle)
#     ny = y+step+math.sin(angle)
#     return nx,ny
# # 返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号
# print(move(20,20,4,60))


# 函数的参数
# 一是必选参数在前，默认参数在后
# def power(x,n=2):
#     s = 1
#     while n>0:
#         n = n-1
#         s = s *x
#     return s
# print(power(3))


# 默认参数必须指向不变对象！
# def add_end(l=None):
#     if l is None:
#         l = []
#     l.append('end')
#     return l
# print(add_end())
# print(add_end())

# 定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。
# 在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。
# 但是，调用该函数时，可以传入任意个参数，包括0个参数：

# def calc(number):
#     sum = 0
#     for n in number:
#         sum = sum + n * n
#     return sum
# print(calc([1,2,3]))

# def calc1(*number):
#     sum = 0
#     for n in number:
#         sum = sum + n * n
#     return sum
# # 相当于...
# print(calc1(*[1,2,3]))


# tup = (1,23,3)
# sum = 0;
# for n in tup :
#     sum = sum + n
# print(sum)

# 关键字参数
# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
# 而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
# def person(name,age,**kw):
#     print ('name : ',name,"age : ",age,'other : ',kw)
#
# person("li","25",city = 'beijing',gender="M")

# **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数
# kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。
# extra = {'city' : 'beijing','job':'engineer'}
# person("li","25",**extra)

# 关键字参数 位置参数
# 由于命名关键字参数city具有默认值，调用时，可不传入city参数：
# def person1(name,age,*args,city = "beijingd",job):
#     print(name,age,args,city,job)
# person1('liyang',12,56,job="engeer")



# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，
# 这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

# def f1(a,b,c=0,*args,**kw):
#     print(a,b,c,args,kw)
# f1(1,2,3,4,city = "hello")


# *args是可变参数，args接收的是一个tuple；
#
# **kw是关键字参数，kw接收的是一个dict。
# 可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
#
# 关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。


# 递归函数
# 递归函数需要注意防止栈溢出。在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，
# 每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出
# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n-1)
# print(fact(10))

# 尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式
# 要改成尾递归方式，需要多一点代码，主要是要把每一步的乘积传入到递归函数中：
# def fact1(n):
#     return fact_iter(n,1)

# 大多数编程语言没有针对尾递归做优化，Python解释器也没有做优化，所以，即使把上面的fact(n)函数改成尾递归方式，也会导致栈溢出。
# def fact_iter(num,product):
#     if num == 1:
#         return product
#     return fact_iter(num-1,num * product)



# 切片

# 1.切片（Slice）操作符
# L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# print(L[0:3])
# print(L[:3])
# print(L[-2:])
# print(L[-2:-1])

# L = list(range(100))
# print(L[:10:2])
# print(L[::5])
# print(L[:2])
# # 2.字符串'xxx'也可以看成是一种list，
# print('ABCDEF'[:2])


#  迭代
# d = {"a":1,"b":2}
# for i in d.items() :
#     print(i)


# d = {"a":1,"b":2}
# for i,k in d.items() :
#     print(i,k)

# 如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断：
# from collections import Iterable
#
# print(isinstance('abc',Iterable))

# Python内置的enumerate函数可以把一个list变成索引-元素对

# for i,v in enumerate(['a','b']):
#     print(i,v)

# tup = ('3','3')
# print(tup)
# for i,v,k in [(1,2,2),(3,5,8),(4,6,8)]:
#     print(i,v,k)

#列表生成式 把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来
# print([x * x for x in range(1,11)])
# # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#
# print([x * x for x in range(1,11) if x%2==0])
#
#
# print([m+n for m in 'ABC' for n in 'xyz'])


# import os
# print(d for d in os.listdir(','))

# d = {'x':'1','y':'2'}
# print([k + '='+ v for k,v in d.items()])


#
# 生成器

# 通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。
# 而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。

# 所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，
# 从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。

# L = [x *x for x in range(10)]
# print(L)
#
# g = (x*x for x in range(10))
#
# for n in g:
#     print(n)

# 函数是顺序执行，遇到return语句或者最后一行函数语句就返回。而变成generator的函数，
# 在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。

# def fib(max):
#     n,a,b = 0,0,1
#     while n<max:
#         yield b
#         a,b = b,a+b
#         n = n +1
# g = fib(6)
#
# for n in g:
#     print(n)

# def odd(x):
#     print('step 1')
#     yield x+1
#     print('step 2')
#     yield(x+3)
#     print('step 3')
#     yield(5+x)
#
# o = odd(5)
# print(next(o))
# print(next(o))
# print(next(o))

# 我们已经知道，可以直接作用于for循环的数据类型有以下几种：
#
# 一类是集合数据类型，如list、tuple、dict、set、str等；
#
# 一类是generator，包括生成器和带yield的generator function。
#
# 这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。
#
# 可以使用isinstance()判断一个对象是否是Iterable对象：

from collections import Iterator

print(isinstance([], Iterator))
# print(isinstance({},Iterable))


# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。


# 把list、dict、str等Iterable变成Iterator可以使用iter()函数：



















