#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
for root, dirs, files in os.walk("/Users/wangziqiao/workspace/cs_study/test"):
  open("Public.cdc","a").write("%s %s %s"%(root, dirs, files))
