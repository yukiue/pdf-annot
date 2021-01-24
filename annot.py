#!/usr/bin/env python3

import re

import fitz


def add_annot(num_page, x, y, text):
    page = doc[num_page]
    size = page.MediaBoxSize
    width, height = size[0], size[1]
    # print(width, height)
    page.addTextAnnot((width * x, y * height), text, icon='Comment')


doc = fitz.open('dummy.pdf')

ant = ''
with open('dummy.ant') as f:
    for line in f:
        ant += line
# print(ant)

for s in re.split(r'#\+', ant):
    if 'annotation:' in s:
        regex = re.compile(
            r'annotation:\s(.+)\s(.+)\s(.+)\s-(.+)\s\[(.+)\]\n(.*)',
            re.MULTILINE | re.DOTALL)
        mo = regex.search(s)
        num_page = int(mo.groups()[0]) - 1
        x = float(mo.groups()[1])
        y = float(mo.groups()[2])
        name = mo.groups()[3]
        date = mo.groups()[4]
        text = mo.groups()[5]

        # print(num_page)
        # print(x)
        # print(y)
        # print(name)
        # print(date)
        # print(text)

        add_annot(num_page, x, y, text)

doc.save('out.pdf')

# if __name__ == "__main__":
#     main()
