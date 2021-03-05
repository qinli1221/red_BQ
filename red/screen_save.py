import subprocess


class Screenshot ():  # 截取手机屏幕并保存到电脑
    def __init__(self):
        # 查看连接的手机
        connect = subprocess.Popen ("adb devices", stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        stdout, stderr = connect.communicate ()  # 获取返回命令
        # 输出执行命令结果结果
        stdout = stdout.decode ("utf-8")
        stderr = stderr.decode ("utf-8")
        # print (stdout)
        # print (stderr)

    def screen(self):  # 在手机上截图
        cmd = r"adb shell /system/bin/screencap -p /sdcard/1.png"
        screenExecute = subprocess.Popen (str (cmd), stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        stdout, stderr = screenExecute.communicate ()
        # 输出执行命令结果结果
        stdout = stdout.decode ("utf-8")
        stderr = stderr.decode ("utf-8")
        # print (stdout)
        # print (stderr)

    def saveComputer(self, cmd):  # 将截图保存到电脑
        screenExecute = subprocess.Popen (str (cmd), stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        stdout, stderr = screenExecute.communicate ()
        stdout = stdout.decode ("utf-8")
        stderr = stderr.decode ("utf-8")
        # 输出执行命令结果结果
        stdout = stdout.decode ("utf-8")
        stderr = stderr.decode ("utf-8")
        # print (stdout)
        # print (stderr)

#
# cmd1 = r"adb shell /system/bin/screencap -p /sdcard/4.png"  # 命令1：在手机上截图3.png为图片名
# cmd2 = r"adb pull /sdcard/3.png d:/3.png"  # 命令2：将图片保存到电脑 d:/3.png为要保存到电脑的路径
# screen = Screenshot ()
# screen.screen ()

# adb shell getprop ro.build.version.release