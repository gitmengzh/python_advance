"""
re模块常用方法
https://zhuanlan.zhihu.com/p/68014839
"""

import re

pat = re.compile("A")           # compile(pattern)：创建模式对象


n1 = pat.search('ABC')
n2 = pat.search('CBDE')          # search(pattern,string)：在字符串中寻找模式



m1 = pat.match('aABCD')
m2 = pat.match('CBAA')

r1 = pat.split('SSSABBB')           # split(pattern,string)：根据模式分割字符串,返回列表


f1 = pat.findall('ABCAsskdjfieA')                  # findall(pattern,string)：列表形式返回匹配项


r2 = pat.sub('B', 'ACAD')                  # sub(pat,repl,string) ：用repl替换 pat匹配项

# 常用的函数方法

# group

# start

# end

# span



print(n1, n2)
print(m1, m2)
print(r1)
print(f1)
print(r2)