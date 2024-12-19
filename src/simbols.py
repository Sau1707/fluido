from sympy import symbols, Function, Matrix

x = symbols('x')
y = symbols('y')
z = symbols('z')

a = Function('a')(x, y, z)
b = Function('b')(x, y, z)
c = Function('c')(x, y, z)

u = Function('u')(x, y, z)
v = Function('v')(x, y, z)
w = Function('w')(x, y, z)

U = Matrix([u, v, w])
A = Matrix([a, b, c])