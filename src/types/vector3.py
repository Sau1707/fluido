from sympy import Matrix, diff, Function, symbols, sin, cos, exp, Expr, sqrt, atan2


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
    
    @property
    def cartesian(self):
        if self._system == 'cartesian':
            return self
        elif self._system == 'cylindrical':
            r, theta, z = self[0], self[1], self[2]
            x = r * cos(theta)
            y = r * sin(theta)
            return Vector3([x, y, z], system='cartesian')
        else:
            raise ValueError("Unsupported coordinate system: " + self._system)

    @property
    def cylindrical(self):
        if self._system == 'cylindrical':
            return self
        elif self._system == 'cartesian':
            x, y, z = self[0], self[1], self[2]
            r = sqrt(x**2 + y**2)
            theta = atan2(y, x)
            return Vector3([r, theta, z], system='cylindrical')
        else:
            raise ValueError("Unsupported coordinate system: " + self._system)