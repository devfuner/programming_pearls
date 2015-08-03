#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ==============================================================================
#   Date : 2015-08-03
#   Name : 
#   Version : 0.0.1
#   Mail : devfuner@gmail.com
#   Twitter : http://twitter.com/devfuner
# ==============================================================================


class BitVetorException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value


class BitVetor(object):
    def __init__(self, vetor=0b0):
        self.vetor = vetor

    def add(self, num):
        n = 0b1 << (num-1)
        if self.get(num) > 0:
            raise BitVetorException('value exists')
        self.vetor = self.vetor | n
        return self.vetor

    def get(self, num):
        n = 0b1 << (num-1)
        return self.vetor & n

    def clear(self):
        self.vetor = 0b0

if __name__ == '__main__':
    b = BitVetor()
    b.add(3)  # 4
    b.get(3)  # 4
    b.clear()  # 0