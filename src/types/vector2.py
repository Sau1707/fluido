from sympy import Matrix, diff, Function, symbols, sin, cos, exp, Expr, sqrt, atan2


class Vector2(Matrix):
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
    