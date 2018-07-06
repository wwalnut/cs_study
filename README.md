# cs_study
The notes during my study of computer science

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