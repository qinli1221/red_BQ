import time
import traceback
from red.task import _init_,wait_list,wait_element,wait_element_c,wait_element_id,wait_elements_c,get_task,do_task


driver = _init_()
time.sleep(2)
ti = time.time()
print("进入大厅")

do_times = 0
for i in range(40):
    get =False
    do =False
    try:
        (get,tiss) = get_task()
        print("已领取任务数：",tiss)
        print(get)
    except Exception as e:
        exstr = traceback.format_exc ()
        print(exstr)
        print("没有领取任务")
    try:
        (times,do) = do_task()
        do_times += times
        print(do_times,do)
    except Exception as e:
        print("执行任务失败")
    print("已执行任务：",do_times)
    try:
        task_hall = wait_element('//*[contains(@text,"任务大厅")]')
        task_hall.click()
    except Exception as e:
        driver.quit()
        driver = _init_()
    if get==True and do==True:
        break
tt = time.time()
print("运行时间",tt-ti)
driver.quit()