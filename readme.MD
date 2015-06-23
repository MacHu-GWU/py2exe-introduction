#Py2exe introduction

![](py2exe_logo.png)

本项目是一个py2exe的教学文档项目

##[CN]介绍

py2exe是一个能将python脚本转化成windows系统中的.exe可执行文件。即双击test.exe和python test.py的效果是完全一样的。而这个转换过程涉及了将py脚本编译成c语言和dll动态链接库的过程, 我也不是很清楚。本文主要用最简单的语言介绍如何用py2exe将你写的python脚本变成exe, 而在其他windows机器上无需安装python即可运行。

##[CN]py2exe的安装

因为.exe文件是微软的windows系统下的特有可执行文件。而你既然想要你的脚本能在windows下运行, 相信你的开发平台也选的是windows。所以在windows下安装py2exe非常简单, 只要双击执行已经build好的安装文件即可:

	py2exe-0.9.2.2.win32.exe - 32位系统, 例如xp
	py2exe-0.9.2.2.win-amd64.exe - 64位系统, 例如window7

2014-10-21 distribution是由py2exe开发组织在2014年10月21日发布的。

安装完毕后, python setup.py 命令就会多一个选项 py2exe。例如: python setup.py py2exe。
具体用途下面详述。

##[CN]py2exe的使用

我们以example-project为例。其中hello.py是我们的主脚本(python2,3兼容)

	from __future__ import print_function
	import sys
	
	is_py2 = (sys.version_info[0] == 2)
	print("hello")
	if is_py2:
	    raw_input("press any key to exit... ")
	else:
	    input("press any key to exit... ")

然后在和hello.py同一个文件夹下建立一个setup.py脚本([setup.py的详细介绍](https://docs.python.org/2/distutils/setupscript.html))。内容如下:

	from distutils.core import setup
	import py2exe
	
	setup(console=["hello.py"])

然后打开命令行, cd到setup.py目录下, 执行:

	python setup.py py2exe

那么py2exe就会把hello.py所依赖的第三方包, 以及所需要的一切都编译好, 并在当前目录生成一个dist文件夹, 里面的hello.exe文件即是和hello.py同功能的可执行文件。

##Reference

- software download: [https://pypi.python.org/pypi/py2exe/](https://pypi.python.org/pypi/py2exe/)
- official tutorial: [http://www.py2exe.org/index.cgi/Tutorial](http://www.py2exe.org/index.cgi/Tutorial)
- more information: [http://www.py2exe.org/index.cgi/FrontPage](http://www.py2exe.org/index.cgi/FrontPage)
	