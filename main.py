import click
import numpy as np
from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot

from cut_path import CutPath
from point import Point


if __name__=='__main__':
    @click.command(context_settings=dict(ignore_unknown_options=True))

    test_stl = mesh.Mesh.from_file('part.stl')
    scale = test_stl.points.flatten()
    cut_scale = max(scale) - min(scale)

    cut_path = CutPath('cut_path1.csv')
    cut_path.set_scale(cut_scale)
    #cut_path.dump_points()

    figure = pyplot.figure()
    axes = mplot3d.Axes3D(figure)

    axes.add_collection3d(mplot3d.art3d.Poly3DCollection(test_stl.vectors))
    axes.plot3D(cut_path.get_coords('x'), cut_path.get_coords('y'), cut_path.get_coords('z'), color='red')


    print(scale)
    axes.auto_scale_xyz(scale, scale, scale)

    pyplot.show()
