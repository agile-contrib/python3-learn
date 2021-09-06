#!/usr/bin/python3

# 基础语法

# 【1】注释

# 第一个注释
# 第二个注释

'''
第三注释
第四注释
'''

"""
第五注释
第六注释
"""

# 【2】行与缩进

# 使用缩进来表示代码块，不需要使用大括号 {}

# 【3】多行语句

# 如果语句很长，我们可以使用反斜杠 \ 来实现多行语句

item_one = 1
item_two = 2
item_three = 3
total = item_one + \
    item_two + \
    item_three

# 打印一下
print(total)

# 在 [], {}, 或 () 中的多行语句，不需要使用反斜杠 \

total2 = ['item_one', 'item_two', 'item_three',
          'item_four', 'item_five']

print(total2)

# 【4】数字(Number)类型

# python中数字有四种类型：整数、布尔型、浮点数和复数

number1 = 1
number2 = True
number3 = 1.23
number4 = 1.1 + 2.2j

print(number1, number2, number3, number4)

# 【5】字符串(String)

# 单引号和双引号使用完全相同
# 使用三引号(''' 或 """)可以指定一个多行字符串

str1 = '我是一个字符串'
str2 = '''我是第一行
        我是第二行
        我是最后一行'''
print(str1, str2)

# 【6】等待用户输入

yourInput = input("\n\n[温馨提示]你可以输入一段内容后回车: ")
print(yourInput)

# 【7】同一行显示多条语句

# 语句之间使用分号 ; 分割，例如：
# val1 = "前置名称";val2 = "后置名称"
# print(val1+"-"+val2)

# 【8】print 输出

# print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=""：

x = "a"
y = "b"
# 换行输出
print(x)
print(y)

print('---------')
# 不换行输出
print(x, end=" ")
print(y, end=" ")
print()


