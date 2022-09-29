#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = input()
l=[]
for i in range(26):
    l.append(0)
for i in s:
    l[ord(i)-ord('a')]+=1

m=0
for i in range(len(l)):
    if l[i]>l[m]:
        m=i
print(chr(m+ord('a'))+" "+str(l[m]))
l[m]=0

m=0
for i in range(len(l)):
    if l[i]>l[m]:
        m=i
print(chr(m+ord('a'))+" "+str(l[m]))
l[m]=0

m=0
for i in range(len(l)):
    if l[i]>l[m]:
        m=i
print(chr(m+ord('a'))+" "+str(l[m]))
l[m]=0

