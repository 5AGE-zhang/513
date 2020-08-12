#!usr/bin/env python
# -*- coding:utf-8 -*-
# time = 2020-08-12

import pandas as pd

# 读取文件
with open('./My EndNote Library.txt', 'r', encoding='utf-8') as f:
    content = f.readlines()
# 定义存放数据的列表
data = []
# 循环读取标题
for i in range(len(content)):
    # 获取标题词
    title_words = content[i].split(')')[1].split('.')[0].split()
    # 存入列表
    data.extend(title_words)
# 空字典
frequency = {}
# 词频统计
for word in data:
    # 统计词频
    frequency[word] = frequency.get(word, 0) + 1

# 输出词频
top_name = sorted(frequency, key=lambda x: frequency[x], reverse=True)
# 整合列表
frequency = list(zip(top_name, [frequency[i] for i in top_name]))
# 输出
print(frequency)