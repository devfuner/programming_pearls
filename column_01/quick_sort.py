#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ==============================================================================
#   Date : 2015-08-02
#   Name : quick_sort
#   Version : 0.0.1
#   Mail : devfuner@gmail.com
#   Twitter : http://twitter.com/devfuner
# ==============================================================================


def quick_sort(_list):
    _len = len(_list)
    if _len <= 1:
        return _list
    pivot = _list[_len//2]

    less = []
    greator = []
    equal = []
    for i in _list:
        if i < pivot:
            less.append(i)
        elif i > pivot:
            greator.append(i)
        else:
            equal.append(i)

    return quick_sort(less) + equal + quick_sort(greator)
