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


## 第四课 寻找10000以内所有素数

今天我们来列出 1-100 以内的所有质数。

我用了两种方式来找出这些质数。

首先我们来看`lstdir3.py`， 一开始我就给出了范围 2-100 （质数>1）。

然后我就在此又用 % 来判断一个数是不是质数，%是求余符号，会算出数字的余数。如果 i 的除以 比它小的数 的余数等于 0 ，说明这个数是 i 的因数，那么 i 肯定不是质数，我们就设定 isodd 为“假”，然后跳出循环；如果 i 除以 比它小的数 的余数都不等于 0 的话，说明比它小的数里面没有它的质因数，那么它本身应该就是质数，这时 isodd 的值不会被更改，我们通过判断 isodd 为“真”，就会把数字打印出来。



现在我们就来看更加复杂的版本，[质数的筛法](https://baike.baidu.com/item/%E7%AD%9B%E6%B3%95)。

其实`lstdir4.py`也很容易理解，首先我们导入了 math 和 time 两个模块，先不要去管 time（它仅仅是用来计算我们程序的执行时间），我们来看 math 的部分。

起始我们先标明了最后的数字：last

在此我就说了：“我的`list`只能在101以内（因为最后一个数是100但这里说了`last`加一），每一个数组元素的值都是 True（“真”）。

呢么为什么要到101呢？

那是因为，数组从0开始，如果只到100的话最后一个数是99而不是一百，所以我加了一个1。

然后我们就标明了范围：“开始”，“结束”，和“步骤/过程”

之后我们定义了一个 my_range ，用来根据要走的步长来计算倍数。这里面用到了 yield，它的意思是，除了第一次使用 my_range 返回 start，后面返回的数值都是 yield 这步以后的计算步骤得到的结果，这里是 start 上累加 step。

后面就直接排除掉了0和1，因为它们不是素数也不是合数。

下面就稍微有点复杂了，这里说在 2-101 的数中只取101的算数平方根以内的数来做筛法，筛法就是在 2 到 last + 1 的数里，把 2 到 last + 1开平方根 的倍数都删掉，这里我们就是给对应的数组元素值设为 False(“假”)。这里求倍数我们就用到了前面我们自己定义的 my_range 方法。

这是为什么呢？

让我来举个例子：![x \cdot y = z](https://latex.codecogs.com/svg.latex?x&space;\cdot&space;y&space;=&space;z) （x乘y等于z），如果x大于 ![\sqrt{z}](https://latex.codecogs.com/svg.latex?\sqrt{z}) （z的算数平方根），那么y必定小于 ![\sqrt{z}](https://latex.codecogs.com/svg.latex?\sqrt{z}) ，那是不是x就不用再去求了呀？！

筛完了之后被筛过的数字都没有出现在列表里。我们就用一个循环把留下的质数打印出来（也可以输出到文件里）。

我们好像还遗漏了什么？哦，对，是时间。

我们要时间就是为了测量运行整个程序的时间。

用 `et(end time)`减去`st(start time)`就行了

嗒哒！大功告成。


***PS:***

这里介绍一下怎么在github的markdown里插入公式。访问在线公式生成器 https://www.codecogs.com/latex/eqneditor.php ，调整一下选项（我就用了svg格式），然后输入你的公式，生成的 HTML 代码里就包含了图片网址，直接在github的markdown里使用图片插入语法调用就好了，例如 x乘y等于z：
```
![x \cdot y = z](https://latex.codecogs.com/svg.latex?x&space;\cdot&space;y&space;=&space;z)
```



