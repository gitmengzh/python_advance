#  装饰器    https://zhuanlan.zhihu.com/p/269012332

import time

# 简单装饰器实例， 计算程序运行时间
def run_time(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        costtime = end_time - start_time
        print("function cost time {}".format(costtime))
    return wrapper
@run_time
def func1():
    time.sleep(1)

@run_time
def func2():
    time.sleep(2)

@run_time
def func3():
    time.sleep(3)


def log(func):
    def wrapper(*args, **kwargs):
        print("现在执行{}方法".format(func.__name__))
        func(*args, **kwargs)
        print("{}方法执行完成".format(func.__name__))
    return wrapper

@log
def add_func(a,b):
    print("{} + {} = {}".format(a, b, a+b))



#  带参数的装饰器


#  自定义属性的装饰器


if __name__ == "__main__":
    add_func(10, 20)
    func1()
    func2()
    func3()



