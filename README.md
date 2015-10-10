## 百度贴吧自动一键签到

平台：
Python 2.7.9
OS 10.10.5

需要安装的 Python 库：
pyautogui
pyobjc-core
pyobjc

使用方法：
1. 第一次使用时，需要根据 浏览器大小 和 屏幕大小 重新定位、获取 每次鼠标点击的坐标。
方法：注释 def 和 调用语句，允许`print pyautogui.position()`执行，将鼠标移动到需要点击的位置，运行`python main.py`获取坐标，替换脚本中的两个坐标
2. 确认退出 chrome（不仅仅是关闭窗口）
3. 在 shell 中运行`python main.py`，整个过程大概4s，期间不要动鼠标
