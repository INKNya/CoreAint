#CoreAint 客制于INKANT的超定义化程序集


#=========================================================================

#库导入

import threading
from datetime import datetime
import os
import tkinter
import platform
import time
from threading import Thread
from tkinter import PhotoImage, Frame
from tkinter.ttk import Label
from colorama import init,Fore,Back,Style
init()
import pywinstyles


#=========================================================================
#根窗口创建
os.system(f'mode con: cols=130 lines=20') #cmd初始化
root = tkinter.Tk()

#title文件;系统信息打印
with open("title.txt","r") as t:
    content = t.read()
print(content)

print('——————————————————————————')

system = platform.python_version()
print('|Python-version:',system)
system = platform.system()
print('|System:',system)
system = platform.node()
print('|PC-name:',system)
system = platform.processor()
print('|CPU:',system) #信息打印完成

#输出台等待所有组件加载完成
def first_print_succ(part_name): #结束加载（成功）
    print(Back.GREEN+Fore.BLACK+'succeed','[',part_name,']'+Style.RESET_ALL)


#各变量初始化

Theme = 'aero' #basic Theme




#创建UI加载子进程
def start_wait():
    root.title("StartWait")
    root.overrideredirect(True)
    # file = PhotoImage(file="file_photo/CoreAint.gif")
    # label = Label(root, image=file)
    # label.pack()
    # 确定窗口大小
    root.geometry("600x300")
    file = PhotoImage(file="file_photo/CoreAint.gif")
    root.config(bg="black")
    label = Label(root, image=file)
    root.update()
    label.place(x=-2,y=-2)
    x = int((root.winfo_screenwidth() - root.winfo_reqwidth()) / 2)
    y = int((root.winfo_screenheight() - root.winfo_reqheight()) / 2)
    # 将窗口居中显示
    x = x - 250
    y = y - 40
    root.geometry("+{}+{}".format(x, y))
    z = 0
    z_speed = 0
    root.update()


def other_flies_loading():
    # 检查附加文件是否存在
    # 可支持的文件：
    # 附加软件包（打包文件夹Other）
    # 音乐包(打包文件夹Music,支持主流音乐格式)
    other_files = os.path.exists('Other')
    music_files = os.path.exists('Music')

    if other_files or music_files:
        print('FOUND FLIES,TRYING TO LOADING...')
        if music_files:
            print(Fore.GREEN + '.Music/' + Fore.RESET)
            Musics = os.listdir('Music')
            for i in Musics:
                time.sleep(0.01)
                print(Fore.BLUE + '--' + i + Fore.RESET)
        if other_files:
            print(Fore.GREEN + '.Other/' + Fore.RESET)
            Other = os.listdir('Other')
            for i in Other:
                time.sleep(0.01)
                print(Fore.BLUE + '--' + i + Fore.RESET)
        print(Back.GREEN + 'ALL OTHER FILES LOAD' + Style.RESET_ALL)
        time.sleep(1)
    else:
        print(Back.YELLOW + "NO FOUND OTHER FILES-", "SKIP" + Style.RESET_ALL)

    first_print_succ("other_flies")

def overs_start():
    file = PhotoImage(file="file_photo/CoreAint.gif")
    root.config(bg="black")
    label = Label(root, image=file)
    root.update()
    label.place(x=-2,y=-2)
    x = int((root.winfo_screenwidth() - root.winfo_reqwidth()) / 2)
    y = int((root.winfo_screenheight() - root.winfo_reqheight()) / 2)
    # 将窗口居中显示
    x = x - 250
    y = y - 40
    root.geometry("+{}+{}".format(x, y))
    z = 0
    z_speed = 0
    root.update()
    time.sleep(0)
    for i in range(50):
        z_speed += 1
        z -= 1 + z_speed
        time.sleep(0.01)
        root.update()
        root.geometry("+{}+{}".format(x, y + z))
    first_print_succ("start_wait")
    root.destroy()

def config_create():
    # 初始化创建所需文件
    global Theme
    found_file = os.path.exists("Config.txt")
    if not found_file:
        print(Back.YELLOW + "NOT FOUND CONFIG,CREATE NOW..." + Style.RESET_ALL) #未找到文件 写入
        with open('Config.txt','w') as config:

            #开始写入
            config.write('CreateTime = '+ str(datetime.now()))
            config.write('\nlast changed = '+ str(datetime.now()))
            config.write('\ntheme = ')
            config.write('\n'+Theme)


    else:
        print("FOUND CONFIG,LOADING CONFIG NOW...") #找到文件 读取
    cfg =open('Config.txt',"r",encoding='utf-8')
    print('----------------------------------------')
    #获取config内容
    cfg = cfg.read().splitlines()
    print((Fore.RED , cfg , Style.RESET_ALL)) #以表格列出config
    #载入config
    Theme = cfg[3]



    first_print_succ("config_loading/create")


StartWait = Thread(target=start_wait()) #定义线程
FileLoading = Thread(target=other_flies_loading())
overs_all_loading = Thread(target=overs_start())
Config_Create = Thread(target=config_create())

StartWait.start() #启用线程
StartWait.join() #等待线程
FileLoading.start()
FileLoading.join()
Config_Create.start()
Config_Create.join()


overs_all_loading.start() #加载结束
overs_all_loading.join()



#主窗口加载
main = tkinter.Tk()
pywinstyles.apply_style(main,Theme)

#GUI部件部署
TextFrame = Frame(main,bd=100,highlightthickness=1,height=10,width=10)
TextFrame.pack()


main.mainloop()

