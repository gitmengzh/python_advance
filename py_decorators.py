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



#  带参数的装饰器

def log(func):
    def wrapper(*args, **kwargs):       # 不固定参数
        print("现在执行{}方法".format(func.__name__))
        func(*args, **kwargs)
        print("{}方法执行完成".format(func.__name__))
    return wrapper

@log
def add_func1(a,b):
    print("{} + {} = {}".format(a, b, a+b))

@log
def add_func2(a,b,c):
    print("{}+{}+{}={}".format(a,b,c,a+b+c))



# 使用多个装饰器   从上到下依次执行
def deco01(func):
    def wrapper(*args, **kwargs):
        print("deco01 running")
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        cost_time = end_time - start_time
        print("cost time is %d" %cost_time)
        print("deco01 end")
    return wrapper

def deco02(func):
    def wrapper(*args, **kwargs):
        print("deco02 running")
        func(*args, **kwargs)
        print("deco02 end")
    return wrapper

@deco02
@deco01
def muilt_func(a, b):
    time.sleep(1)
    print(a+b)

# python内置装饰器
'''
staticmethod
classmethod
property
'''

# 参数化装饰器
def repeat(number=3):
    """多次重复执行原始函数，返回最后一次调用的值作为结果"""
    def actual_decorator(func):
        def wrapper(*args, **kwargs):
            result = None
            for i in range(number):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return actual_decorator

@repeat()  # 即使有默认参数，这里的括号也不能省略
def f():
    print("喵")

@repeat(2)
def g(a,b):
    print("g函数执行中")
    return a + b

# 使用第三方优化
from decorator import decorator
from datetime import datetime

@decorator
def logging(func, *args, **kwargs):
    print(f"[DEBUG] {datetime.now()}: enter {func.__name__}()")
    return func(*args, **kwargs)

@logging
def f(a, b):
    return a + b


#  自定义属性的装饰器


if __name__ == "__main__":
    # add_func1(10, 20)
    # add_func2(10, 20, 30)
    # func1()
    # func2()
    # func3()
    # muilt_func(10, 20)
    f()
    print(g(1,2))





