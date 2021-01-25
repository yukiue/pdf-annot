# pdf-annot

Add annotations to the pdf file according to the ant file

An ant file is created by [doc-annotate](https://lsnl.jp/~ohsaki/software/elisp/doc-annotate.el).

# Usage

If `paper.pdf` and `papdf.ant` exist in the current working directory, run the following command.

```shell
python3 annot.py paper
```

# Requirements

- [PyMuPDF](https://github.com/pymupdf/PyMuPDF)

- [doc-annotate](https://lsnl.jp/~ohsaki/software/elisp/doc-annotate.el)
