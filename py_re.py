# re 模块

import re

# match && fullmatch
# match 将符合条件的输出， fullmatch 如果全部符合，则输出，否则返回None
def match():
    # s1='abcabccba'
    # s2 = 'abcabcabc'
    # # match
    # a=re.match(r'([a-z]+)\1+',s1)
    # print(a, a.group())
    # b=re.match(r'([a-z]+)\1+',s2)
    # print(b)
    # print(b.group())
    # # fullmatch
    # c=re.fullmatch(r'([a-z]+)\1+',s1)
    # print(c)
    # d=re.fullmatch(r'([a-z]+)\1+',s2)
    # print(d)
    # print(d.group())
    s3 = 'sdfsdf234sdfsdf343'
    e = re.match(r'\d+', s3)
    print(e)

# search  # 搜索字符串
def search():
    s1 = 'abcaBccba'
    a = re.search(r'([a-z]+)\1+', s1, re.I)  # re.I 不区分大小写
    print(a.group())

# findall
def find():
    pattern = re.compile(r'\d+')  # 查找数字
    result1 = pattern.findall('runoob 123 google 456')
    result2 = pattern.findall('run88oob123google456', 0, 10)  # 在0-10中查找
    result3 = pattern.search('run88oob123google456')

    print(result1, result2, result3.group())

# re.sub 替换   re.sub(pattern, repl, string, count=0, flags=0) 正则，要替换的字符（可以是一个函数）， 目标字符串， 替换总数，默认0全部替换
def sub():
    s1 = 'Abcabccba'
    a = re.sub(r'([a-z]+)\1+', 'test', s1, re.I)  # re.I 不区分大小写
    print(a)

#  re.re.compile 函数
# compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用。
# re.compile(pattern[, flags])  pattern : 一个字符串形式的正则表达式  flags : 可选，表示匹配模式，比如忽略大小写，多行模式等
def compile(s):
    pattern = re.compile("({(.*)})")  # 搜索{}包含的内容   .* 就是单个字符匹配任意次，即贪婪匹配
    res = pattern.search(s)
    return res
if __name__ == "__main__":

    match()

