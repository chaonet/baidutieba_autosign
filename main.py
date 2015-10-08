#!/usr/bin/python
# -*- coding:utf-8 -*-

import webbrowser
import pyautogui
import time

print pyautogui.position() # 获取当前鼠标的坐标


webbrowser.open_new_tab("https://www.baidu.com/")

time.sleep(0.5)
pyautogui.moveTo(1023, 137) # 点进 贴吧

pyautogui.click()
time.sleep(1)
pyautogui.moveTo(309, 617)  # 一键签到 。上方可能会有新内容弹出，在加载完成前点击就可以了
pyautogui.click()
time.sleep(0.5)
pyautogui.moveTo(660, 405)  # 进行签到
pyautogui.click()
time.sleep(0.5)
pyautogui.moveTo(943, 239) # 关闭签到弹窗
