# Face-Detection

## 中文介绍

本项目包含了一些人脸识别相关的例程。包括了人脸检测，人脸识别，人脸打码等。

参考的他人项目有：
https://github.com/ageitgey/face_recognition

我的CSDN博客写了更加详细的过程：https://blog.csdn.net/yzy_1996/article/details/80223053

>文件说明

.py是python的可执行程序。

.html是做的一个UI界面。

.xml是人脸识别的库。

.jpg是做人脸识别时对照的人脸照片。(某些问题删掉了，请换上自己的吧)


>相关准备说明

安装opencv-python库，你可以去网上查如何下载。

安装face_recognition库，```pip install face_recognition```

找到 haarcascade_frontalface_default.xml 包

>使用说明

安装了相关的包后，这些Python程序就可以直接运行了。注意人脸识别需要你自己放几张照片进去，并改好相应的名字。

如果想要看到一个好看的UI界面，可以双击这个网页文件，我使用的是Chrome浏览器，而里面有一个指令只能在IE的内核下运行，所以我下载了一个IE Tab 的拓展项，它会在C盘下创建一个文件夹，比如我的就是 ```C:\Users\Jerry\AppData\Local\IE Tab\11.4.23.1``` 因为打开网页后执行的代码的根目录都是这个地址，所以我们把这些文件都移动到改文件目录中，然后就可以完美地实现了。

如果使用IE浏览器，就把所有文件都放在桌面，如果想在其他文件夹使用，你需要修改代码里的文件地址，全部改为绝对地址。


