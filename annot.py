#!/usr/bin/env python3
#
# usage: python3 annot.py basename

import os
import re
import sys

import fitz


def add_annot(num_page, x, y, text):
    '''
    num_page: page number (zero-based indexing)
    x: normalized x coordinate (0.0 ~ 1.0)
    y: normalized y coordinate (0.0 ~ 1.0)
    (The top-left corner is the origin.)
    text: commentary text
    '''
    page = doc[num_page]
    size = page.MediaBoxSize
    width, height = size[0], size[1]
    # print(width, height)
    page.addTextAnnot((width * x, height * y), text, icon='Comment')


basename = os.path.splitext(os.path.basename(sys.argv[1]))[0]
doc = fitz.open(f'{basename}.pdf')

ant = ''
with open(f'{basename}.ant') as f:
    for line in f:
        ant += line

for s in re.split(r'#\+', ant):
    if 'annotation:' in s:
        regex = re.compile(
            r'annotation:\s(.+)\s(.+)\s(.+)\s-(.+)\s\[(.+)\]\n(.*)',
            re.MULTILINE | re.DOTALL)
        mo = regex.search(s)
        num_page = int(mo.groups()[0]) - 1
        x = float(mo.groups()[1])
        y = float(mo.groups()[2])
        # name = mo.groups()[3]
        # date = mo.groups()[4]
        text = mo.groups()[5]

        add_annot(num_page, x, y, text)

doc.save(f'{basename}-annotated.pdf')

# if __name__ == "__main__":
#     main()
