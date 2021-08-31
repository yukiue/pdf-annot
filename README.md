# pdf-annot

Add annotations to the pdf file according to the corresponding ant file

An ant file is created by [doc-annotate](https://lsnl.jp/~ohsaki/software/elisp/doc-annotate.el).

# Usage

If `paper.pdf` and `paper.ant` exist in the current working directory, run one of the following commands.

```shell
python3 annot.py paper
```

```shell
python3 annot.py paper.ant
```

```shell
python3 annot.py paper.pdf
```

Then, the annotated pdf file named `paper-annotated.pdf` will be generated.

# Requirements

- [PyMuPDF](https://github.com/pymupdf/PyMuPDF)

- [doc-annotate](https://lsnl.jp/~ohsaki/software/elisp/doc-annotate.el)
