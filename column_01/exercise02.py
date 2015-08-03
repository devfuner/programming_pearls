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
    def __init__(self, bit):
        self.bit = bit

    def push(self, bit, num):
        n = 0b1 << (num-1)
        if self.pop(bit, num) > 0:
            raise BitVetorException('value exists')
        return bit | n

    def pop(self, bit, num):
        n = 0b1 << (num-1)
        return bit & n

if __name__ == '__main__':
    bitvetor = BitVetor()
    bitvetor.push(0b0111, 4)  # 15
    bitvetor.pop(0b0111, 3)  # 4
    bitvetor.pop(0b0111, 2)  # 2
