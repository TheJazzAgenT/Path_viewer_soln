class Point:
    """
    Class used to represent a point within a cut path

    Attributes
    ----------
    x : float
        x value
    y : float
        y value
    z : float
        z value
    """
    
    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __repr__(self):
        return '({}, {}, {})'.format(self.x, self.y, self.z)
