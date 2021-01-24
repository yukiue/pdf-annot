#!/usr/bin/env python3

import re

# with open('dummy.ant') as f:
#     for line in f:
#         print(line)

line = '#+annotation: 1 0.022 0.086 -xxx [2021/01/25]'

regex = re.compile(r'\#\+annotation:\s(.+)\s(.+)\s(.+)\s-(.+)\s\[(.+)\]')

# regex = re.compile(r'\#\+annotation:\s(.+)\s(.+)\s(.+)\s-(.+)\s[(.+)]')

mo = regex.search(line)

num_page = int(mo.groups()[0]) - 1
x = float(mo.groups()[1])
y = float(mo.groups()[2])
name = mo.groups()[3]
date = mo.groups()[4]

print(num_page)
print(x)
print(y)
print(name)
print(date)
