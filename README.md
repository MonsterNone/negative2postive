# negative2postive
Convert negative film to normal colour. 将翻拍的彩色负片转换成正常的颜色（去色罩）

# 去色罩使用的方法
在曲线里面拉R G B，倒置并且拉到起点。

可以参考具体的实现：
[如何科学而正确的去除色罩？ - 黄昊Haosky的回答 - 知乎](https://www.zhihu.com/question/50793003/answer/137645900)

(实际代码中并没有管18%灰的问题，只是简单地倒置曲线)

# 效果演示

# 原始图片的准备
> 我是直接翻拍的，扫描出来的负片（负片正扫）应该也可以
1. 在PS中打开raw图片 ~~，最好用ProPhoto RGB（16位）打开~~(PIL库处理色深有问题？)
2. 裁切（快捷键C）出成像部分，不要留有片基！不要留有片基！不要留有片基！（宁可多抠一点）
3. 将裁切好的保存，保存为tiff格式（后缀名为 **.tif** ）
选项如下：
```
嵌入颜色配置文件
**无压缩**
像素顺序 - 隔行（没测试不知道有没有区别）
```

## DLC：关于白平衡

翻拍没有放底片的时候使用相机白平衡自定义里面的白色设置设定一下（也是玄学）

也可以后期在ps里面设置。扫描就无所谓了

# 程序使用说明
1. 下载https://github.com/MonsterNone/negative2postive/raw/master/run.exe 。Windows端直接下载打包好的run.exe，Mac的话自己安装下python3的numpy和pillow模块吧（不会的自行百度）。Linux...Linux就别用了，没有ACR解raw很麻烦
2. 在程序同一目录下创建两个文件in 和 out
3. 把上一步骤准备好的.tif图片放到in里面
4. 运行
5. 输出在out文件夹里

# 代码实现
> 很粗糙

首先提取r g b三个分量的图片，然后各自用numpy转换成数组。

接着从中选出最大值和最小值。最大值对应ps中曲线0，最小值对应ps中曲线255，输入值为x，输出值为y，这样就有了一个y=kx+b。

然后把之前得出的数组每个值都用y=kx+b算一下，最后三个颜色分量合并。

大功告成。

# 如果你有更好的算法或者其他思路欢迎issue和pr
