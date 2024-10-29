# class A:
#     def a(self):
#         print('a')


# class B:
#     def a(self):
#         print('b')


# class C(B,A):
#     def c(self):
#         self.a()


# o = C()
# o.c()

# class A:
#     pass


# class B(A):
#     pass


# class C(B):
#     pass


# print(issubclass(C,A))

# class A:
#      def __init__(self):
#         pass


# a = A(1)
# print(hasattr(a,'A'))

# class Ex(Exception):
#     def __init__(self, msg):
#         Exception.__init__(self, msg + msg)
#         self.args = (msg,)


# try:
#     raise Ex('ex')
# except Ex as e:
#     print(e)
# except Exception as e:
#     print(e)

# class A:
#     def __str__(self):
#         return 'a'


# class B(A):
#     def __str__(self):
#         return 'b'


# class C(B):
#     pass
 

# o = C()
# print(o)

# def f(x):
#     try:
#         x = x / x
#     except:
#         print("a",end='')
#     else:
#         print("b",end='')
#     finally:
#         print("c",end='')


# f(1)
# f(0)

# try:
#     raise Exception(1,2,3)
# except Exception as e:
#     print(len(e.args))

# class I:
#     def __init__(self):
#         self.s = 'abc'
#         self.i = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.i == len(self.s):
#             raise StopIteration
#         v = self.s[self.i]
#         self.i += 1
#         return v


# for x in I():
#     print(x,end='')

class A:
    v = 2


class B(A):
    v = 1


class C(B):
    pass


o = C()
print(o.v)




