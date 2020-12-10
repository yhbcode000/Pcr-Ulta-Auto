# pcr-ulta-auto

公主连结自动跑轴工具

## 公主连结自动跑轴工具部分说明

1. data 文件夹下 zhou.csv 文件是轴的存储表格，是允许修改的部分。
    1.1. 其中1-5表示boss编号
    1.2. a、b表示非狂暴和狂暴
    1.3. 时间单位为秒
    1.4. UB是从左到右是1到5，表示第几个角色UB
2. 程序运行时按照指令操作即可。
    2.1. 注意尽量使用管理员模式打开，模拟器的权限往往很高
    2.2. 程序运行中，鼠标随意点击不会影响程序运行。程序中鼠标移动取绝对坐标
3. 程序采用MIT协议（可以乱改）GitHub 地址：https://github.com/Discover304/pcr-ulta-auto 
4. Happy Auto

## 乱七八糟的

variable include:

```python
timeStamp
UBList
clicks
ubPosition

# 获取截屏
import pyautogui
import cv2
img = pyautogui.screenshot(region=[0,0,100,100]) # x,y,w,h
# img.save('screenshot.png')
img = cv2.cvtColor(np.asarray(img),cv2.COLOR_RGB2BGR)
```
