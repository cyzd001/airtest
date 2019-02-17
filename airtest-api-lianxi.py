# -*- encoding=utf8 -*-
__author__ = "Admin"

from airtest.core.api import *
import os

"""获取当前打开app包名"""
app = os.popen(adb shell dumpsys window | findstr mCurrentFocus)

"""获取当前连接设备"""
shebei = os.popen('adb devices').readlines()
for i in range(len(shebei)):
        if shebei[i].find('\tdevice') != -1:
            temp = shebei[i].split('\t')
            DEV = temp[0]
            
"""卸载app"""            
uninstall('org.cocos2d.test102_test')
"""安装app"""
install('D:\\app\\ceshi\\19995_Android.apk')
"""
如果存在app，报AdbError错误
"""
try:
    install('D:\\app\\ceshi\\19995_Android.apk')
except AirtestError:
    uninstall('org.cocos2d.test102_test')
    install('D:\\app\\ceshi\\19995_Android.apk')

"""设备上app"""
list = device().list_app(third_only=True)
result = []
for i in list:
    if i.startswith("org.cocos2d"):
        result.append(i)
print(result)

"""获得手机里面某个apk的应用信息、版本信息"""
os.popen(adb shell dumpsys package app)  #app是包名
os.popen(adb shell dumpsys)  #是列出手机上所以包名


"""adb启动apk"""
os.popen(adb shell am start -n breakan.test/breakan.test.TestActivity)

