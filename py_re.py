# re 模块

import re

# match && fullmatch
# match 将符合条件的输出， fullmatch 如果全部符合，则输出，否则返回None
def match():
    s1='abcabccba'
    s2 = 'abcabcabc'
    # match
    a=re.match(r'([a-z]+)\1+',s1)
    print(a, a.group())
    b=re.match(r'([a-z]+)\1+',s2)
    print(b)
    print(b.group())
    # fullmatch
    c=re.fullmatch(r'([a-z]+)\1+',s1)
    print(c)
    d=re.fullmatch(r'([a-z]+)\1+',s2)
    print(d)
    print(d.group())


def aaa(arr):
    res = arr[0]
    for i in range(1, len(arr)):
        if arr[i-1]>0:
            arr[i] += arr[i-1]
        res = max(arr[i], res)
    return res

if __name__ == "__main__":
    arr = [-2,1,-3,4,-1,2,1,-5,4]
    print(aaa(arr))

