# SpeechRecognition

## 依赖项

代码中需要用到以下的包，请确保您的环境中已经安装好这些包。

```python
# asr.py
from PyQt5 import QtWidgets, QtGui, QtCore, uic

import sys
import os
import webbrowser

import speech_recognition as sr
import threading
```

```python
# asrInterface.py
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QDesktopWidget
```

## 运行演示

进入工作目录

<img src="./images/cd.png">

激活虚拟环境

<img src="./images/activate.png">

运行程序

<img src="./images/run_code.png">

显示图形化用户界面

<img src="./images/GUI.png">

可以在命令行看到程序运行状态的提示信息

没有识别到音频

<img src="./images/hear_nothing.png">

识别到 **play music** 指令

<img src="./images/play_music_detected.png">

播放音乐

<img src="./images/play_music.png">

识别到 **open notepad** 指令

<img src="./images/open_notepad_detected.png">

打开文件

<img src="./images/open_notepad.png">

没有识别到指令

<img src="./images/no_command_detected.png">

程序运行过程中会持续监听麦克风的音频输入并进行识别，直到用户关闭程序。