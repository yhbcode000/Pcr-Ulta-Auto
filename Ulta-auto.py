import mouse as m
import time as t
import pandas as pd
import os

auto_df = pd.read_csv(os.path.join(os.getcwd(), "data", "zhou.csv"))
ubPosition = []

print("----公主连结：Re dive---\n超级自动工具\n注意事项：因为大部分模拟器权限比较高，本程序需要管理员权限才能正常工作\n")


def text_save(filename, data):  # filename为写入CSV文件的路径，data为要写入数据列表.
    file = open(filename, 'w')
    for i in range(len(data)):
        s = str(data[i]).replace(
            '[', '').replace(']', '')  # 去除[],这两行按数据不同，可以选择
        s = str(data[i]).replace(
            '(', '').replace(')', '')  # 去除(),这两行按数据不同，可以选择
        s = s.replace("'", '').replace(',', '') + '\n'  # 去除单引号，逗号，每行末尾追加换行符
        file.write(s)
    file.close()
    print("保存文件成功")


reset_flag = input("是否完成过UB位置设置? (y/n)")
if (reset_flag != "y"):
    print("请进入模拟战模式，按照指令设置5个UB点点击位置\n")
    for i in range(5):
        print("鼠标指针滑到左边开始第" + str(i+1) + "个UB(不要进行点击)\n然后按回车键确认当前位置\n")
        input()
        ubPosition.append(m.get_position())
        # print("Log:"+str(ubPosition[i]))
    text_save("data/ubPosition.txt", ubPosition)

f = open('data/ubPosition.txt')
ubPositionString = f.read()
f.close()

ubPositionString = ubPositionString.split('\n')

for i in range(5):
    listTemp = []
    for j in ubPositionString[i].split(' '):
        listTemp.append(int(j))
    ubPosition.append(listTemp)
    # print("Log:"+str(ubPosition[i]))

boss_num = input("输入对应的boss编号 (1-5): ")
angre_bool = input("是否狂暴? (y/n): ")
angre_bool = (angre_bool == "y")

angre_note = "狂暴" if angre_bool else "普通"
print("开始运行针对" + angre_note + boss_num + "号boss的轴\n\n")

if angre_bool:
    bossIndex = boss_num + "b"
else:
    bossIndex = boss_num + "a"

timeStamp = auto_df[bossIndex]

UBList = auto_df[bossIndex+"-ub/num"]


starting_time = int(input("请进入战斗并暂停，输入当前的时间，例如89或者88，单位是秒: "))

print("鼠标指针滑到\"返回\"按钮位置(不要进行点击)\n然后按回车键确认当前位置，程序将托管会战\n")
input()
resume_position = m.get_position()

# double click to ensure working
m.move(resume_position[0], resume_position[1])
m.click()
t.sleep(0.1)
m.move(resume_position[0], resume_position[1])
m.click()

index = 0
for i in range(starting_time):
    currentTime = starting_time - i
    if i == 0:
        timeStampNow = timeStamp[index]
        UB = UBList[index]-1
        index += 1
        t.sleep(0.999)
        continue
    if currentTime == timeStampNow:
        m.move(ubPosition[UB][0], ubPosition[UB][1])
        for click in range(22):
            m.click()
            t.sleep(0.045)
        t.sleep(4)
        if index < len(timeStamp):
            timeStampNow = timeStamp[index]
            UB = UBList[index]-1
            index += 1
            continue
    t.sleep(0.999)

print("程序运行结束\n按任意键退出")
os.system('pause')
