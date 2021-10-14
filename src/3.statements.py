#!/usr/bin/python3

# 语句

# 【1】if

if_flag = 10

if if_flag == 5:
    print('值等于5')
elif if_flag == 10:
    print('值等于10')
else:
    print('不是5和10')

# 【2】while

while_flag = 1
while(while_flag < 10):
    print(while_flag)
    while_flag += 1

while(while_flag < 20):

    # 拼接的时候，需要先把数字转成字符串类型
    print('第二块打印：'+str(while_flag))
    while_flag += 3
else:
    print('不小于20了')

# 【3】for

# datas = ['你好2007', 'hai2007', 2007, 2021]
# datas = ('你好2007', 'hai2007', 2007, 2021)
# datas = {'你好2007', 'hai2007'}
datas = {
    'mark': '这是一个字典',
    'name': '你好2007',
    'date': '2007 ~ 2021'
}
for item in datas:
    print(item)

'''
range()函数
'''

# 【4】函数


def doit(mark):
    print('信息是：'+str(mark))


doit(1)
