```
devfunerui-MacBook-Air:column_01 devfuner$ python -m memory_profiler exercise01.py
Filename: exercise01.py

Line #    Mem usage    Increment   Line Contents
================================================
    46     10.2 MiB      0.0 MiB   @profile
    47                             def read_file():
    48     10.2 MiB      0.0 MiB       nums = []
    49     10.2 MiB      0.0 MiB       with open('number.txt', 'r') as f:
    50    457.8 MiB    447.6 MiB           for line in f.readlines():
    51    457.8 MiB      0.0 MiB               nums.append(int(line))
    52     51.2 MiB   -406.5 MiB       return nums

Filename: exercise01.py

Line #    Mem usage    Increment   Line Contents
================================================
    55    423.9 MiB      0.0 MiB   @profile
    56                             def sorted_file(nums):
    57    423.9 MiB      0.1 MiB       with open('sorted.txt', 'w') as f:
    58    424.1 MiB      0.2 MiB           for num in nums:
    59    424.1 MiB      0.0 MiB               print(num, file=f)

devfunerui-MacBook-Air:column_01 devfuner$ time python exercise01.py

real    0m32.840s
user    0m31.113s
sys 0m1.144s
```