#!/usr/bin/python3

# 数据类型

# 【1】多个变量赋值
a = b = c = 1
d, e, f = 1, 2, '数据'

# print(a,b,c)
# print(d,e,f)

# 【2】标准数据类型

'''
不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。

辅助理解：
List       -> 数组
Dictionary -> JSON
'''

# 【3】数字

'''
整型(int)

浮点型(float)
浮点型由整数部分与小数部分组成，浮点型也可以使用科学计数法表示（2.5e2 = 2.5 x 102 = 250）

复数( (complex))
复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型
'''

# 【4】字符串

'''
索引值以 0 为开始值，-1 为从末尾的开始位置
（这在别的数据类型中也适用）
'''

# 【5】列表

listdemo = ['你好2007', 'hai2007', 2007, 2021]
print(listdemo[1])

# 【6】元组

tupledemo = ('你好2007', 'hai2007', 2007, 2021)
print(tupledemo[0])

# 【7】字典

dictionarydemo = {
    'mark': '这是一个字典',
    'name': '你好2007',
    'date': '2007 ~ 2021'
}

print(dictionarydemo['mark'])

# 【8】集合

setdemo = {'你好2007', 'hai2007'}

# 判断是否在集合中
print('hai2007' in setdemo)
