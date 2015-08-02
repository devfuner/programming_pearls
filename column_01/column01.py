#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ==============================================================================
#   Date : 2015-08-02
#   Name : 
#   Version : 0.0.1
#   Mail : devfuner@gmail.com
#   Twitter : http://twitter.com/devfuner
# ==============================================================================
#   문제 : 디스크 파일을 어떻게 정렬 하는가?
#   요구사항 :
#       입력 : 최대 n개의 양의 정수를 포함하는 파일로, 각 숫자는 n보다 작고,
#             n=10의 7승이다. 어떤 숫자가 두 번 이상 나오는 것은 치명적 에러이다.
#             정수 이외에 관련된 데이터는 없다.
#       출력 : 입력된 정수를 오름차순으로 정렬한 리스트
#       제약조건 : 메모리를 많아야 대략 1MB 정도를 사용할 수 있고, 디스크 공간은
#                충분하다. 실행시간은 최대 몇 분 정도가 될 수 있고, 10초 정도 안
#                에 작업을 끝낼 수 있으면 충분하다.
# ==============================================================================

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
    nums = []
    with open('number.txt', 'r') as f:
        for line in f.readlines():
            nums.append(int(line))
    return nums


def bit_sort(_list, limit):
    b = []
    for i in range(limit):
        b.append(0)

    for i in _list:
        b[i] = 1
    return b


def sorted_file(nums):
    with open('sorted.txt', 'w') as f:
        for idx, flag in enumerate(nums):
            if flag == 1:
                print(idx, file=f)


if __name__ == '__main__':
    limit = 10000000
    filename = 'number.txt'
    if not os.path.exists(filename):
        init_file(filename, limit)
    nums = read_file()
    sorted_nums = bit_sort(nums, limit)
    sorted_file(sorted_nums)
