#!/usr/bin/python
# -*- coding:utf-8 -*-

# import webbrowser
import pyautogui
import time
# from selenium import selenium
import subprocess


# print pyautogui.position() # 获取当前鼠标的坐标

# webbrowser.open_new_tab("https://www.baidu.com/")
def browse():
    child = subprocess.Popen("/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome http://tieba.baidu.com/", shell=True)

    time.sleep(2)
    pyautogui.moveTo(303, 612)  # 一键签到 。上方可能会有新内容弹出，在加载完成前点击就可以了
    pyautogui.doubleClick()

    time.sleep(1)
    pyautogui.moveTo(664, 360)  # 进行签到
    pyautogui.doubleClick()

    child.kill()

browse()
