# cs_study
```
The notes during my study of computer science
```
## 第一课 学习打字
在学习计算机科学之前，我们需要先学习一些基本的计算机操作，例如操作鼠标、键盘，使用输入法打字等等。

So, 我们先学习打字。

打字对于编程是极其重要的，能打好字，就能更加高效得编程。


## 第二课 学习pyhton脚本

今天，我们来学习怎样创造脚本和使用脚本运行一段python脚本

我们的目标是列出某个目录的所有文件并把结果输出到一个文本文件里面。

首先，在脚本的头部，定义这是一个python脚本，并以 utf-8 编码：
```
#!/usr/bin/env python
# -*- coding: utf-8 -*-
```

然后，引入python的os库，这样我们就可以使用对操作系统的相关方法：`import os`。

之后就是一个for循环，用它我们遍历指定目录的根目录以及其下的子目录、文件，在循环体内打开一个叫 Public.cdc 的文件，以追加模式写入根目录、文件夹和文件。

```
for root, dirs, files in os.walk("/Users/wangziqiao/workspace/cs_study/test"):
  open("Public.cdc","a").write("%s %s %s"%(root, dirs, files))
```

经过两遍尝试运行脚本：`./lsdir.py`，我们就得出了...感觉什么都没得出的样子，但是如果cat一下Public.cdc的话，就会发现上面显示了：
```
/Users/wangziqiao/workspace/cs_study/test [] ['bbb', 'ccc', 'aaa']/Users/wangziqiao/workspace/cs_study/test [] ['bbb', 'ccc', 'aaa']
```

这么一大行东西。

那么这一坨到底是什么呢，它就是在lsdir.py里所 walk 的 ("/Users/wangziqiao/workspace/cs_study/test") 了。

成功了yeah！！！


## 第三课 更系统的list

今天的任务是把`test目录`下的所有文件更系统化-而不是一行-地列出来，

还需要列出它的大文件名, 文件大小, 和创建时间。

首先我们用第一个`for`循环来找出`aaa,bbb,和ccc`并将它们归入`files`。

在第二个`for`循环中我们就开始把这三个文件的数据列出来并用`/t`来充当空格使结果看起来更整齐。

但我们测试完结果后出现了一个问题：时间不可读。

出来结果后我们发现，上面显示的时间只是单纯的一串杂乱的数字，（在人类看来）根本不可读。

那我们怎么办呢？

通过在网上搜查了一番之后我们就找到了我们需要的东西：
```
fromtimestamp(fstat.st_birthtime)
```
通过它我们就看到了人能读懂的年，月，日了

其实通过仔细的查看，我们会发现，在第一个`for`循环其实就是第二课程序的修改版。

今天我的任务算是完成了。


## 第四课 寻找100以内所有素数

今天我们来列出 1-100 以内的所有质数。

我用了两种方式来找出这些质数，

`lstdir3.py`是`lstdir4`的复杂版，也更加详细。

首先我们来看`lstdir4.py`， 一开始我就给出了范围 2-100 （质数>1）。

然后我就在此又用 % 限制了范围，

%会算出数字的余数，如果 i 的余数除以 2 等于 0 的话 就会把数字打印出来, 	

因为质数的因子只有 1 和质数本身，所以用二除以质数不可能等于零，所以就用`break`跳出了循环。

现在就用到了`else`，`else`的意思就是别的，或者其他，在这里它代表除列出可能性的一切其他可能性

在这里就是指除了双数之外的书，也就只能是质数。

现在`lstdir4.py`就好解释了，一开始只不过是用了代数的方法，然后加了一些辅助作用的词，如`"Prime numbers between",min,"and"max,"are:"`。

