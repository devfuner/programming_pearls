#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ==============================================================================
#   Date : 2015-08-03
#   Name : 
#   Version : 0.0.1
#   Mail : devfuner@gmail.com
#   Twitter : http://twitter.com/devfuner
# ==============================================================================


class BitVectorException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value


class BitVector(object):
    BITSPERWORD = 32
    SHIFT = 5
    MASK = 0x1F
    LIMIT = 10000000
    VECTOR = [0 for _ in range(int(LIMIT / BITSPERWORD))]

    def set(self, num):
        self.VECTOR[num >> self.SHIFT] |= (1 << (num & self.MASK))

    def clear(self, num):
        self.VECTOR[num >> self.SHIFT] &= ~(1 << (num & self.MASK))

    def test(self, num):
        return self.VECTOR[num >> self.SHIFT] & (1 << (num & self.MASK))


import os
from random import shuffle
from memory_profiler import profile


def init_file(filename):
    with open(filename, 'w') as f:
        for num in unique_list():
            print(num, file=f)


def unique_list():
    """
    특정 범위의 유니크한 숫자 리스트를 가져오는 함수
    """
    arr = []
    for i in range(1000000, 10000000):
        arr.append(i)
    shuffle(arr)
    return arr


def check_unique(_list):
    from collections import Counter
    cnts = Counter(_list).most_common()
    for cnt in cnts:
        word, c = cnt
        if c > 1:
            print('ALERT!!!', word)


def read_file():
    vector = BitVector()
    with open('number.txt', 'r') as f:
        for line in f.readlines():
            vector.set(int(line))
    return vector


def sorted_file(vector, limit):
    with open('sorted.txt', 'w') as f:
        for i in range(limit):
            if vector.test(i) > 0:
                print(i, file=f)


if __name__ == '__main__':
    limit = 10000000
    filename = 'number.txt'
    if not os.path.exists(filename):
        init_file(filename, limit)
    vector = read_file()
    sorted_file(vector, limit)
