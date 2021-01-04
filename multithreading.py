#  python 多线程和线程池的使用

# import threadpool
# pool = ThreadPool(poolsize)
# requests = makeRequests(some_callable, list_of_args, callback)
# [pool.putRequest(req) for req in requests]
# pool.wait()


def aaa():
    num1 = 0
    num2 = 1
    try:
        res = num1/num1

    except BaseException as e:

        print("出错了,错误信息：{0}".format(e))
    else:
        print(res)
        print('else')
    finally:
        print("执行finally语句")

aaa()