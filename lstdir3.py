#!/usr/bin/env python
# -*- coding: utf-8 -*-

max = 100
min = 1
print("Prime numbers between %s and %s are: ", min, max)

for num in range(min, max + 1):
	if num > 1:
		isodd = True
		for i in range(2, num):
			if((num % i) == 0):
				isodd = False
				break
		if isodd:
			print(num)