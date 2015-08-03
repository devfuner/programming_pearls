```
devfunerui-MacBook-Air:column_01 devfuner$ python -m memory_profiler column01.py
Filename: column01.py

Line #    Mem usage    Increment   Line Contents
================================================
    56     10.2 MiB      0.0 MiB   @profile
    57                             def read_file():
    58     10.2 MiB      0.0 MiB       nums = []
    59     10.2 MiB      0.0 MiB       with open('number.txt', 'r') as f:
    60    444.3 MiB    434.1 MiB           for line in f.readlines():
    61    444.3 MiB      0.0 MiB               nums.append(int(line))
    62     50.5 MiB   -393.8 MiB       return nums


Filename: column01.py

Line #    Mem usage    Increment   Line Contents
================================================
    65    357.5 MiB      0.0 MiB   @profile
    66                             def bit_sort(_list, limit):
    67    357.5 MiB      0.0 MiB       b = []
    68    369.3 MiB     11.8 MiB       for i in range(limit):
    69    369.3 MiB      0.0 MiB           b.append(0)
    70
    71    378.8 MiB      9.5 MiB       for i in _list:
    72    378.8 MiB      0.0 MiB           b[i] = 1
    73    378.8 MiB      0.0 MiB       return b


Filename: column01.py

Line #    Mem usage    Increment   Line Contents
================================================
    76    379.7 MiB      0.0 MiB   @profile
    77                             def sorted_file(nums):
    78    379.9 MiB      0.2 MiB       with open('sorted.txt', 'w') as f:
    79    388.0 MiB      8.1 MiB           for idx, flag in enumerate(nums):
    80    388.0 MiB      0.0 MiB               if flag == 1:
    81    388.0 MiB      0.0 MiB                   print(idx, file=f)
```