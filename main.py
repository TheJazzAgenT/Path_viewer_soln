import csv

import numpy as np
from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot


class Point:
    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def to_str(self):
        return '({}, {}, {})'.format(self.x, self.y, self.z)

class CutPath:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.points = []
        self.read_csv()
        self.scale = 1

    def read_csv(self):
        with open(self.csv_file) as csv_file:
            csv_reader = csv.reader(csv_file)
            line_count = -1
            bad_lines = 0

            for row in csv_reader:
                line_count += 1
                if line_count == 0:
                    continue

                if self.check_row(row):
                    self.points.append(Point(*row[:3]))

                else:
                    bad_lines += 1

        print('CSV read')
        print('found {} errors'.format(bad_lines))
        print('found {} valid points'.format(len(self.points)))

    def check_row(self, row):
        if len(row) != 10:
            return False

        for point in row:
            if not point:
                return False
            pt = float(point)
            if pt < -1 or pt > 1:
                return False

        return True

    def dump_points(self):
        for pt in self.points:
            print(pt.to_str())

    def get_coords(self, axis):
        if axis == 'x':
            return [pt.x * self.scale for pt in self.points]
        elif axis == 'y':
            return [pt.y * self.scale for pt in self.points]
        elif axis == 'z':
            return [pt.z * self.scale for pt in self.points]
        else:
            print('problem')

    def set_scale(self, scale):
        self.scale = scale


if __name__=='__main__':
    test_stl = mesh.Mesh.from_file('part.stl')
    scale = test_stl.points.flatten()
    cut_scale = max(scale) - min(scale)

    cut_path = CutPath('cut_path1.csv')
    cut_path.set_scale(cut_scale)
    #cut_path.dump_points()

    figure = pyplot.figure()
    axes = mplot3d.Axes3D(figure)

    axes.add_collection3d(mplot3d.art3d.Poly3DCollection(test_stl.vectors))
    axes.plot3D(cut_path.get_coords('x'), cut_path.get_coords('y'), cut_path.get_coords('z'), color='red', linewidth=2)


    print(scale)
    axes.auto_scale_xyz(scale, scale, scale)

    pyplot.show()
