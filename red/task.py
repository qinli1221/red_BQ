import traceback

from  appium import  webdriver
import time

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from red.screen_save import Screenshot
import random


def _init_():
    global driver
    desired_caps={}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '9'
    desired_caps['deviceName'] = '5JP0217819000194'

    # 配置app参数：包名、启动名
    desired_caps['appPackage'] = 'w2a.W2Aapp.kol1.vip'
    # desired_caps['appPackage'] = 'com.android.settings'
    # desired_caps['appActivity'] = 'com.android.settings.HWSettings'
    desired_caps['appActivity'] = 'io.dcloud.PandoraEntry'
    desired_caps['appWaitActivity']='io.dcloud.PandoraEntryActivity'

    desired_caps['autoGrantPermissions'] =True
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

    def wait_element(xpa):
        return WebDriverWait (driver, 15, 0.5).until (lambda x: x.find_element_by_xpath (xpa))

    def wait_list(xpa):
        return WebDriverWait (driver, 15, 0.5).until (lambda x: x.find_elements_by_xpath (xpa))

    # 等待弹窗加载
    inform = wait_element ('//*[contains(@text,"查看详情")]')

    # 点击关闭弹窗
    driver.tap([(540, 1490)])

    # 点击导航栏任务
    task = wait_list ('//*[contains(@text,"任务")]')
    try:
        # task[3].click()
        driver.tap([(400,1860)])
    except Exception as e:
        print(e)
    return driver

def wait_element(xpa):
        return WebDriverWait (driver, 3, 0.5).until (lambda x: x.find_element_by_xpath (xpa))

def wait_element_c(cla):
        return WebDriverWait (driver,3, 0.5).until (lambda x: x.find_element_by_class_name (cla))

def wait_element_id(id):
        return WebDriverWait (driver, 3, 0.5).until (lambda x: x.find_element_by_id (id))

def wait_list(xpa):
        return WebDriverWait (driver, 3, 0.5).until (lambda x: x.find_elements_by_xpath (xpa))

def wait_elements_c(cla):
        return WebDriverWait (driver, 3, 0.5).until (lambda x: x.find_elements_by_class_name (cla))

def get_task():
    global get
    # 领取任务列表

    get = False
    got_list = wait_list ('//*[contains(@text,"领取")]')
    for j in range (9):
        # 领取任务
        got_list[0].click ()
        limit = ''

        if j == 0:
            # 如果任务没有达到上限，继续领取，任务领取完成退出循环
            try:
                limit = wait_element ('//*[contains(@text,"已超出当前每天可领取的任务总量")]')
            except Exception as e:
                got_list[0].click ()
            if limit != '':
                # print ("领取超限啦，去做任务")
                get = True
                j=0
                break
            j += 1
    return get,j


def red_commit():
    # 点击去完成，跳转到小红书
    go_for = wait_element ('//*[contains(@text,"去完成")]')
    go_for.click ()

    # print ("评论小红书")
    try:
        comment = wait_element_id ('com.xingin.xhs:id/bn9')
        comment.click ()
    except Exception as e:
        driver.tap([(191,1836)])

    cos_list = ['i like it', 'good', 'cool', 'nice', 'dd', 'haha']
    cos = cos_list[random.randrange (0, 6)]
    # comment1.send_keys(rand)
    # print ('在小红书完成评论')
    try:
        comment1 = wait_element_c ('android.widget.EditText')
    except Exception as e:
        exstr = traceback.format_exc ()
        print (exstr)
        screen = Screenshot ()
        screen.screen ()
    # comment1.click ()
    # driver.set_value(comment1,rand)
    # print ('点击下方的表情')
    else:
        emo_list = wait_elements_c ('android.widget.ImageView')
        emo_list[3].click ()
        emo_list[4].click ()
        try:
            send = wait_element_id ('com.xingin.xhs:id/cgi')
            send.click ()
        except Exception as e:
            driver.tap([(977, 872)])
        # 调用截图类 保存截图
        screen = Screenshot ()
        screen.screen ()

    # exstr = traceback.format_exc ()
    # print(exstr)
    # print(e)
    # try:
    #     non = wait_element_id ('com.xingin.xhs:id/avatarLayout')
    #     # 调用截图类 保存截图
    #     screen = Screenshot ()
    #     screen.screen ()
    # except Exception as e:
    #     print ("不是加载问题")

    driver.keyevent (187)
    time.sleep (0.3)
    wait_element ('//*[contains(@text,"小红书达人")]').click ()


def submit_task():
    game = wait_element ('//*[contains(@text,"提交")]')
    game.click ()
    time.sleep (0.1)
    driver.tap ([(190, 1335)])
    # 定位相册
    try:
        item_list = wait_elements_c ('android.widget.LinearLayout')
        item_list[4].click ()
        # print ("定位")
    except Exception as e:
        # print ("绝对")
        driver.tap ([(950, 1275)])
    time.sleep (0.5)
    # 选择指定相册，图片，点击确认按钮
    selec_s = wait_element ('//*[contains(@text,"根目录")]')
    # print (selec_s.text)
    selec_s.click ()
    time.sleep (0.5)
    driver.tap ([(109, 361)])
    selec_pic = wait_element_id ('com.android.gallery3d:id/head_select_right')
    selec_pic.click ()

    submit = wait_list ('//*[contains(@text,"提交")]')
    time.sleep(1)
    driver.tap([(930,1730)])
    # for i in submit:
    #     if submit.index (i) > 2:
    #         i.click ()
    #         print (submit.index (i))

def do_task():
    times=0
    do = False
    # 我的任务列表
    my_task = wait_element ('//*[contains(@content-desc,"我的任务")]')
    my_task.click ()
    for k in range (10):
        # 如果有任务，点击任务列表第一个任务，没有任务退出循环
        comp_list = []
        try:
            print("a")
            comp_list = wait_list ('//*[contains(@content-desc,"去")]')
        except Exception as e:
            # print ("任务执行完了")
            do = True
        if len (comp_list) > 0:
            comp_list[0].click ()
        else:
            # print ("退出循环")
            break

        # print(k)
        red_commit()
        # 点击提交按钮上传任务图片,提交任务
        submit_task()
        # print("提交成功")
        try:
            wait = wait_element ('//*[contains(@text,"待审核")]')
            # print("待审核")
        except Exception as e:
            time.sleep (0.3)
        driver.tap ([(61, 116)])
        times += 1
        # print ("已完成任务：", times)
        time.sleep (0.3)
    return times,do
    # inform = wait_element('//*[contains(@text,"公告")]')
    #
    # task = wait_list('//*[contains(@text,"任务")]')
    # got_list = wait_list('//*[contains(@text,"领取")]')
    # wait_for = wait_element('//*[contains(@text,"操作成功")]')
    # limit = wait_element ('//*[contains(@text,"已超出当前每天可领取的任务总量")]')
    # my_task = wait_element('//*[contains(@text,"我的任务")]')
    # to_do =wait_element ('//*[contains(@text,"待完成")]')
    # comp_list = wait_list('//*[contains(@text,"去完成")]')
    # go_for= wait_element ('//*[contains(@text,"完成")]')
    # comment = wait_element_id('com.xingin.xhs:id/bds')
    # comment1 = wait_element_c('android.widget.EditText')
    # emo_list = wait_elements_c('android.widget.ImageView')
    # send = wait_element_id('com.xingin.xhs:id/c6s')
    # game = wait_element ('//*[contains(@text,"提交")]')
    # tab_list = wait_elements_c('android.view.View')
    #
    # # 定位相册
    # item_list = wait_elements_c('android.widget.LinearLayout')
    # game_overs =  wait_list ('//*[contains(@text,"提交")]')
    #
    # game_overs =wait_list(('//*[contains(@text,"提交")]'))
    #
    # wait = wait_element('//*[contains(@text,"待审核")]')
def change_user(mobie):
    if mobie == 18015409532:
        pwd = "04559072w"
    elif mobie == 17751264476:
        pwd = "cares2018"
    driver.tap([(94,1834)])
    time.sleep(0.3)
    try:
        wait_element('//*[contains(@text,"我的收款信息")]')
    except Exception as e:
        print("现在的页面不是我的")
    driver.tap([(1000, 150)])
    time.sleep (0.3)
    wait_element('//*[contains(@text,"退出账号")]').click()
    wait_element('//*[contains(@text,"确认退出当前账号吗")]')
    time.sleep(0.3)
    driver.tap ([(900, 1100)])
    try:
        wait_element('//*[contains(@text,"忘记密码")]')
    except Exception as e:
        eles = wait_elements_c("android.view.View")
        for i in eles:
            print(i.text)
    mob = wait_element('//*[contains(@text,请输入手机号")]')
    mob.click()
    mob.driver.send_keys(mobie)
    passwd = wait_element ('//*[contains(@text,请输入密码")]')
    passwd.click()
    passwd.driver.send_keys(mobie)

