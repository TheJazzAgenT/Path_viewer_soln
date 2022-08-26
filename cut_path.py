import csv

from point import Point


class CutPath:
    """
    A class used to represent a path to be cut, represented by a csv file

    Attributes
    ----------
    csv_file : str
        path to csv file on disk
    points : List(Point)
        a list of Point objects, representing the path to be cut
    scale : float
        the scale of the stl file

    Methods
    -------
    read_csv(csv_file=None)
        reads in a csv file. Called on construction if a csv is provided
    dump_points()
        prints all points in path to console
    get_coords(axis)
        returns a list of the {axis} coordinate for each point in points
    set_scale(scale)
        set the scale for this cut path
    """

    def __init__(self, csv_file=None, scale=1):
        """
        Parameters
        ----------
        csv_file : str
            path to csv file on disk
        scale : float
            scale at which points should be scaled by (default 1)
        """

        self.csv_file = csv_file
        self.points = []
        if self.csv_file is not None:
            self.read_csv()
        self.scale = scale

    def read_csv(self, csv_file=None):
        """Reads in a csv file if one was not provided in the constructor

        Paramaters
        ----------
        csv_file : str
            path to csv file on disk

        Returns
        -------
        int
            number of csv lines that could not be read as valid points
        """

        if csv_file is not None:
            self.csv_file = csv_file

        with open(self.csv_file) as csv_file:
            csv_reader = csv.reader(csv_file)
            line_count = -1
            bad_lines = 0

            for row in csv_reader:
                line_count += 1
                if line_count == 0:
                    continue

                if self.__check_row(row):
                    self.points.append(Point(*row[:3]))

                else:
                    bad_lines += 1

        print('CSV read')
        print('found {} errors'.format(bad_lines))
        print('found {} valid points'.format(len(self.points)))

        return bad_lines

    def __check_row(self, row):
        """Validate a row in an input csv file
        """

        if len(row) != 10:
            return False

        for point in row[:3]:
            if not point:
                return False
            pt = float(point)
            if pt < -1 or pt > 1:
                return False

        return True

    def dump_points(self):
        """Print a list of points in this path to console
        """

        for pt in self.points:
            print(pt.to_str())

    def get_coords(self, axis):
        """Get a list of coordinates on a given axis

        Parameters
        ----------
        axis : str
            [x | y | z] specifying the axis you want to get coordinates on

        Returns
        -------
        list
            A list of coordinate's values for the given axis
        """

        if axis == 'x':
            return [pt.x * self.scale for pt in self.points]
        elif axis == 'y':
            return [pt.y * self.scale for pt in self.points]
        elif axis == 'z':
            return [pt.z * self.scale for pt in self.points]
        else:
            raise Exception('ERROR: bad axis value (must be [x|y|z])')

    def set_scale(self, scale):
        """Set the scale to apply to all coordinates

        Parameters
        ----------
        scale : float
            scale to apply to all coordinates
        """

        self.scale = scale
