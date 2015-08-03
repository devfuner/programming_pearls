#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ==============================================================================
#   Date : 2015-08-04
#   Name : exercise04
#   Version : 0.0.1
#   Mail : devfuner@gmail.com
#   Twitter : http://twitter.com/devfuner
# ==============================================================================
# 0부터 n-1 사이의 k개의 정수를 랜덤한 순서로 가지는 파일을 만들 수 있겠는가?
# 가능한 짧고 효율적인 프로그램을 작성해보라.
# n = 10000000
# k = 1000

import random
from memory_profiler import profile


def random_items():
    n = 10000000
    k = 1000
    return random.sample(range(n), k)


def check_unique(_list):
    from collections import Counter
    cnts = Counter(_list).most_common()
    for cnt in cnts:
        word, c = cnt
        if c > 1:
            print('ALERT!!!', word)


if __name__ == '__main__':
    items = random_items()
    check_unique(items)
