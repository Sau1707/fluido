import matplotlib.pyplot as plt

from src.simbols import x, y, z
from src.simbols import u, v, w
from src.simbols import a, b, c
from src.simbols import A, U
from src.texprint import texprint

# Compute (u · ∇) alpha
u_dot_grad_alpha = A.jacobian([x, y, z]).T @ U

texprint(u_dot_grad_alpha)