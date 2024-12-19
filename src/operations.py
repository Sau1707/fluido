from sympy import Matrix, diff, Function, symbols, sin, cos, exp, Expr

x = symbols('x')
y = symbols('y')
z = symbols('z')

a = Function('a')(x, y)

u = a - 5
v = sin(x) + cos(y) + z
w = exp(x) + 9 * y

u = Function('u')(x, y, z)
v = Function('v')(x, y, z)
w = Function('w')(x, y, z)

class Vector3(Matrix):
    def __new__(cls, coords, system='cartesian'):
        obj = super().__new__(cls, Matrix([[c] for c in coords]))
        obj._system = system
        return obj

    def __init__(self, coords, system='cartesian'):
        self._system = system
        assert system in ['cartesian', 'cylindrical'], "The coordinate system must be either 'cartesian' or 'cylindrical'."
    
    @property
    def system(self):
        return self._system
    

U = Vector3([u, v, w])


def div(U: Vector3) -> Expr:
    """
    Compute the divergence of a vector field U.

    Cartesian coordinates U = (u, v, w)^T is given by:
    div U = ∇ · U = ∂u/∂x + ∂v/∂y + ∂w/∂z

    Ciylindrical coordinates U = (r, θ, x)^T is given by:
    div U = ∇ · U = (1 / r) * ∂/∂r * (r * U_r) + (1 /r) ∂U_θ/∂θ + ∂U_x/∂x

    Returns a scalar quantity that represents the net rate of flow of a vector field's "flux" out of an infinitesimal volume. 
    It provides insight into how much the field is "spreading out" or "converging" at a given point.

    Fluid Dynamics:
    - Divergence is a measure of the rate of expansion of a fluid at a given point.
    - If div U > 0, the fluid is expanding.
    - If div U < 0, the fluid is contracting.


    Notes:
    - divergenzfrei := div U = 0

    """
    if U.system == 'cartesian':
        U_u = U[0]
        U_v = U[1]
        U_w = U[2]
        divergence = diff(U_u, x) + diff(U_v, y) + diff(U_w, z)

    if U.system == 'cylindrical':
        u_r = U[0]
        u_theta = U[1]
        u_x = U[2]
        divergence = (1 / x) * diff(x * u_r, x) + (1 / x) * diff(u_theta, y) + diff(u_x, z)

    assert divergence is not None, "The divergence of the vector field U is not defined."
    return divergence


def grad(a: float):
    pass


def rot():
    pass


if __name__ == "__main__":
    print(div(U))
    print(div(U).subs({x: 1, y: 2, z: 3}))