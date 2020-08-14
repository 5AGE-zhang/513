#!usr/bin/env python3
# -*- coding:utf-8 -*-
# time = 2020-08-14
# author = zhang xujun

def cal_frequency(data_list):
    # 空字典
    frequency_dic = {}
    # 计算频率
    for data in data_list:
        frequency_dic[data] = frequency_dic.get(data, 0) + 1
    #
    return frequency_dic
