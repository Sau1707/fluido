from sympy import latex
from IPython.display import display, Math


def texprint(*args, **kwargs):
    print(latex(*args), **kwargs)


def texdisplay(*args, **kwargs):
    display(Math(latex(*args), **kwargs))