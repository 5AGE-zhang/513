#!usr/bin/env python3
# -*- coding:utf-8 -*-
# time = 2020-08-14
# author = zhang xujun
# used for t test

from scipy import stats


def t_test(data1, data2):
    # 判断两个样本总体方差是否相同
    if stats.levene(data1, data2)[1] > 0.05:
        # 方差相同
        p = stats.ttest_ind(data1, data2, equal_var=True)[1]
    else:
        # 方差不同
        p = stats.ttest_ind(data1, data2, equal_var=False)[1]
