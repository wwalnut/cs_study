#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from datetime import datetime

root_dir = "/Users/wangjh/Workspace/cs_study/test/"

for root, dirs, files in os.walk(root_dir):
	open("Public2.cdc","a").write("File info under %s: \n"%(root_dir))
	open("Public2.cdc","a").write("%s \t%s \t\t%s\n"%("文件名", "文件大小", "创建时间"))
	for file in files:
	    fstat = os.stat(root_dir+file)
	    fsize = fstat.st_size
	    fctime = datetime.fromtimestamp(fstat.st_birthtime)
	    open("Public2.cdc","a").write("%s \t%s \t\t%s\n"%(file, fsize, fctime))
