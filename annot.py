#!/usr/bin/env python3

import fitz


def add_annot(num_page, x, y, text):
    page = doc[num_page]
    size = page.MediaBoxSize
    width, height = size[0], size[1]
    print(width, height)
    page.addTextAnnot((width * x, y * height), text, icon='Comment')


def main():
    global doc
    doc = fitz.open('dummy.pdf')
    add_annot(0, 0.9, 0.5, 'str')

    doc.save('out.pdf')


if __name__ == "__main__":
    main()
