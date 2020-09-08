'''
python 的递归
特点：
    要出现自身调用自身的现象
    要具有明确的结束标志

'''

# 递归斐波那契数  F(1)=1，F(2)=1, F(n)=F(n - 1)+F(n - 2)
def Fibonacci_sequence(n):
    if n ==1:
        result = 1
    elif n ==2:
        result = 2
    else:
        result = Fibonacci_sequence(n-1)+ Fibonacci_sequence(n-2)
    return result


def recursion():
    pass


if __name__ == "__main__":
    print(Fibonacci_sequence(10))