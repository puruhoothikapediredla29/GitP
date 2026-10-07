from datetime import date
print(date(2026,1,12)- date(2026,10,29))
import os

print(os.getcwd())
import os

print(os.listdir())

import os

if os.path.exists("data.txt"):
    print("File exists")
else:
    print("File does not exist")

import sys

print(sys.version)
import sys

print(sys.argv)
from collections import Counter

text = "hello"



print(Counter(text))
import statistics 
numbers = [1,2,3,4,5,6]
print(statistics.mean(numbers))

import time

print(time.time())
import time

print("Hello")

time.sleep(3)

print("World")
import time

current = time.localtime()

print(current)
