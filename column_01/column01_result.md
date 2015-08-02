```
devfunerui-MacBook-Air:column_01 devfuner$ python -m memory_profiler column01.py
Filename: column01.py

Line #    Mem usage    Increment   Line Contents
================================================
    46     10.2 MiB      0.0 MiB   @profile
    47                             def read_file():
    48     10.2 MiB      0.0 MiB       nums = []
    49     10.2 MiB      0.0 MiB       with open('number.txt', 'r') as f:
    50    574.4 MiB    564.2 MiB           for line in f.readlines():
    51    574.4 MiB      0.0 MiB               nums.append(int(line))
    52     55.1 MiB   -519.3 MiB       return nums
```