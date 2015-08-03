#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ==============================================================================
#   Date : 2015-08-02
#   Name : exercise01.py
#   Version : 0.0.1
#   Mail : devfuner@gmail.com
#   Twitter : http://twitter.com/devfuner
# ==============================================================================

import os
from random import shuffle
from memory_profiler import profile


@profile
def init_file(filename):
    with open(filename, 'w') as f:
        for num in unique_list():
            print(num, file=f)


@profile
def unique_list():
    """
    특정 범위의 유니크한 숫자 리스트를 가져오는 함수
    """
    arr = []
    for i in range(1000000, 10000000):
        arr.append(i)
    shuffle(arr)
    return arr


@profile
def check_unique(_list):
    from collections import Counter
    cnts = Counter(_list).most_common()
    for cnt in cnts:
        word, c = cnt
        if c > 1:
            print('ALERT!!!', word)


@profile
def read_file():
    nums = []
    with open('number.txt', 'r') as f:
        for line in f.readlines():
            nums.append(int(line))
    return nums


@profile
def sorted_file(nums):
    with open('sorted.txt', 'w') as f:
        for num in nums:
            print(num, file=f)


if __name__ == '__main__':
    limit = 10000000
    filename = 'number.txt'
    if not os.path.exists(filename):
        init_file(filename, limit)
    nums = read_file()
    nums.sort()
    sorted_file(nums)
