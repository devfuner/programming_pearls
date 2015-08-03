```
devfunerui-MacBook-Air:column_01 devfuner$ time python exercise04.py

real    0m0.104s
user    0m0.064s
sys 0m0.043s
devfunerui-MacBook-Air:column_01 devfuner$ python exercise04.py
Filename: exercise04.py

Line #    Mem usage    Increment   Line Contents
================================================
    20      9.6 MiB      0.0 MiB   @profile
    21                             def random_items():
    22      9.6 MiB      0.0 MiB       n = 10000000
    23      9.6 MiB      0.0 MiB       k = 1000
    24      9.6 MiB      0.0 MiB       return random.sample(range(n), k)
```