#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import math

st = time.time()	# 起始时间

last = 10000 # 设定要查找的范围：last
nums = list(True for _ in range(last + 1))	# 构造数量为 last + 1 个(因为第0个不记入)，元素值为 True 的数组

# 根据step步长走过整个序列
def my_range(start, end, step):
	while start <= end:
		yield start
		start += step

nums[0] = False # 0
nums[1] = False # 1

for i in range(2, 	int(math.sqrt(last + 1))):
	for j in my_range(i, last + 1, i):
		#print 'i', i, 'j', j # DEBUG: 查看i的倍数
		if j > i and j <= last and nums[j]:
			nums[j] = False

for i in range(len(nums)):
	if nums[i]:
		print i
		#open("Odd.txt","a").write("%s\n"%(i))	# 输出到文件Odd.txt

et = time.time()	# 结束时间

print "Time cost: ",(et - st)," second."	# 总耗时