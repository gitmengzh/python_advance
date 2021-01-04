#  装饰器

import time

# 简单装饰器实例， 计算程序运行时间
def run_time(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        costtime = end_time - start_time
        print("function cost time {}".format(costtime))
    return wrapper()
@run_time
def func1():
    time.sleep(1)

@run_time
def func2():
    time.sleep(2)

@run_time
def func():
    time.sleep(3)

#   带参数的装饰器

#   自定义属性的装饰器