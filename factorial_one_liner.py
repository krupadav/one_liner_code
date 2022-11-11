# factorial of a number
from functools import reduce

num = int(input('Enter a number:'))
factorial = lambda num: reduce(lambda x, y: x * y, range(1, num + 1))
print('%d != %d' % (num, factorial(num)))
print('Method two')
factorial = reduce(lambda x, y: x * y, range(1, num + 1))
print('%d != %d' % (num, factorial))
print('Method three')
fact = lambda n: 1 if n <= 1 else n * fact(n - 1)
print('%d != %d' % (num, fact(num)))
