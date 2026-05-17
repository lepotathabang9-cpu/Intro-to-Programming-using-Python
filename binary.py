# https://github.com/lepotathabang9-cpu/Intro-to-Programming-using-Python.git

import sys 

n = abs(int(sys.argv[1])) # Ask user for input
i = 1 # Initalize i

# Compute the largest power of 2 that is greater than or equal to the input integer.
while i < n: i *=2

# If i is greater than n, reduce it by a factor of 2.
if i > n :
    i = i // 2


while i > 0:
    if i <= n:
        print('1',end="")
        n = n-i
        i = i//2
    else:
        print('0',end="")
        i = i//2
print()