"""
格式化输出

Version: 0.1
Author: 骆昊
Date: 2018-02-27
"""

a = int(input('a = '))
b = int(input('b = '))
print('%d + %d = %d' % (a, b, a + b))
print('%d - %d = %d' % (a, b, a - b))
print('%d * %d = %d' % (a, b, a * b))
print('%d / %d = %f' % (a, b, a / b))
print('%d // %d = %d' % (a, b, a // b))
print('%d %% %d = %d' % (a, b, a % b))
print('%d ** %d = %d' % (a, b, a ** b))

#f - format - 格式化字符串
print(f'{a1} + {b2} = {a1 + b2 }')
#print(f'{a1} + {b2} = {a1 + b2:.2f }') 如果想保留n位就添加 ：.nf 即可
print(f'{a1} - {b2} = {a1 - b2 }')
print(f'{a1} * {b2} = {a1 * b2 }')
print(f'{a1} / {b2} = {a1 / b2 }')

#坑点1 print（0.1+0.2）不等于0.3
#print（0.1+0.2+0.3）不等于0.6
#print（0.3+0.2+0.1）等于0.6
#坑点2 ，后面和运算符+-*/后面要加空格 pycharm--->code-->reformat code 可以帮助规范没有打空格的地方
