# cs_study
```
The notes during my study of computer science
```
### 第一课 学习打字
在学习计算机科学之前，我们需要先学习一些基本的计算机操作，例如操作鼠标、键盘，使用输入法打字等等。

So, 我们先学习打字。

打字对于编程是极其重要的，能打好字，就能更加高效得编程。


### 第二课 学习pyhton脚本

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


### 第三课 更系统的list

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


### 第四课 寻找10000以内所有素数

今天我们来列出 1-10000 以内的所有质数。

我用了两种方式来找出这些质数。

首先我们来看`lstdir3.py`， 一开始我就给出了范围 2-10001 （质数>1）。

然后我就在此又用 % 来判断一个数是不是质数，%是求余符号，会算出数字的余数。如果 i 的除以 比它小的数 的余数等于 0 ，说明这个数是 i 的因数，那么 i 肯定不是质数，我们就设定 isodd 为“假”，然后跳出循环；如果 i 除以 比它小的数 的余数都不等于 0 的话，说明比它小的数里面没有它的质因数，那么它本身应该就是质数，这时 isodd 的值不会被更改，我们通过判断 isodd 为“真”，就会把数字打印出来。



现在我们就来看更加复杂的版本，[质数的筛法](https://baike.baidu.com/item/%E7%AD%9B%E6%B3%95)。

其实`lstdir4.py`也很容易理解，首先我们导入了 math 和 time 两个模块，先不要去管 time（它仅仅是用来计算我们程序的执行时间），我们来看 math 的部分。

起始我们先标明了最后的数字：last

在此我就说了：“我的`list`只能在10001以内（因为最后一个数是10000但这里说了`last`加一），每一个数组元素的值都是 True（“真”）。

呢么为什么要到10001呢？

那是因为，数组从0开始，如果只到10000的话最后一个数是9999而不是一万，所以我加了一个1。

然后我们就标明了范围：“开始”，“结束”，和“步骤/过程”

之后我们定义了一个 my_range ，用来根据要走的步长来计算倍数。这里面用到了 yield，它的意思是，除了第一次使用 my_range 返回 start，后面返回的数值都是 yield 这步以后的计算步骤得到的结果，这里是 start 上累加 step。

后面就直接排除掉了0和1，因为它们不是素数也不是合数。

下面就稍微有点复杂了，这里说在 2-10001 的数中只取10001的算数平方根以内的数来做筛法，筛法就是在 2 到 last + 1 的数里，把 2 到 last + 1开平方根 的倍数都删掉，这里我们就是给对应的数组元素值设为 False(“假”)。这里求倍数我们就用到了前面我们自己定义的 my_range 方法。

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


### 第五课 正式开始学习Python

这节课可以说是我第一节正式学习Python的一堂课。

虽然说正式学习Pyhton的第一课，但是很多东西都在先前的课里面学到了，所以也可以说是预习。

今天我们去到了Python的官网来进行对Pyhton更深一步的了解。
```
https://docs.python.org/3/tutorial/interpreter.html
```
以上是Python的官方教程的网址

首先第一章其实并没有讲什么，就是Pyhton的一个简单的介绍，和哪里好哪里不好。

第二章讲的是Python的两种模式：

1.交互模式

所谓交互模式，就是最常见的模式，就是在电脑里打字立马就会出来结果，terminal就是用的交互模式。

2.脚本模式

脚本模式就是把程序写成文档然后再用 `./+文件名` 来实现操作。

第三章就开始了正式的介绍了Python的基本用途，例如计算机和字符串。

这里介绍到，Python可以当作计算机使用，并且很方便，可以基本上实现所有计算功能。

里面给到的例子就有小数，整数，和代数计算。

其中还介绍了字符串，里面其中一个例子就是用字符串将 Python 这个词中的某些特定的字母单独挑出来。

字符串还被用到了区分方面，例如 'dosen't'这个例子，

如果直接把'dosen't'输入进电脑里，它就不知到怎么相应，因为电脑会把 t 前面的撇点也看成 ' ' 。

所以这里就用到了 \ ，\的用处就是让电脑区分开两种情况的符号。

还有一点，字符串是不可修改的，所以不能修改已有的数据。

下面就讲到了 list， list 就是列表，能列出来已经定义了的东西.

List 和字符串的其中一个区别就是，list 是可以修改的。

最后我们就用斐波那契数组学习到了基础的语法和编程
![the example of basic indentation and programming](https://screenshotscdn.firefoxusercontent.com/images/4e8a6020-3254-439b-9a3a-0fd12dd5ed19.png)


### 第六课 更多对于程序流程的控制

今天我们就来学习Python官网里第四章的内容，

首先我们就看见了 if，if 是我们最常用到的变成语句。

if 的意思就是如果，

一开始给到的例子是一个代数例子

![picture](./imgs/snapshot001.png)

就是说，如果 x 小于零那么就将其变成零，如果 x 等于零，那么就是零，如果 x 大于零，那么就输出 More。

好吧，这个程序也是够简便的。

但是这里介绍到了和 if 功能一样的语句，那就是 elif

那么什么时候用 if 什么时候用 elif 呢？

其实他们两个之间有很大的区别，那就是 elif 是留给 if 后面的所有可能性的。

也就是说，if 只是留给开头用的，如过后面还有可能性而且是在一个循环内的，就用 elif.

接下来也介绍到了一个非常常用的语句，那就是 for，

意思就是对于。

比如说将 word 这个变量中所有值的长度，然后将其发布（例一）。

for 是一个循环，它只有在所有可能性实施后才会停止。

下面讲到了 range， 

range 的意思是范围，我们在 lstdir3.py 和 lstdir4.py 中都在计算范围时用过这个语句。

用 range 语句可以把任何排列性质的数组或者list进行更加系统的范围排序。

下面我们就看到了三个非常重要的语句条款，它们能对编程有更多的细节和范围约束性。

- break能切断循环

- else就是一个循环里除了列出可能性以外的其他可能性

- continue能在循环本应中断的时候让其继续


下面介绍到了一个在程序里基本上没有什么用处但是还有用的语句：pass。

pass 的唯一用图就是保留空间。

但是 functions/函数 可比 pass 有用多了。

functions 的作用很大，我也不知道所有的，所以这里只介绍一部分，

首先需要 define/定义 一个变量，然后基本上拿它干什么都行了。

下面介绍到的 keywords argument 基本上就是有三个值的变量，

而且必须得是系统已经起好的名字，

再下面就是可以有无限多值的变量。

下面就是高深莫测的 lambda表达式了，

lambda表达式的用途就是将一个值经过更改返回一个不同的值，例子：

![lambda expression](https://screenshots.firefox.com/ccSoF57awUx1Cc3a/docs.python.org)

下面又是一个几乎没什么用的语句，叫 documentation，

系统都说它没什么用了

![documentation](https://screenshots.firefox.com/Mfwvo75N4li6P2ni/docs.python.org)

最后讲解了，编程的一种写法，叫 PEP8，有兴趣的请点[这里](https://www.python.org/dev/peps/pep-0008/)

啊啊啊啊啊！！！

终于写完了。